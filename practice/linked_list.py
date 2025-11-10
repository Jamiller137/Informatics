class LinkNode:
    def __init__(self, value=None, next=None):
        self.next = next
        self.value = value

    def __str__(self):
        return str(self.value)

x = LinkNode(value=1, next=None)

raw = [1, 'a', 2, 'b', 3, 'c']

dummy_head = LinkNode()
head = LinkNode()
dummy_head.next = head
for i in raw:
    head.value = i
    head.next = LinkNode()
    head = head.next

def print_linked_list(curr: LinkNode):
    if curr.next == None:
        print("Done!")
        return None
    else:
        print(curr.value)
        print_linked_list(curr.next)

    
print_linked_list(dummy_head.next)


# Although this is not really how we would use a linked list.
# We would use queue or deque for double-ended.

from collections import deque

dq = deque(raw)
dq.append('4')
dq.appendleft('0')

print(dq)

# Note: Linked lists have worse cache performance than arrays.
#   So we should use lists for general-purpose random-access tasks
#   and we use deque for queue/stack behavior.


