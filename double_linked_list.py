class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None  # Reference to the previous node

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:  # If the list is empty
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node  # Link the current tail to the new node
            new_node.prev = self.tail  # Link the new node back to the current tail
            self.tail = new_node  # Update the tail to the new node

    def insert(self, position, data):
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            if self.head:
                self.head.prev = new_node
            self.head = new_node
            if self.tail is None:  # If the list was empty, update the tail
                self.tail = new_node
        else:
            current = self.head
            current_position = 0
            while current and current_position < position:
                current_position += 1
                current = current.next
            if current is None:  # If inserting at the end
                self.append(data)
            else:
                previous = current.prev
                previous.next = new_node
                new_node.prev = previous
                new_node.next = current
                current.prev = new_node

    def delete(self, data):
        current = self.head
        while current:
            if current.data == data:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                return True
            current = current.next
        return False

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next

    def traversal(self):
        print("Doubly linked list elements:")
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

def menu():
    doubly_linked_list = DoublyLinkedList()
    while True:
        print("\nWelcome To Scotty's doubly_linked_list")
        print("\nChoose an option:")
        print("1. Traverse through linked list")
        print("2. Insert into linked list")
        print("3. Delete from linked list")
        print("4. Append to linked list")
        print("5. Exit")

        choice = input("Enter your decision (1-5): ")

        if choice == "1":
            doubly_linked_list.traversal()
        elif choice == "2":
            position = int(input("Enter the position to insert: "))
            data = input("Enter the data to insert: ")
            doubly_linked_list.insert(position, data)
        elif choice == "3":
            data = input("Enter the data to delete: ")
            if doubly_linked_list.delete(data):
                print(f"Deleted {data} from the linked list.")
            else:
                print(f"{data} not found in the linked list.")
        elif choice == "4":
            data = input("Enter the data to append: ")
            doubly_linked_list.append(data)
        elif choice == "5":
            print("Exiting the menu. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again (1-5).")

menu()
