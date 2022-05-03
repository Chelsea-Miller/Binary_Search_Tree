class Binary_Search_Tree:
    def __init__(self, value):
        self.l_child = None
        self.r_child = None
        self.value = value

    def add_element(self, value):

        # If the value is already in the tree, return without adding it
        if value == self.value:
            return

        if value < self.value:
            if self.l_child is not None:
                self.l_child.add_element(value)
            else:
                self.l_child = Binary_Search_Tree(value)
        else:
            if self.r_child is not None:
                self.r_child.add_element(value)
            else:
                self.r_child = Binary_Search_Tree(value)

    def largest_element(self, parent):
        if self.r_child is not None:
            parent = self
            return self.r_child.largest_element(parent)
        else:
            return self, parent, self.value

    def _delete_leaf(self, parent, value):
        if parent.value < value:
            parent.r_child = None
        else:
            parent.l_child = None

    def delete_element(self, value):
        # Parent Node
        parent = None

        # Current Node
        curr = self

        # Search the tree for value and save its parent node
        while curr is not None and curr.value != value:
            parent = curr
            if value < self.value:
                curr = self.l_child
            elif value > self.value:
                curr = self.r_child

        # If value was found, delete it
        if curr is not None:

            # if curr is a leaf
            if curr.l_child is None and curr.r_child is None:
                curr._delete_leaf(parent, value)

            # if curr has children
            else:
                # Set curr value to the largest value in the right subtree (a leaf). Delete that leaf.
                largest, parent_of_largest, new_value = curr.largest_element(None)
                largest._delete_leaf(parent_of_largest, new_value)
                curr.value = new_value

    def elements_inorder(self):
        elements = []
        if self.l_child is not None:
            elements += self.l_child.elements_inorder()

        elements.append(self.value)

        if self.r_child is not None:
            elements += self.r_child.elements_inorder()

        return elements

    def elements_inorder_print(self):
        if self.l_child is not None:
            self.l_child.elements_inorder_print()

        print(self.value, end=' ')

        if self.r_child is not None:
            self.r_child.elements_inorder_print()


if __name__ == '__main__':
    bst = Binary_Search_Tree(7)
    bst.add_element(5)
    bst.add_element(12)
    bst.add_element(6)
    bst.add_element(1)
    bst.add_element(14)
    elms = bst.elements_inorder()
    print(elms)
    bst.delete_element(5)
    elms = bst.elements_inorder()
    print(elms)
    # bst.elements_inorder_print()
