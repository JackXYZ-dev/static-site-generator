class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
        
    def props_to_html(self):
        if self.props == None:
            return None
        if self.props == {}:
            return ""
        prop_string = ""
        for key, value in self.props.items():
            prop_string  += f''' {key}="{value}"'''
        return prop_string[1:]

    def __repr__(self):
        print(f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})")
