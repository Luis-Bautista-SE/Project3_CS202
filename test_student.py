import unittest
from proj3 import *

class TestRegionFunctions(unittest.TestCase):
    def test_heapify_up(self):
        heap = MinHeap([
            Node(5, "a"),
            Node(7, "b"),
            Node(2, "c")
        ])
        result = heapify_up(heap, 2)
        self.assertEqual(result.data[0].freq, 2)

    def test_insert(self):
        heap = MinHeap([
            Node(3, "a"),
            Node(5, "b")
        ])
        result = insert(heap, Node(1, "c"))
        self.assertEqual(result.data[0].freq, 1)
        self.assertEqual([], [])
    def test_heapify_down(self):
        heap = MinHeap([
            Node(10, "a"),
            Node(2, "b"),
            Node(3, "c")
        ])
        result = heapify_down(heap, 0)
        self.assertEqual(result.data[0].freq, 2)

    def test_extract_min(self):
        heap = MinHeap([
            Node(1, "a"),
            Node(3, "b"),
            Node(5, "c")
        ])
        new_heap, min_node = extract_min(heap)
        self.assertEqual(min_node.freq, 1)
        self.assertEqual(len(new_heap.data), 2)

    def test_count_frequency(self):
        result = count_frequency("banana")
        expected = {
            "b": 1,
            "a": 3,
            "n": 2
        }
        self.assertEqual(result, expected)

    def test_priority_queue(self):
        freq = {
            "a": 5,
            "b": 2,
            "c": 1
        }
        heap = create_priority_queue(freq)
        self.assertEqual(len(heap.data), 3)
        self.assertEqual(heap.data[0].freq, 1)

    def test_build_tree(self):
        freq = {
            "a": 5,
            "b": 2,
            "c": 1
        }
        heap = create_priority_queue(freq)
        root = build_tree_from_queue(heap)
        self.assertEqual(root.freq, 8)

    def test_generate_codes(self):
        freq = {
            "a": 5,
            "b": 2,
            "c": 1
        }
        heap = create_priority_queue(freq)
        root = build_tree_from_queue(heap)
        codes = generate_codes(root)
        self.assertIn("a", codes)
        self.assertIn("b", codes)
        self.assertIn("c", codes)

    def test_encode(self):
        codes = {
            "a": "0",
            "b": "10",
            "c": "11"
        }
        result = encode("abc", codes)
        self.assertEqual(result, "01011")

    def test_decode(self):
        freq = {
            "a": 5,
            "b": 2,
            "c": 1
        }

        heap = create_priority_queue(freq)
        root = build_tree_from_queue(heap)
        codes = generate_codes(root)
        encoded = encode("abc", codes)
        decoded = decode(encoded, root)

        self.assertEqual(decoded, "abc")


if __name__ == '__main__':
    unittest.main()
