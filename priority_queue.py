class PriorityQueue:
  def __init__(self):
    self.heap = []

  def push(self, item, priority):
    entry = (priority, item)
    self.heap.append(entry)
    self._sift_up(len(self.heap) - 1)

  def pop(self):
    if len(self.heap) > 1:
      self._swap(0, len(self.heap) - 1)
      _, item = self.heap.pop()
      self._sift_down(0)
      return item
    elif len(self.heap) == 1:
      _, item = self.heap.pop()
      return item
    else:
      return None

  def _sift_up(self, index):
    while index > 0:
      parent_index = (index - 1) // 2
      if self.heap[parent_index][0] < self.heap[index][0]:  # 우선순위가 높은 것이 위로 올라오도록
        self._swap(parent_index, index)
        index = parent_index
      else:
        break

  def _sift_down(self, index):
    while True:
      left_child_index = 2 * index + 1
      right_child_index = 2 * index + 2
      largest = index

      if left_child_index < len(self.heap) and \
        self.heap[left_child_index][0] < self.heap[largest][0]:  # 우선순위가 높은 것(작은 값)이 위로 올라오도록
        largest = left_child_index

      if right_child_index < len(self.heap) and \
        self.heap[right_child_index][0] < self.heap[largest][0]:  # 같은 비교
        largest = right_child_index

      if largest != index:
        self._swap(index, largest)
        index = largest
      else:
        break

  def _swap(self, i, j):
    self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
