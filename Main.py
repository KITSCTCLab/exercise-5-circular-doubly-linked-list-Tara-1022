class Node:
    def __init__(self, data=None):
        self.data = data
        self.previous = None
        self.next = None


class DoublyCircularLinkedList:
    def __init__(self):
        self.head = None
        self.count = 0
        self.tail = None

    def add_at_tail(self, data) -> bool:
        new = Node(data)
        if self.count == 0:
            self.tail = new
            self.head = new
        else:
            self.tail.next = new
            new.previous = self.tail
            self.tail = new
        self.count += 1
        return True

    def add_at_head(self, data) -> bool:
        new = Node(data)
        if self.count == 0:
            self.tail = new
            self.head = new
        else:
            new.next = self.head
            self.head.previous = new
            self.head = new
        self.count += 1
        return True

    def add_at_index(self, index, data) -> bool:
        if not 0 <= index <= (self.count - 1):
            return False
        
        curr_node = self.head
        for ind in range(index):
            curr_node = self.head.next
            
        new = Node(data)
        new.next = curr_node
        new.previous = curr_node.previous
        curr_node.previous.next = new
        curr_node.previous = new
        
        if index == 0:
            self.head = new
        if index == self.count - 1:
            self.tail = new
        self.count += 1
        return True

    def get(self, index) -> int:
        if not 0 <= index <= (self.count - 1):
            return -1
        curr_node = self.head
        for ind in range(index):
            curr_node = self.head.next
        return curr_node.data

    def delete_at_index(self, index) -> bool:
        if not 0 <= index <= (self.count - 1):
            return False
        
        curr_node = self.head
        for ind in range(index):
            curr_node = self.head.next
            
        curr_node.next.previous = curr_node
        curr_node.previous.next = curr_node
        self.count -= 1
        return True

    def get_previous_next(self, index) -> list:
        if not 0 <= index <= (self.count - 2):
            return [-1]
        curr_node = self.head
        for ind in range(index):
            curr_node = self.head.next
        return [curr_node.previous.data, curr_node.next.data]


# Do not chantge the following code
operations = []
for specific_operation in input().split(','):
    operations.append(specific_operation.strip())
input_data = input()
data = []
iteration_count = 0

for item in input_data.split(', '):
    inner_list = []
    if item.isnumeric():
        data.append(int(item))
    elif item.startswith('['):
        item = item[1:-1]
        for letter in item.split(','):
            if letter.isnumeric():
                inner_list.append(int(letter))
        data.append(inner_list)

obj = DoublyCircularLinkedList()
result = []
for i in range(len(operations)):
    if operations[i] == "add_at_head":
        result.append(obj.add_at_head(data[i]))
    elif operations[i] == "add_at_tail":
        result.append(obj.add_at_tail(data[i]))
    elif operations[i] == "add_at_index":
        result.append(obj.add_at_index(int(data[i][0]), data[i][1]))
    elif operations[i] == "get":
        result.append(obj.get(data[i]))
    elif operations[i] == "get_previous_next":
        result.append(obj.get_previous_next(data[i]))
    elif operations[i] == 'delete_at_index':
        result.append(obj.delete_at_index(data[i]))

print(result)
