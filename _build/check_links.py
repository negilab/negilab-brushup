# 相対リンク・CSS参照のリンク切れとページ内アンカーを確認する
import os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
bad = 0
pages = []
for d, _, fs in os.walk(ROOT):
    if '.git' in d or '_build' in d:
        continue
    pages += [os.path.join(d, f) for f in fs if f.endswith('.html')]

ids = {}
for pg in pages:
    ids[os.path.normpath(pg)] = set(re.findall(r'id="([^"]+)"', open(pg, encoding='utf-8').read()))

for pg in pages:
    html = open(pg, encoding='utf-8').read()
    if 'name="robots" content="noindex,nofollow"' not in html:
        print('robots missing:', pg); bad += 1
    for url in re.findall(r'(?:href|src)="([^"]+)"', html):
        if re.match(r'^(https?:|mailto:)', url):
            continue
        path, _, frag = url.partition('#')
        target = os.path.normpath(os.path.join(os.path.dirname(pg), path)) if path else os.path.normpath(pg)
        if not os.path.isfile(target):
            print('broken:', os.path.relpath(pg, ROOT), '->', url); bad += 1
        elif frag and frag not in ids.get(target, set()):
            print('anchor missing:', os.path.relpath(pg, ROOT), '->', url); bad += 1
        if url.startswith('/'):
            print('root-absolute:', os.path.relpath(pg, ROOT), '->', url); bad += 1

print(f'{len(pages)} pages checked, {bad} problems')
sys.exit(1 if bad else 0)
