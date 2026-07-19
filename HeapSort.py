def max_heapify(arr, n, i):
   """
   Maintains the max-heap property iteratively.
   Runs in O(log n) time and O(1) space.
   """
   while True:
       largest = i
       left = 2 * i + 1
       right = 2 * i + 2

       # Check if left child exists and is greater than root
       if left < n and arr[left] > arr[largest]:
           largest = left


       # Check if right child exists and is greater than the current largest
       if right < n and arr[right] > arr[largest]:
           largest = right

       # If the largest element is not the root, swap and continue down
       if largest != i:
           arr[i], arr[largest] = arr[largest], arr[i]
           i = largest  # Move index down to the child node
       else:
           break


def build_max_heap(arr):
   """
   Converts an unordered array into a valid Max-Heap.
   Runs in O(n) time.
   """
   n = len(arr)
   # Start from the last non-leaf node and move upwards to the root
   for i in range(n // 2 - 1, -1, -1):
       max_heapify(arr, n, i)


def heapsort(arr):
   """
   Sorts an array in-place using the Heapsort algorithm.
   Time Complexity: O(n log n) across all cases.
   Space Complexity: O(1) auxiliary space.
   """
   n = len(arr)
   if n <= 1:
       return arr

   # Step 1: Transform the array into a Max-Heap
   build_max_heap(arr)

   # Step 2: Progressively extract elements from the heap
   for i in range(n - 1, 0, -1):
       # Move the current maximum (root) to the end of the unsorted boundary
       arr[0], arr[i] = arr[i], arr[0]
      
       # Restore the max-heap property on the reduced heap area
       max_heapify(arr, i, 0)
      
   return arr


if __name__ == "__main__":
   test_cases = {
       "Random Array": [12, 11, 13, 5, 6, 7],
       "Already Sorted": [1, 2, 3, 4, 5, 6],
       "Reverse Sorted": [6, 5, 4, 3, 2, 1],
       "Repeated Elements": [5, 5, 2, 2, 5, 1],
       "Empty Array": []
   }
  
   print("--- Verifying Heapsort Correctness ---")
   for name, array in test_cases.items():
       sorted_arr = heapsort(array.copy())
       # FIXED: Wrapped array and sorted_arr in str() so string padding works
       input_str = str(array)
       output_str = str(sorted_arr)
       print(f"{name:<18} -> Input: {input_str:<25} | Sorted: {output_str}")
