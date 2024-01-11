def quicksort(data):
  """
  Implements the quicksort algorithm to sort a list of numbers.

  Args:
    data: A list of numbers to be sorted.

  Returns:
    s_d: A new list containing the sorted data.

  Explain the logic:
    pivot means center of the data.
    it selects the first element of the list as the pivot element.

    It creates two empty lists left and right.

    It then creates a new list containing all elements from the input list,
    which are less than or equal to the pivot element by using list comprehension
    left = [x for x in data[1:] if x <= pivot] and assigns it to the left list

    It then creates a new list containing all elements from the input list,
    which are greater than the pivot element by using list comprehension,
    right = [x for x in data[1:] if x > pivot] and assigns it to the right list

    It then recursively calls the quicksort function on the left and right list
    and concatenates the result with the pivot element in the middle to get the final sorted list.

  User's Input:
    It is asking the user for 10 inputs, converting them to integers
    and appending them to a list called u_d which is then passed to the
    quicksort function to get the sorted list s_d.
    Finally, it prints the unsorted and sorted list.

    It also checks if the user input is empty or not,
    if it is empty it will ask the user to enter a valid number.
  """
  # generate the logic to sort the data.

  ## entered values are nothing OR 1 then its already sorted.

  if len(data) <= 1:
    return data

  pivot = data[0]
  left = [x for x in data[1:] if x <= pivot]
  right = [x for x in data[1:] if x > pivot]

  return quicksort(left) + [pivot] + quicksort(right)

x = 0
u_d = []

# asking 10 user inputs.
while (x < 10):
  y = (input("Enter number to sort: "))
  # remove empty inputs.
    if (y != ""):
    z = int(y)
    u_d.append(z)
  else:
    print("Enter the valid number.")
  x += 1
# applying logic
s_d = quicksort(u_d)
print("\nOK. here is the answer.,")
print(f"\nUnsorted data: {u_d}")
print(f"\nSorted data: {s_d}")
