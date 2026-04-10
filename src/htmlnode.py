
class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
        
    def to_html(self):
        raise NotImplemented
    
    def text_node_to_html_node(text_node):
        pass
        
    def props_to_html(self):
        if self.props is None or len(self.props) == 0:
            return ""
        prop_string = ""
        for key in self.props:
            prop_string += f' {key}="{self.props[key]}"'
        return prop_string
    
    def __repr__(self):
        return f"tag = {self.tag}, value = {self.value}, children = {self.children}, props = {self.props}"