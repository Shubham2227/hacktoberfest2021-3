# Python3 program to count buildings
# that can see sunlight.

# Returns count buildings that
# can see sunlight


def countBuildings(arr, n):

	# Initialuze result (Note that first
	# building always sees sunlight)
	count = 1

	# Start traversing element
	curr_max = arr[0]
	for i in range(1, n):

		# If curr_element is maximum or
		# current element is equal,
		# update maximum and increment count
		if (arr[i] > curr_max or arr[i] == curr_max):

			count += 1
			curr_max = arr[i]

	return count


# Driver code
arr = [7, 4, 8, 2, 9]
n = len(arr)
print(countBuildings(arr, n))

# This code is contributed by Rohit.
