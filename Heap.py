class Heap:
    """A class used to store a heap of TreeNode objects"""

    def __init__(self, nodes):
        self.nodes = nodes

    def __len__(self):
        return len(self.nodes)
    
    def __str__(self):
        """Returns a string representing each node in the heap, excluding child nodes"""
        string = ", ".join(f"{node.byte}:{node.frequency}" for node in self.nodes)
        return f"{{ {string} }}"

    def heapify(self):
        """This method sorts the array into min-heap order based on frequency in place"""
        for i in range((len(self) // 2) - 1, -1, -1):
            self.sink(i)

    def sink(self, i):
        """A helper method to maintain min-heap order"""
        small = i
        left = 2*i + 1
        right = 2*i + 2
        if (left < len(self) and self.nodes[left].frequency < self.nodes[small].frequency):
            small = left
        if (right < len(self) and self.nodes[right].frequency < self.nodes[small].frequency):
            small = right
        if (small != i):
            self.swap(i, small)
            self.sink(small)

    def swim(self, i):
        """A helper method to maintain min-heap order"""
        if (self.nodes[i].frequency < self.nodes[(i-1) // 2].frequency):
            self.swap(i, (i-1) // 2)
            self.swim((i-1) // 2)

    def swap(self, i, j):
        """A helper method for heap operations"""
        self.nodes[i], self.nodes[j] = self.nodes[j], self.nodes[i]

    def pop(self):
        """Removes the minimum TreeNode from the Heap and returns it"""
        minNode = self.nodes[0]
        self.swap(0, len(self)-1)
        self.nodes = self.nodes[:-1]
        self.sink(0)
        return minNode

    def push(self, newNode):
        """Adds the newNode to the Heap and updates the Heap to maintain min-heap order"""
        self.nodes.append(newNode)
        self.swim(len(self)-1)

    def is_min_heap(self):
        """This method checks whether or not the heap is sorted in min-heap order"""
        n = len(self.nodes)
        # Check each non-leaf node
        for i in range(n // 2 - 1, -1, -1):
            # Compare with left child
            left_child = 2 * i + 1
            if left_child < n and self.nodes[i] > self.nodes[left_child]:
                return False
            # Compare with right child
            right_child = 2 * i + 2
            if right_child < n and self.nodes[i] > self.nodes[right_child]:
                return False
        return True