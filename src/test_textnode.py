import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
        
    def test_eq_type(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
        
    def test_eq_link(self):
        node = TextNode("This is a text node", "bold", None)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
        
    def test_neq_text(self):
        node = TextNode("This is not text node", "text")
        node2 = TextNode("This is a text node", "text")
        self.assertNotEqual(node, node2)

    def test_neq_type(self):
        node = TextNode("This is a text node", "text")
        node2 = TextNode("This is a text node", "bold")
        self.assertNotEqual(node, node2)
        
    def test_neq_link(self):
        node = TextNode("This is a text node", "text", "null.fm")
        node2 = TextNode("This is a text node", "text")
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()