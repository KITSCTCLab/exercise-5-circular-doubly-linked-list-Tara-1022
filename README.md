# Problem

Design your implementation of the Circular Doubly Linked List.</b>
A node in a circular doubly linked list should have three attributes: data, previous and next. data is the value of the current node, previous is a pointer/reference to the previous node and next is a pointer/reference to the next node.</br>
Assume all nodes in the linked list are 0-indexed.

Implement the DoublyCircularLinkedList class:

> **get(index)** : Get the value of the indexth node in the linked list. If the index is invalid, return -1.</br>
**add_at_head(data)** : Add a node of value data before the first element of the linked list. After the insertion, the new node will be the first node of the linked list. The function returns True after adding data at head.</br>
**add_at_tail(data)** : Append a node of value data as the last element of the linked list. The function returns True after append operation.</br>
**add_at_index(index, data)** : Add a node of value data before the indexth node in the linked list. If index equals the length of the linked list, the node will be appended to the end of the linked list. If index is greater than the length, the node will not be inserted. If the operation is success, the function returns True, otherwise it returns False.</br>
**delete_at_index(index)** : Delete the indexth node in the linked list, if the index is valid. If the operation is success, the function returns True, otherwise it returns False.</br>
**get_previous_next(index)** : If the index is valid, it returns a list of previous data and next data. If the index is valid it returns [-1].

# Constraints
Data should be integer value.

## Sample Input - 1
```
add_at_head, add_at_tail, add_at_index, get, delete_at_index, get, get_previous_next
10, 3, [1,2], 1, 1, 1, 1
```
## Sample Output - 1
```
[True, True, True, 2, True, 3, [10, 10]]
```
## Sample Input - 2
```
add_at_head, add_at_tail, add_at_index, add_at_index, add_at_index, add_at_index, get, get, get, get, get, get
5, 10, [1,6], [2,7], [3,8], [4,9], 0, 1, 2, 3, 4, 5
```
## Sample Output - 1
```
[True, True, True, True, True, True, 5, 6, 7, 8, 9, 10]
```
