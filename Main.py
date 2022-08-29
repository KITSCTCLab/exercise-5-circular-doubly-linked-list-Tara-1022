class Node:
    def __init__(self, data=None):
        self.data = data
        self.previous = self
        self.next = self


class DoublyCircularLinkedList:
    def __init__(self):
        self.head = None
        self.count = 0
        self.tail = None

    def add_at_tail(self, data) -> bool:
        new = Node(data)
        if self.count > 0:
            new.previous = self.tail
            self.tail.next = new
            self.head.previous = new
            new.next = self.head
        else:
            self.head = new
        self.tail = new
        self.count += 1
        return True

    def add_at_head(self, data) -> bool:
        new = Node(data)
        if self.count > 0:
            new.next = self.head
            new.previous = self.tail
            self.head.previous = new
            self.tail.next = new
        else:
            self.tail = new
        self.head = new
        self.count += 1
        return True
        
        
    def add_at_index(self, index, data) -> bool:
        if index < 0 or index >= self.count:
            return False
        if index == 0:
            return self.add_at_head(data)
        if index == self.count:
            return self.add_at_tail(data)
        
        new = Node(data)
        curr_node = self.head
        for ind in range(index):
            curr_node = curr_node.next
        
        new.previous = curr_node.previous
        new.next = curr_node
        curr_node.previous.next = new
        curr_node.previous = new
        self.count += 1
        return True
        

    def get(self, index) -> int:
        if index < 0 or index >= self.count:
            return -1
        curr_node = self.head
        for ind in range(index):
            curr_node = curr_node.next
        return curr_node.data
        

    def delete_at_index(self, index) -> bool:
        if index < 0 or index >= self.count:
            return False
        if index == 0:
            temp = self.head
            temp.next.previous = self.tail
            self.tail.next = temp.next
            self.head = temp.next
            self.count -= 1
            return True
        if index == self.count - 1:
            temp = self.tail
            self.head.previous = temp.previous
            temp.previous.next = self.head
            self.tail = temp.previous
            self.count -= 1
            return True
        
        curr_node = self.head
        for ind in range(index):
            curr_node = curr_node.next
        curr_node.previous.next = curr_node.next
        curr_node.next.previous = curr_node.previous
        self.count -= 1
        return True
        

    def get_previous_next(self, index) -> list:
        if index < 0 or index >= self.count:
            return -1
        curr_node = self.head
        for ind in range(index):
            curr_node = curr_node.next
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
