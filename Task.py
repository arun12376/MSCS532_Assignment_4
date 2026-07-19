class Task:
   """Represents a single task in the priority queue scheduler."""
   def __init__(self, task_id, priority, arrival_time, deadline):
       self.task_id = task_id
       self.priority = priority          # Higher integer value = higher priority
       self.arrival_time = arrival_time  # Simulation arrival time marker
       self.deadline = deadline          # Task expiration deadline limit

   def __repr__(self):
       return f"[ID: {self.task_id} | Priority: {self.priority}]"


class PriorityQueue:
   """
   A Max-Heap Priority Queue implementation for Task scheduling objects.
   """
   def __init__(self):
       self.heap = []  # Internal array storage for heap nodes

   def _bubble_up(self, idx):
       """
       Restores the max-heap property upwards from the given index.
       Runs in O(log n) time.
       """
       while idx > 0:
           parent_idx = (idx - 1) // 2
           # If current task has higher priority than its parent, swap them
           if self.heap[idx].priority > self.heap[parent_idx].priority:
               self.heap[idx], self.heap[parent_idx] = self.heap[parent_idx], self.heap[idx]
               idx = parent_idx
           else:
               break

   def insert(self, task):
       """
       Inserts a new Task object into the Priority Queue.
       Time Complexity: O(log n) where n is the number of elements.
       Space Complexity: O(1) auxiliary space.
       """
       # Step 1: Append the element to the end of the array representation
       self.heap.append(task)
      
       # Step 2: Bubble the element up to fix any heap property violations
       self._bubble_up(len(self.heap) - 1)

   def peek_max(self):
       """Returns the highest priority task without removing it. O(1) time."""
       if not self.heap:
           return None
       return self.heap[0]

   def size(self):
       """Returns current size of queue. O(1) time."""
       return len(self.heap)


# Verification Driver Code
if __name__ == "__main__":
   print("\n--- Testing Priority Queue Insertions ---")
   pq = PriorityQueue()
  
   # Simulating arriving workflow tasks
   tasks_to_schedule = [
       Task(task_id="T1", priority=10, arrival_time=0, deadline=5),
       Task(task_id="T2", priority=45, arrival_time=1, deadline=10),
       Task(task_id="T3", priority=20, arrival_time=2, deadline=8),
       Task(task_id="T4", priority=99, arrival_time=3, deadline=3)
   ]
  
   for t in tasks_to_schedule:
       pq.insert(t)
       print(f"Inserted {t} -> Current Highest Priority Task: {pq.peek_max()}")
