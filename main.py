ls = [2, 4, 3, 7, 1, 5, 3, 150, 75, 8]

# def min_sort(arr):
#   sorted_array = []
#   for x in range(len(arr)):
#     m = min(arr)
#     sorted_array.append(m)
#     arr.remove(m)
#   return sorted_array

# r = min_sort(ls)
# print(r)

def bubble_sort(arr):
  for x in range(len(arr)):
    for y in range(1, len(arr)):
      if arr[y - 1] > arr[y]:
        arr[y - 1], arr[y] = arr[y], arr[y - 1]

bubble_sort(ls);
print(ls)
