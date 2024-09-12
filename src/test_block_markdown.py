import unittest
import re
from block_markdown import markdown_to_blocks


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


if __name__ == "__main__":
    unittest.main()
