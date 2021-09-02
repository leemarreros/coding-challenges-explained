def loop_size(node):
    counter = 1
    while node.next:
        node.counter = counter
        if not node.visited and node.next.visited:
            counter = node.counter - node.next.counter + 1
            break
        node.visited = True
        print(node, "next ", node.next)
        node = node.next
        counter += 1
    return counter


class Node:
    def __init__(self):
        self.next = None
        self.visited = False
        self.counter = 0

    def loop_size(node):
        dict = {}
        counter = 0
        dict[node] = 0
        while node.next:
            if node.next in dict:
                counter = dict[node] - dict[node.next] + 1
                return counter
            counter += 1
            dict[node.next] = counter
            node = node.next

    def __str__(self):
        return "visited {} for Node {}".format(self.visited, self.counter)
