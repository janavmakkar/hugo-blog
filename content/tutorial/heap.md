---
title: "Min Heap Implementation from Scratch | #DSA-450"
keywords:
  [
    "DSA",
    "python",
    "Min Heap",
    "Heap",
    "Tree",
    "Binary Tree",
    "Array",
    "Heap Sort",
  ]
categories: [DSA]
date: 2025-02-20T12:30:03+05:30
draft: false
defaultTheme: auto
tags: ["DSA", "python", "Heap", "Tree", "Binary Tree", "Array", "Heap Sort"]
showToc: true
comments: true
cover:
  image: posts/otter_basic_dsa.jpg
  alt: otter_basic_dsa
---

# Min-Heap

- Min-Heap is a complete binary tree where the parent node is always smaller than or equal to its child nodes.
- Since a Min Heap is a Complete Binary Tree, it is commonly represented using an array. In an array representation:

- - The root element is stored at Arr[0].
- - For any i-th node (at Arr[i]):
- - Parent Node → Arr[(i - 1) / 2]
- - Left Child → Arr[(2 * i) + 1]
- - Right Child → Arr[(2 * i) + 2]

## Operations on Min Heap

- `getMin()`: It returns the root element of Min Heap. Time Complexity of this operation is O(1).
- `extractMin()`: Removes the minimum element from MinHeap. Time Complexity of this Operation is O(Log n) as this operation needs to maintain the heap property (by calling heapify()) after removing root.
- `insert()`: Inserting a new key takes O(Log n) time. We add a new key at the end of the tree. If new key is larger than its parent, then we don’t need to do anything. Otherwise, we need to traverse up to fix the violated heap property.

```python
'''
            5                      13
          /   \                  /    \
        10     15              16      31
       /                      /  \     /  \
     30                     41    51  100  41

'''
A = [5, 10, 15, 30]
B = [13, 16, 31, 41, 51, 100, 41]
```

    <>:1: SyntaxWarning: invalid escape sequence '\ '
    <>:1: SyntaxWarning: invalid escape sequence '\ '
    C:\Users\ASUS\AppData\Local\Temp\ipykernel_33824\711618232.py:1: SyntaxWarning: invalid escape sequence '\ '
      '''

```python
# Implementation of Min Heap in Python

class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, k): # O(log_n)
        self.heap.append(k)
        i = len(self.heap) -1

        while self.heap[i] < self.heap[(i-1)//2] and i > 0:
            self.heap[i], self.heap[(i-1)//2] = self.heap[(i-1)//2], self.heap[i]
            i = (i-1)//2

    def delete(self, val):
        i=-1
        for j in range(len(self.heap)):
            if self.heap[j] == val:
                i=j
                break

        if i==-1:
            return -1

        self.heap[i] = self.heap[-1]
        self.heap.pop()

        while True:
            small = i
            left = 2*i+1
            right = 2*i+2

            if left<len(self.heap) and self.heap[left]<self.heap[small]:
                small = left

            if right<len(self.heap) and self.heap[right]<self.heap[small]:
                small = right

            if small != i:
                self.heap[i], self.heap[small] = self.heap[small], self.heap[i]
                i = small

            else:
                break



    def getMin(self):
        return self.heap[0] if self.heap else None


    """Heapify function to maintain the heap property."""
    def minHeapify(self,i,n):
        left = 2 * i + 1
        right = 2 * i + 2
        smallest = i

        if left < n and self.heap[smallest] > self.heap[left]:
            smallest = left
        if right < n and self.heap[smallest] > self.heap[right]:
            smallest = right
        if smallest!= i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.minHeapify(smallest, n)

    def printHeap(self):
        print("Min Heap:", self.heap)

    def search(self, k):
        for j in self.heap:
            if j == k:
                return True
        return False

if __name__ == "__main__":
    h = MinHeap()
    values = [10, 7, 11, 5, 4, 13]
    for value in values:
        h.insert(value)
    h.printHeap()

    h.delete(7)
    print("Heap after deleting 7:", h.heap)

    print("Searching for 10 in heap:", "Found" if h.search(10) else "Not Found")
    print("Minimum element in heap:", h.getMin())
```

    Min Heap: [4, 5, 11, 10, 7, 13]
    Heap after deleting 7: [4, 5, 11, 10, 13]
    Searching for 10 in heap: Found
    Minimum element in heap: 4
