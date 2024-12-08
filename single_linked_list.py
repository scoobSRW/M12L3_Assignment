class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def insert(self, position, data):
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            if self.tail is None:  # If the list was empty, update the tail
                self.tail = new_node
        else:
            current = self.head
            current_position = 0
            previous = None
            while current is not None and current_position < position:
                previous = current
                current = current.next
                current_position += 1
            if previous:
                previous.next = new_node
            new_node.next = current
            if current is None:  # If inserted at the end, update the tail
                self.tail = new_node

    def delete(self, data):
        current = self.head
        prev = None
        while current:
            if current.data == data:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                if current.next is None:
                    self.tail = prev
                return True
            prev = current
            current = current.next
        return False

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next

    def traversal(self):
        print("Linked list elements:")
        for data in self:
            print(data, end=" -> ")
        print("None")

def menu():
    linked_list = LinkedList()
    while True:
        print("\nWelcome To Scotty's single_linked_list")
        print("\nChoose an option:")
        print("1. Traverse through linked list")
        print("2. Insert into linked list")
        print("3. Delete from linked list")
        print("4. Append to linked list")
        print("5. Exit")

        choice = input("Enter your decision (1-5): ")

        if choice == "1":
            linked_list.traversal()
        elif choice == "2":
            position = int(input("Enter the position to insert: "))
            data = input("Enter the data to insert: ")
            linked_list.insert(position, data)
        elif choice == "3":
            data = input("Enter the data to delete: ")
            if linked_list.delete(data):
                print(f"Deleted {data} from the linked list.")
            else:
                print(f"{data} not found in the linked list.")
        elif choice == "4":
            data = input("Enter the data to append: ")
            linked_list.append(data)
        elif choice == "5":
            print("Exiting the menu. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again (1-5).")

menu()
