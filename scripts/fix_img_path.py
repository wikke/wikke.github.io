import re
from pathlib import Path

PREFIX = '/posts/'
REGEXP = 'src=\"(.+?).assets'

def add_prefix(match):
    return f"src=\"{PREFIX}{match.group(1)}.assets"

for html in Path("docs/posts").glob("*/index.html"):
    with open(html) as f:
        content = f.read()
        
    content = re.sub(REGEXP, add_prefix, content)

    with open(html, 'w') as f:
        f.write(content)
