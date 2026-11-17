#!/usr/bin/env python3
"""Read only the calling Codex thread's emitted rate-limit meter.

No credentials or message bodies are returned. This is account-window usage,
not a separate session allowance. --guard refuses a new lesson at >=95% used.
"""
import argparse
import json
import os
from pathlib import Path


def latest_usage():
    thread=os.environ.get('CODEX_THREAD_ID')
    if not thread:return {'available':False,'reason':'CODEX_THREAD_ID is not exposed'}
    paths=list((Path.home()/'.codex/sessions').rglob('*'+thread+'.jsonl'))
    if not paths:return {'available':False,'reason':'Current-thread log not found'}
    last=None
    with max(paths,key=lambda p:p.stat().st_mtime).open() as stream:
        for line in stream:
            try:event=json.loads(line)
            except ValueError:continue
            p=event.get('payload',{})
            if event.get('type')=='event_msg' and p.get('type')=='token_count' and p.get('rate_limits'):
                limits=p['rate_limits'];windows=[]
                for key in ['primary','secondary']:
                    w=limits.get(key)
                    if w and isinstance(w.get('used_percent'),(int,float)):
                        windows.append({'window':key,'remaining_percent':100-w['used_percent'],
                                        'window_minutes':w.get('window_minutes'),'resets_at':w.get('resets_at')})
                if windows:
                    info=p.get('info') or {};window=info.get('model_context_window')
                    usage=info.get('last_token_usage') or {}
                    context=100*(1-usage.get('total_tokens',0)/window) if window else None
                    remaining=min(w['remaining_percent'] for w in windows)
                    last={'available':True,'timestamp':event.get('timestamp'),
                          'remaining_percent':min(remaining,context) if context is not None else remaining,
                          'account_remaining_percent':remaining,'context_remaining_percent':round(context,2) if context is not None else None,
                          'windows':windows,'scope':'Minimum of account-window and context-capacity remaining; no separate session quota is exposed'}
    return last or {'available':False,'reason':'No emitted rate-limit meter found'}


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--guard',action='store_true');a=p.parse_args()
    report=latest_usage();print(json.dumps(report,indent=2))
    if a.guard and (not report['available'] or report['remaining_percent']<=5):raise SystemExit(75)
