def sum_nums(num1: int, num2: int) -> None:
    """Example of data types: int, none"""
    print(num1 + num2)


sum_nums(5, 1)


def is_bigger(num1: float, num2: float) -> bool:
    """Example of bolean and float"""
    return num1 > num2


print(is_bigger(1.3, 1.9))


def process_string_tuple_bytes(input_string, char_tuple):
    """Example of a string, tuple, byte"""
    # Step 1: Convert the string to bytes using UTF-8 encoding
    encoded_string = input_string.encode('utf-8')
    print("Encoded String (bytes):", encoded_string)

    # Step 2: Add each character from the tuple to the string (as characters)
    for char in char_tuple:
        input_string += char

    # Step 3: Decode the encoded bytes back to a string (from bytes to string)
    decoded_string = encoded_string.decode('utf-8')
    print("Decoded String:", decoded_string)

    # Step 4: Combine the decoded string with the added characters and return
    final_string = decoded_string + input_string
    return final_string


# Example usage:
EXAMPLE_STRING = "Hello"
CHAR_TUPLE = (' ', 'W', 'o', 'r', 'l', 'd')

RESULT = process_string_tuple_bytes(EXAMPLE_STRING, CHAR_TUPLE)
print("Final Result:", RESULT)


# Node class for Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked List class


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node  # type: ignore

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


def demonstrate_data_structures():
    """Function to demonstrate the usage of lists, linked lists, sets,
    and dictionaries."""
    # List: A simple list of integers
    my_list = [10, 20, 30, 40, 50]
    list_sum = sum(my_list)  # Sum of all elements in the list
    print("Sum of list elements:", list_sum)

    # Linked List: Create a linked list and add some values
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    print("Linked List values:")
    linked_list.display()

    # Set: A set of unique items
    my_set = {1, 2, 3, 4, 5}
    print("Original Set:", my_set)
    another_set = {4, 5, 6, 7}
    union_set = my_set.union(another_set)  # Perform union with another set
    print("Union of sets:", union_set)

    # Dictionary: A dictionary with key-value pairs
    my_dict = {"name": "Alice", "age": 30, "city": "New York"}
    print("Value for key 'name':", my_dict["name"])
    print("Value for key 'age':", my_dict["age"])


# Call the function to demonstrate
demonstrate_data_structures()
