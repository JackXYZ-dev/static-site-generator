import unittest
import re
from block_markdown import markdown_to_blocks, block_to_block_type


class TestMarkdownToBlocks(unittest.TestCase):
    def test_empty_markdown(self):
        markdown = ""
        expected = []
        self.assertEqual(markdown_to_blocks(markdown), expected)

    def test_single_block(self):
        markdown = "This is a single block of text."
        expected = ["This is a single block of text."]
        self.assertEqual(markdown_to_blocks(markdown), expected)

    def test_multiple_blocks(self):
        markdown = "This is the first block.\n\nThis is the second block."
        expected = ["This is the first block.", "This is the second block."]
        self.assertEqual(markdown_to_blocks(markdown), expected)

    def test_blocks_with_leading_trailing_whitespace(self):
        markdown = "   This is a block with leading and trailing whitespace.   \n\n  This is another block with whitespace.  "
        expected = [
            "This is a block with leading and trailing whitespace.",
            "This is another block with whitespace.",
        ]
        self.assertEqual(markdown_to_blocks(markdown), expected)

    def test_blocks_with_empty_lines(self):
        markdown = "This is a block.\n\n\nThis is another block."
        expected = ["This is a block.", "This is another block."]
        self.assertEqual(markdown_to_blocks(markdown), expected)

    def test_blocks_with_multiple_empty_lines(self):
        markdown = "This is a block.\n\n\nThis is another block."
        expected = ["This is a block.", "This is another block."]
        self.assertEqual(markdown_to_blocks(markdown), expected)

    def test_heading(self):
        block = "# Heading"
        self.assertEqual(block_to_block_type(block), "heading")

    def test_code_block(self):
        block = "```\ncode\n```"
        self.assertEqual(block_to_block_type(block), "code")

    def test_quote_block(self):
        block = "> Quote"
        self.assertEqual(block_to_block_type(block), "quote")

    def test_unordered_list(self):
        block = "- Item 1\n- Item 2"
        self.assertEqual(block_to_block_type(block), "unordered_list")

    def test_ordered_list(self):
        block = "1. Item 1\n2. Item 2"
        self.assertEqual(block_to_block_type(block), "ordered_list")

    def test_invalid_ordered_list(self):
        block = "1. Item 1\n3. Item 2"
        self.assertEqual(block_to_block_type(block), "paragraph")

    def test_normal_paragraph(self):
        block = "This is a normal paragraph."
        self.assertEqual(block_to_block_type(block), "paragraph")

    def test_empty_string(self):
        block = ""
        self.assertEqual(block_to_block_type(block), "paragraph")

    def test_multiple_lines(self):
        block = "# Heading\n## Subheading\n### Subsubheading"
        self.assertEqual(block_to_block_type(block), "heading")

    def test_code_block_multiple_lines(self):
        block = "```\ncode\nline 1\ncode\nline 2\n```"
        self.assertEqual(block_to_block_type(block), "code")


if __name__ == "__main__":
    unittest.main()
