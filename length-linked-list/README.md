# Get the length of linked list in O(n) and zero memory or how the turtle and the rabbit end up at the same place

Given a linked list, you will receive the beginning node of the list. This list will always contain a tail and a loop. The goal of **this challenge is to determine the length of the loop**. For example, in the following drawing the tail's size is 2 (A and B) and the loop size is 6 (1 to 6).

`````python
"""
A
  \  tail
    B       2  --   3
      \  /            \
        1      loop     4
          \           /
            6  --   5
"""
`````



The function that will find the length of the loop is called `loop_size(node)`and receives a `Node` as argument. This particular `Node` is the beginning of the linked list. Review the following examples:

`````python
node1 = Node()
node2 = Node()
node3 = Node()
node4 = Node()
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2
loop_size(node1)
# 3

nodes = [Node() for _ in xrange(50)]
for node, next_node in zip(nodes, nodes[1:]):
    node.next = next_node
nodes[59].next = nodes[21]
loop_size(nodes[0])
# 39

`````

We'll take **three** approaches for this challenge. 

1. The first solution will define a particular `Node` (of linked list) that will help us to keep wether that `Node` has been visited or not. In the third solution, the only allowed property for `Node` would be `.next`, solution that will lead us to have zero memory foot print.
2. The second one will use of a dictionary, hence the use of memory, for keeping track of the nodes that have been visited.
3. We'll model the solution using a turtle and a rabbit and see how the turtle will end up at the same position (Node) as the rabbit, and, by doind that, we'll count the steps (Nodes) the rabbit pass to reach the turtle



#### First approach

We will define a class `Node`. For this time, `Node` will have several properties that will help us to achieve a solution. Let's take a look at a implementation of Node:

`````python
class Node:
    def __init__(self):
        self.next = None
        self.visited = False
        self.counter = 0
`````



These three properties (next, visitied and counter) will help us to find the length of a linked list.

* `.next` - stores the address of the next Class
* `.visited` - will tell us wether a `Node`  has been visited or not. 
* `.counter` - will assign a counter to each `Node` beginning at 0

The key in this solution is to find **two linked nodes** in which one `Node` has the property `.visited` set to `True` and the other `Node` has `False` for the same property. At that point we'll know that we already circled back to one of the `Nodes`. Remember that the `Nodes` shape a circular path as the example above. At moment, as you go through the `Nodes`, you will end up at the same place. Let's see the implementation:

`````python
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
`````



#### Second approach

For this approach, we'll get rid off of the `.visited` property of `Node`. Instead of using a flag for finding out wether a `Node` has been counted or not, we'll keep the `Node`'s address and its position within the linked list in dictionary. Once we find a `Node`'s address that is included in the dictionary, we conclude that the loop has found its ending `Node`.  Let's see how the implementation looks like:

`````python
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
`````



##### Third approach (*most interesting)

This final and definitive approach really amazed me once I found about it. Specially because I was able to recreate in my mind a well-known story between a turtle a rabbit. The solution goes like this:

We know already that there is a circular path (loop). No matter how fast you go. Ultimately, you will end up at the same place where you started. 

Let's pretend that in this path there is a rabbit and a turtle racing. For the sake of the argument, let's say that the rabbit goes by two steps at each time, and the turtles moves by just one step at each time. If both animals are racing, eventually, the rabbit will catch the turtle. Why? Because they are running in circles.

Once we know that both turtle and rabbit are at the same position (`Node`), we'll just let the rabbit go for one more lap. The turtle will keep its position (`Node`) as reference and wait until the rabbit pass again.We'll count the steps the rabbit takes to go around the path. By doing that, we'll know that the steps taken by the rabbit in one round are the same as the loop's size. Let's see the implementation:

`````python
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
`````



Also, notice that in this solution, there was no need to use a form of memory. It's solved in linear time as well

