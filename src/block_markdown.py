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


def block_to_block_type(block):
    heading_re = r"^(#{1,6}) (.*)"
    code_re = r"^```(.*?)```$"
    unordered_list_re = r"^[*-] "
    ordered_list_re = r"^\d+\..*"

    if re.match(heading_re, block):
        return "heading"
    elif re.match(code_re, block, re.DOTALL):
        return "code"
    elif all(line.startswith(">") for line in block.split("\n")):
        return "quote"
    elif all(line.startswith(("* ", "- ")) for line in block.split("\n")):
        return "unordered_list"
    elif re.match(ordered_list_re, block):
        lines = block.split("\n")
        numbers = [int(line.split(". ")[0]) for line in lines]
        if numbers == list(range(1, len(numbers) + 1)):
            return "ordered_list"
    return "paragraph"
