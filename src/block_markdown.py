import re

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_link,
    text_type_image,
)


def markdown_to_blocks(markdown):
    blocks = re.split(r"\n\s*\n", markdown)
    blocks = [block.strip() for block in blocks]
    return list(filter(None, blocks))
