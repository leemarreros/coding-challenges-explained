from node import Node


def loop_size(node):
    counter = 1

    # we keep iterating as long as there is a node (next node)
    # attached to the current node
    while node.next:
        node.counter = counter

        # Right at this point, where the current node
        # with its `visited` property set to False, and
        # the next node (node.next.visited) has its `visited` property
        # set to True, we'll know that we circled back to one of previous nodes
        if not node.visited and node.next.visited:
            # Since each node has a counter, a simple rest would give us
            # the distance between these two nodes, hence finding the loop's size
            return node.counter - node.next.counter + 1
        node.visited = True
        node = node.next
        counter += 1
