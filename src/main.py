from textnode import TextNode
from htmlnode import HTMLNode

def main():
    text_node = TextNode("Text stuff", "text")
    print(text_node)
    
    html_node = HTMLNode(tag="h1", value="Header")
    print(html_node)
    print(html_node.props_to_html())
 
if __name__ == "__main__":   
    main()