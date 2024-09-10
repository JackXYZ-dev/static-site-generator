import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

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

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )


if __name__ == "__main__":
    unittest.main()