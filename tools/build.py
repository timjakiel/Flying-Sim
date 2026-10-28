"""Build index.html: the game (src/game.html) with the music packed inside it.

The artifact viewer and other ways of opening the page (a local file, a file viewer) can block
the page from fetching files, so the songs in audio/ are embedded as base64 text blocks that the
game decodes itself. index.html is the file to open, share and publish; edit src/game.html.
Usage: python3 tools/build.py
"""
import base64, datetime, pathlib

root = pathlib.Path(__file__).resolve().parent.parent
html = (root / 'src' / 'game.html').read_text(encoding='utf-8')
blocks = ''
for name in ('menu', 'waves', 'boss'):
    data = base64.b64encode((root / 'audio' / f'{name}-theme.mp3').read_bytes()).decode()
    blocks += f'<script type="text/plain" id="aud-{name}">{data}</script>\n'
marker = '<script src="https://cdn.jsdelivr.net/npm/three@'
assert html.count(marker) == 1, 'three.js script tag not found'
stamp = datetime.datetime.now(datetime.timezone.utc).strftime('%m%d-%H%M')  # shown on the menu, to tell copies apart
assert html.count("const BUILD = 'dev'") == 1 and html.count('build dev') == 1
html = html.replace("const BUILD = 'dev'", f"const BUILD = '{stamp}'").replace('build dev', f'build {stamp}')
out = root / 'index.html'
out.write_text('<!-- Built by tools/build.py from src/game.html, with the music packed in. Edit src/game.html, not this file. -->\n'
               + html.replace(marker, blocks + marker), encoding='utf-8')
print(f'{out} ({out.stat().st_size / 1e6:.1f} MB)')
