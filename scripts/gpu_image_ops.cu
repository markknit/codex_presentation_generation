// CUDA pixel operations for slide-preview resizing and raster quality signals.
#include <cuda_runtime.h>
#include <cstdio>
__global__ void resize_rgb(const unsigned char* src, int w, int h, unsigned char* dst, int ow, int oh) {
    int i=blockIdx.x*blockDim.x+threadIdx.x;
    if(i>=ow*oh) return;
    int x=i%ow, y=i/ow;
    for(int c=0;c<3;c++) dst[i*3+c]=src[((y*h/oh)*w+x*w/ow)*3+c];
}
__global__ void count_ink(const unsigned char* src,int n,unsigned int* counts) {
    int i=blockIdx.x*blockDim.x+threadIdx.x;
    if(i>=n) return;
    int lo=min((int)src[i*3],min((int)src[i*3+1],(int)src[i*3+2]));
    if(lo<240) atomicAdd(counts,1U);
    if(lo<100) atomicAdd(counts+1,1U);
}
extern "C" int gpu_resize(const unsigned char* src,int w,int h,unsigned char* dst,int ow,int oh,unsigned int* counts) {
    unsigned char *a=nullptr,*b=nullptr; unsigned int* c=nullptr;
    cudaError_t err;
    #define CHECK(call) if((err=(call))!=cudaSuccess) {std::fprintf(stderr,"CUDA: %s\n",cudaGetErrorString(err)); goto done;}
    CHECK(cudaMalloc(&a,(size_t)w*h*3)); CHECK(cudaMalloc(&b,(size_t)ow*oh*3)); CHECK(cudaMalloc(&c,2*sizeof(unsigned int)));
    CHECK(cudaMemcpy(a,src,(size_t)w*h*3,cudaMemcpyHostToDevice)); CHECK(cudaMemset(c,0,2*sizeof(unsigned int)));
    resize_rgb<<<(ow*oh+255)/256,256>>>(a,w,h,b,ow,oh); CHECK(cudaGetLastError());
    count_ink<<<(w*h+255)/256,256>>>(a,w*h,c); CHECK(cudaGetLastError()); CHECK(cudaDeviceSynchronize());
    CHECK(cudaMemcpy(dst,b,(size_t)ow*oh*3,cudaMemcpyDeviceToHost)); CHECK(cudaMemcpy(counts,c,2*sizeof(unsigned int),cudaMemcpyDeviceToHost));
    done: cudaFree(a);cudaFree(b);cudaFree(c);return (int)err;
}
