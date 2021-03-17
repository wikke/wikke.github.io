import re
from pathlib import Path

PREFIX = '/posts/'
REGEXP = 'src=\"(.+?).assets'
# <p><img src="github-pages-with-hugo.assets/11.jpeg" alt="11"></p>

def add_prefix(match):
    return f"src=\"{PREFIX}{match.group(1)}.assets"

for html in Path("public/posts").glob("*/index.html"):
    with open(html) as f:
        content = f.read()

    # print(content)
    content = re.sub(REGEXP, add_prefix, content)
    # print(content)

    with open(html, 'w') as f:
        f.write(content)
