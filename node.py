class Node:

    # constructor
    def __init__(self, parent = None):
        self.item = ""
        self.count = 0

        self.children = []
        self.parent = parent

    def append(self, items, node_links):
        if not items:
            return

        next_item = items.pop(0)

        # assign dummy node
        dummy_node = None
        for child in self.children:
            if child.item == next_item:
                dummy_node = child

        if not dummy_node:
            dummy_node = Node(parent=self)
            dummy_node.item = next_item

            self.children.append(dummy_node)
            node_links[next_item].append(dummy_node)

        dummy_node.count += 1
        dummy_node.append(items, node_links)

    def is_single_path(self):
        if not self.children:
            return True
        elif len(self.children) > 1:
            return False
        else:
            return self.children[0].is_single_path()

    def pattern(self):
        parent_list = []
        current = self.parent

        while current.item:
            parent_list.append(current.item)
            current = current.parent

        if parent_list:
           return {tuple(reversed(parent_list)): self.count}
        else:
            return {}