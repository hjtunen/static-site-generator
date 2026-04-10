from textnode import TextNode
from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode

def main():
    text_node = TextNode("Text stuff", "text")
    print(text_node)
    
    html_node = HTMLNode(tag="h1", value="Header")
    print(html_node)
    print(html_node.props_to_html())
    
    child_node = LeafNode("span", "child")
    parent_node = ParentNode("div", [child_node])
    print(parent_node.to_html())
    
    grandchild_node = LeafNode("b", "grandchild")
    grandchild_node2 = LeafNode("p", "grandchild2")
    child_node = ParentNode("span", [grandchild_node, grandchild_node2])
    parent_node = ParentNode("div", [child_node])
    print(parent_node.to_html())
 
if __name__ == "__main__":   
    main()