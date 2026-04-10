import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_no_value(self):

        node = LeafNode("b", None)
        
        with self.assertRaises(ValueError):
            node.to_html()
        
    def test_leaf_to_html_no_tag(self):

        node = LeafNode(None, "Value")
        
        self.assertEqual(node.to_html(), "Value")
        
    def test_leaf_repr(self):

        node = LeafNode(tag="h1", value="Header")
        answer = node.__repr__()

        self.assertTrue("h1" in answer and "Header" in answer and "children" not in answer)
        
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
        
    def test_leaf_to_html_a(self):
        node = LeafNode("a", "google", props={"href": "google.com"})
        self.assertEqual(node.to_html(), '<a href="google.com">google</a>')
        
    def test_leaf_to_html_img(self):
        node = LeafNode("img", "", props={"src": "image.jpg", "alt": "Cat pic"})
        self.assertEqual(node.to_html(), '<img src="image.jpg" alt="Cat pic" />')
        


if __name__ == "__main__":
    unittest.main()