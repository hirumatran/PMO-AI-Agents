"""Build the OEPM dashboard from the template.

Usage:  python3 dashboard/build.py   (needs Pillow)

Outputs
  dashboard/oepm-dashboard.html          local / internal version, with the Olympus logo
  dashboard/oepm-dashboard.publish.html  claude.ai version: no logo, no doctype (the Artifact tool adds its own skeleton)
"""
import base64
import io
import pathlib
import re

from PIL import Image

ROOT = pathlib.Path(__file__).resolve().parent.parent
DASH = ROOT / "dashboard"
ASSETS = ROOT / "assets"


def avatar(name: str) -> str:
    im = Image.open(ASSETS / "avatars" / f"{name}.jpg").convert("RGB").resize((192, 192), Image.LANCZOS)
    buf = io.BytesIO()
    im.save(buf, "JPEG", quality=82)
    return base64.b64encode(buf.getvalue()).decode()


tpl = (DASH / "oepm-dashboard.template.html").read_text(encoding="utf-8")
for n in ("hiruma", "chopper", "jarvis"):
    tpl = tpl.replace("{{%s}}" % n.upper(), avatar(n))

logo = base64.b64encode((ASSETS / "olympus-logo.png").read_bytes()).decode()
(DASH / "oepm-dashboard.html").write_text(tpl.replace("{{LOGO}}", logo), encoding="utf-8")

pub = re.sub(r'<span class="logo-plate">.*?</span>', '<span class="wordmark">OEPM</span>', tpl, count=1)
pub = pub.replace('<div class="brandmark">OEPM · OLYMPUS VIETNAM</div>', '<div class="brandmark">OPERATIONAL EXCELLENCE PMO</div>')
pub = pub.replace("<!doctype html>\n", "", 1)
assert "{{" not in pub and "logo-plate\"><img" not in pub
(DASH / "oepm-dashboard.publish.html").write_text(pub, encoding="utf-8")
print("built:", DASH / "oepm-dashboard.html", "and", DASH / "oepm-dashboard.publish.html")
