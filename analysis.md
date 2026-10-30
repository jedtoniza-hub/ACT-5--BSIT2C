# Analysis

A linked stack adds new nodes at the head because both push and pop can be done in O(1) time. If we used the tail of a singly linked list, removing the last node would take longer because we would need to walk the whole list to find the node before it. An array queue should be circular so its indexes can return to the start of the array. This allows it to reuse spaces left by removed items without shifting the other items.
