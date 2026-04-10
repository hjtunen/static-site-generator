from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, props=props)
        
    def to_html(self):
        if self.value is None:
            raise ValueError("Leaf nodes must have a value")
        if self.tag is None:
            return self.value
        if self.tag == "a":
            return f"<a{self.props_to_html()}>{self.value}</a>"
        if self.tag == "img":
            return f"<img{self.props_to_html()} />"
        
        return f"<{self.tag}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"tag = {self.tag}, value = {self.value}, props = {self.props}"