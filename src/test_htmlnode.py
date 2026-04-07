import unittest

from textnode import TextNode, TextType
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        node = HTMLNode(props=props)
        answer = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), answer)
        
    def test_props_to_html_empty(self):

        node = HTMLNode()
        answer = ""
        self.assertEqual(node.props_to_html(), answer)
        
    def test_repr(self):

        html_node = HTMLNode(tag="h1", value="Header")
        answer = html_node.__repr__()

        self.assertTrue("h1" in answer and "Header" in answer)
        


if __name__ == "__main__":
    unittest.main()