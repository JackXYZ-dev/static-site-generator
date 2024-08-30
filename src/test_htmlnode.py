import unittest
from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_none(self):
        node = HTMLNode("h1", "This is a test", None, None)
        result = node.props_to_html()
        self.assertEqual(result, "")
    
    def test_props_to_html_empty(self):
        node = HTMLNode("h1", "This is a test", None, {})
        result = node.props_to_html()
        self.assertEqual(result, "")

    def test_props_to_html_single_prop(self):
        node = HTMLNode("h1", "This is a test", None, {"class": "header"})
        result = node.props_to_html()
        self.assertEqual(result, ' class="header"')

    def test_props_to_html_multiple_props(self):
        node = HTMLNode("h1", "This is a test", None, {"class": "header", "id": "main-title"})
        result = node.props_to_html()
        self.assertEqual(result, ' class="header" id="main-title"')

    def test_to_html_no_children(self):
        node = LeafNode("p", "Test")
        self.assertEqual(node.to_html(), "<p>Test</p>")

    def test_to_html_no_tag(self):
        node = LeafNode(None, "Test!")
        self.assertEqual(node.to_html(), "Test!")

if __name__ == "__main__":
    unittest.main()