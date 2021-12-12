from __future__ import annotations

class Node:
     data : int
     next : Node  #or None

def is_equal(head1: Node, head2: Node)-> bool:
     '''checks if the linked lists starting with head1 is equal to the linked list starting with head2'''
     if head1 is None and head2 is None:
        return True
     elif head1 is None or head2 is None:
        return False
     else:
        return head1.data == head2.data and is_equal(head1.next, head2.next)
