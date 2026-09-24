import re


def slugify(text):
    """Lowercase text and collapse non-ASCII-alphanumeric runs to hyphens."""
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
