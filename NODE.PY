#th linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

# Contoh penggunaan Linked List
linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.display()

#th map
# Membuat Map
map_data = {
    "nama": "John Doe",
    "umur": 25,
    "pekerjaan": "Engineer"
}

# Mengakses nilai dalam Map
print(map_data["nama"])
print(map_data["umur"])
print(map_data["pekerjaan"])

# Menambahkan entri baru ke dalam Map
map_data["alamat"] = "Jalan Raya No. 123"
print(map_data)

# Menghapus entri dalam Map
del map_data["pekerjaan"]
print(map_data)

#cth tree
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def traverse(self):
        print(self.data)
        for child in self.children:
            child.traverse()

# Contoh penggunaan Tree
root = TreeNode("A")
node1 = TreeNode("B")
node2 = TreeNode("C")
node3 = TreeNode("D")
node4 = TreeNode("E")
root.add_child(node1)
node1.add_child(node2)
node1.add_child(node3)
node2.add_child(node4)

root.traverse()
