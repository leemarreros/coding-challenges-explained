class Node:
    # We only need the location of the next 'Node'
    def __init__(self):
        self.next = None


def loop_size(node):
    # As stated, we'll make the rabbit jumps in two steps
    # while the turtle will go step by step (or node by node)
    turtle, rabbit = node.next, node.next.next

    # This while indicates that both are jumping without break
    # until the moment where turtle and rabbit are at the position.
    # In other words, when both 'nodes' are the same.
    while turtle != rabbit:
        turtle = turtle.next
        rabbit = rabbit.next.next

    # We keep the turtle's node as reference and we make the rabbit
    # jump again one more lap. This time, we need to keep count of the
    # steps taken to reach the same in the circular path
    count = 1
    rabbit = rabbit.next
    # We iterate until the rabbit finds the node's turtle
    # At that moment, will know the length of the loop
    while turtle != rabbit:
        count += 1
        rabbit = rabbit.next

    return count
