def binarySearch(list, item):
  low = 0
  high = len(list) - 1
  while (low <= high):
    mid = int((low + high)/2)
    guess = list[mid]
    if guess == item:
      return mid
    if guess > item:
      high = mid -1
    else:
      low = mid + 1
  return None


arr = [1,5,8,9]
it = 2

a = binarySearch(arr, it)
print(a)
