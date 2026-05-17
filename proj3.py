from __future__ import annotations
from dataclasses import dataclass, field
from operator import index


@dataclass(order=True, frozen=True)
class Node:
    freq: int
    char: str
    left: Node | None = None
    right: Node | None  = None

    def __str__(self):
        return f"Node: {self.char}, Freq: {self.freq}"

@dataclass(frozen=True)
class MinHeap:
    data: list[Node] = field(default_factory=list)

def heapify_up(heap: MinHeap, index: int) -> MinHeap:
    new_data = heap.data[:]
    while index > 0:
        parent = (index - 1) // 2

        if new_data[parent] <= new_data[index]:
            break

        new_data[index], new_data[parent] = (new_data[parent], new_data[index])
        index = parent
    return MinHeap(new_data)


def insert(heap: MinHeap, element: Node) -> MinHeap:
    new_data = heap.data[:] + [element]
    new_heap = MinHeap(new_data)
    return heapify_up(new_heap, len(new_data) - 1)


def heapify_down(heap: MinHeap, index: int) -> MinHeap:
    new_data = heap.data[:]
    while True:
        left = 2 * index + 1
        right = 2 * index + 2
        size = len(new_data)
        if left >= size:
            break
        smallest = left
        if right < size and new_data[right] < new_data[left]:
            smallest = right
        if new_data[smallest] < new_data[index]:
            new_data[index], new_data[smallest] = (new_data[smallest], new_data[index])
            index = smallest
        else:
            break
    return MinHeap(new_data)


def extract_min(heap: MinHeap) -> tuple[MinHeap, Node]:
    if len(heap.data) == 1:
        return MinHeap([]), heap.data[0]
    min_val = heap.data[0]
    last_node = heap.data[-1]
    new_heap = [last_node] + heap.data[1:-1]
    new_heap = heapify_down(MinHeap(new_heap), 0)
    return new_heap, min_val


        
def count_frequency(s: str)-> dict[str,int]:
    new_dict = {}
    for char in s:
        if char in new_dict:
            new_dict[char] +=1
        else:
            new_dict[char] = 1
    return new_dict



def create_priority_queue(frequency: dict[str, int]) -> MinHeap:
    new_heap = MinHeap([])
    for char, freq in frequency.items():
        new_heap = insert(new_heap, Node(freq, char))
    return new_heap



def build_tree(priority_queue: MinHeap) -> Node:
    while len(priority_queue.data) > 1:
        priority_queue, left = extract_min(priority_queue)
        priority_queue, right = extract_min(priority_queue)
        parent = Node(left.freq + right.freq,"",left,right)
    priority_queue = insert(priority_queue, parent)
    return priority_queue.data[0]



def generate_codes(node: Node | None, prefix="", code: dict | None =None)-> dict:
    if code is None:
        code = {}
    if node is None:
        return code

        # leaf node
    if node.left is None and node.right is None:
        code[node.char] = prefix

    generate_codes(node.left, prefix + "0", code)
    generate_codes(node.right, prefix + "1", code)

    return code


def encode(s: str, codes: dict)-> str:
    encoded = ""

    for char in s:
        encoded += codes[char]

    return encoded


def decode(encoded_string: str, root: Node):
    decoded = ""
    current = root

    for bit in encoded_string:

        if bit == "0":
            current = current.left
        else:
            current = current.right

        # reached a leaf
        if current.left is None and current.right is None:
            decoded += current.char
            current = root

    return decoded

def huffman_encoding(s:str):
    #Do Not Change this function
    frequency = count_frequency(s)
    pq = create_priority_queue(frequency)
    root = build_tree_from_queue(pq)
    codes = generate_codes(root)
    encoded_string = encode(s, codes)
    decoded_string = decode(encoded_string,root)
    return encoded_string, decoded_string, codes

