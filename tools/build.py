"""Build the published page: index.html with the music packed inside it.

The artifact viewer blocks the page from fetching files, so the songs in audio/ are
embedded as base64 text blocks that the game decodes itself. Writes build/index.html.
Usage: python3 tools/build.py
"""
import base64, pathlib

root = pathlib.Path(__file__).resolve().parent.parent
html = (root / 'index.html').read_text()
blocks = ''
for name in ('menu', 'boss'):
    data = base64.b64encode((root / 'audio' / f'{name}-theme.mp3').read_bytes()).decode()
    blocks += f'<script type="text/plain" id="aud-{name}">{data}</script>\n'
marker = '<script src="https://cdn.jsdelivr.net/npm/three@'
assert html.count(marker) == 1, 'three.js script tag not found'
out = root / 'build' / 'index.html'
out.parent.mkdir(exist_ok=True)
out.write_text(html.replace(marker, blocks + marker))
print(f'{out} ({out.stat().st_size / 1e6:.1f} MB)')
