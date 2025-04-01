from __future__ import annotations

class Node:
    def __init__(self, obj, parent, height: int,):
        self.obj = obj
        self.parent = parent
        self.height = height + 1
        self.children = []
        if isinstance(obj, dict):
            for name, value in self.obj.items():
                self.addChild([name, value])
        elif isinstance(obj, list):
            for element in obj:
                self.addChild(element)

    def __repr__(self):
        return f"{"   |" * self.height}{self.obj}"

    def addChild(self, child_obj):
        child_node = Node(child_obj, self, self.height)
        self.children.append(child_node)