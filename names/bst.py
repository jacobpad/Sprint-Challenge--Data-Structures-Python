class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        # Insert the given value into the tree
        # Left side
        if value < self.value:                  # If the value is on the left side is less than the root node
            if self.left is None:               # If it's empty, put it here
                self.left = BSTNode(value)      # Insert a node to this spot
            else:                               #
                self.left.insert(value)         # Recursive - calling itself

        elif value >= self.value:               # Right side
            if self.right is None:              # If there is no value to the right, insert it here by
                # assigning it to the right node.
                self.right = BSTNode(value)
            else:                               # If it doesn't go down that right side,
                self.right.insert(value)        # run it again.

    def contains(self, target):
        # Return True if the tree contains the value
        # False if it does not
        if self.value == target:                # If what we're looking for is the same as root
            return True

        if target < self.value:                 # If target is less than self.value
            if self.left is None:
                return False
            else:
                return self.left.contains(target)

        else:                                   # If target is greater than self.value
            if self.right is None:
                return False
            else:
                return self.right.contains(target)

    def get_max(self):
        # Return the maximum value found in the tree
        # If there's only one node
        # Only deal with the right side as smaller values always go left
        current = self.right                    # Set the right node as the current node
        value = self.value                      # Set self.value to value
        while current != None:                  # If there's a node to the right,
            value = current.value               # update value to the current node &
            # set the node to the right as the current node.
            current = current.right
        return value

    def for_each(self, fn):
        # Call the function `fn` on the value of each node
        fn(self.value)
        if self.left:                           # If something to the left exists,
            self.left.for_each(fn)              # call it on the function
        if self.right:                          # If something to the right exists,
            self.right.for_each(fn)             # call it on the function

    # in_order_print ---------------------------------------------------------
    # in_order_print ---------------------------------------------------------
    # in_order_print ---------------------------------------------------------
    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal

    def in_order_print(self, node):
        """
        # Print all the values in order from low to high
        # Hint:  Use a recursive, depth first traversal
        # What should we doif the current node is none?
        # Which direction should we move until we hit the end?
        # When should we switch the direction we're going?
        # If the current node is none, we know we've reached the end of a recursion.
        """

        if self is None:
            return
        # Check if we can move left
        if self.left is not None:
            self.left.in_order_print(self.left)
        # Visit the node by printing the value
        print(self.value)
        # Check if we can move right
        if self.right is not None:
            self.right.in_order_print(self.right)
