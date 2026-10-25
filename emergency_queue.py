class Patient:
    def __init__(self, name, urgency):
        if type(urgency) is not int or not 1 <= urgency <= 10:
            raise ValueError("Urgency must be a whole number from 1 to 10.")
        self.name = name
        self.urgency = urgency


class MinHeap:
    def __init__(self):
        self.data = []

    def heapify_up(self, index):
        while index > 0:
            parent = (index - 1) // 2
            if self.data[index].urgency >= self.data[parent].urgency:
                break
            self.data[index], self.data[parent] = self.data[parent], self.data[index]
            index = parent

    def heapify_down(self, index):
        size = len(self.data)
        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            smallest = index

            if left < size and self.data[left].urgency < self.data[smallest].urgency:
                smallest = left
            if right < size and self.data[right].urgency < self.data[smallest].urgency:
                smallest = right
            if smallest == index:
                break

            self.data[index], self.data[smallest] = self.data[smallest], self.data[index]
            index = smallest

    def insert(self, patient):
        self.data.append(patient)
        self.heapify_up(len(self.data) - 1)

    def print_heap(self):
        print("Current Queue:")
        for patient in self.data:
            print(f"- {patient.name} ({patient.urgency})")

    def peek(self):
        if not self.data:
            return None
        return self.data[0]

    def remove_min(self):
        if not self.data:
            return None
        first = self.data[0]
        last = self.data.pop()
        if self.data:
            self.data[0] = last
            self.heapify_down(0)
        return first


if __name__ == "__main__":
    heap = MinHeap()
    heap.insert(Patient("Jordan", 3))
    heap.insert(Patient("Taylor", 1))
    heap.insert(Patient("Avery", 5))
    heap.print_heap()
    next_up = heap.peek()
    print("Next patient:", next_up.name, next_up.urgency)
    served = heap.remove_min()
    print("Served:", served.name)
    heap.print_heap()

    # Edge cases and more checks
    assert heap.remove_min().name == "Jordan"
    assert heap.remove_min().name == "Avery"
    assert heap.remove_min() is None
    assert heap.peek() is None
    for name, urgency in [("Riley", 8), ("Sam", 2), ("Lee", 4), ("Alex", 1)]:
        heap.insert(Patient(name, urgency))
    assert [heap.remove_min().urgency for _ in range(4)] == [1, 2, 4, 8]
    try:
        Patient("Invalid", 11)
        raise AssertionError("An invalid urgency should raise ValueError")
    except ValueError:
        pass
    print("All heap tests passed.")
