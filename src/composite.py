from abc import ABC, abstractmethod

class Node(ABC):
    @abstractmethod
    def render(self) -> str:
        pass

class Text(Node):
    def __init__(self, content: str):
        self.content = content

    def render(self) -> str:
        return self.content

class Group(Node):
    def __init__(self):
        self.children = []

    def add(self, node: Node):
        self.children.append(node)

    def render(self) -> str:
        return ''.join(child.render() for child in self.children)
    
class Document(Group):
    def __init__(self, title: str):
        super().__init__()
        self.title = title

    def render(self) -> str:
        return f"<h1>{self.title}</h1>" + super().render()