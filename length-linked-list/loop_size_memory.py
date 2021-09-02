class Node:
    # See that we only need two properties here: next and counter
    def __init__(self):
        self.next = None
        self.counter = 0


def loop_size(node):
    # we'll help us to tack the address and position of each
    # 'node' within the linked list.
    dict_ = {}
    counter = 0
    dict_[node] = 0
    while node.next:

        # For this particular solution, we are keeping the address
        # of each 'node' within 'dict_'. At any given point where we find
        # a 'node' whose address is already in 'dict_', we conclude that
        # we reach a 'node' that has been visited already.
        if node.next in dict_:
            return dict_[node] - dict_[node.next] + 1
        counter += 1
        dict_[node.next] = counter
        node = node.next
