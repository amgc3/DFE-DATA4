class Node:
     data : int
     next : None


def is_equal(head1, head2):
    if head1 is None and head2 is None:
        return True
    elif head1 is None or head2 is None:
        return False
    else:
        if head1.data == head2.data:
            return is_equal(head1.next, head2.next)
        else:
            return False
