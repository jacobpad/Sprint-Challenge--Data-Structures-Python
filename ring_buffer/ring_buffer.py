from dll import ListNode, DoublyLinkedList

class RingBuffer:
    def __init__(self, capacity):
        '''Because every class needs an "init"'''
        self.capacity = capacity # It's the capacity
        self.current_node = None # Gotta start somewhere
        self.storage = DoublyLinkedList() # Use a DLL to store them in


    def append(self, item):
        if len(self.storage) < self.capacity: # If there's room in the DLL
            self.storage.add_to_tail(item) # Insert the newest node at the end
        else:
            if self.current_node == None: # If cur is empty
                self.storage.head.value = item # Assign it
                self.current_node = self.storage.head.next # Update
            else:
                self.current_node.value = item # Assign it
                self.current_node = self.current_node.next # Update
                

    def get(self):        
        my_list = [] # Make an empty list for the return
        current_node = self.storage.head # Get a starting place at the head
        while current_node:
            my_list.append(current_node.value) # Append
            current_node = current_node.next # Move on
        return my_list
