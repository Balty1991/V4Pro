#!/usr/bin/env python3
import json
import os
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA = ROOT / 'data'
DATA.mkdir(exist_ok=True)


def write_json(name, payload):
    (DATA / name).write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def now_utc():
    return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')


def main():
    token = os.getenv('BSD_TOKEN', '').strip()
    if not token:
        raise SystemExit('BSD_TOKEN lipsește. Adaugă secretul în GitHub Actions înainte să rulezi workflow-ul.')

    meta = {
        'status': 'token_detected_placeholder_fetcher',
        'generated_at': now_utc(),
        'source': 'BSD Sports Data API',
        'note': 'Fetcher placeholder încărcat. Poți înlocui ulterior cu varianta completă din arhiva locală.'
    }

    write_json('meta.json', meta)
    for file_name, payload in {
        'predictions.json': [],
        'recommendation_log.json': [],
        'history_engine.json': [],
        'ai_memory.json': {},
        'signal_audit.json': {},
        'top3_daily.json': [],
        'cota2_daily.json': [],
        'live.json': []
    }.items():
        write_json(file_name, payload)

    print('Placeholder fetch completed at', meta['generated_at'])


if __name__ == '__main__':
    main()
