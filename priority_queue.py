# Function to return the index of the
# parent node of a given node
def parent(i):
    return (i - 1) // 2


# Function to return the index of the
# left child of the given node
def leftChild(i):
    return ((2 * i) + 1)


# Function to return the index of the
# right child of the given node
def rightChild(i):
    return ((2 * i) + 2)


# Function to shift up the node in order
# to maintain the heap property
def shiftUp(i, arr):
    while i > 0 and arr[parent(i)] < arr[i]:
        # Swap parent and current node
        arr[parent(i)], arr[i] = arr[i], arr[parent(i)]

        # Update i to parent of i
        i = parent(i)


# Function to shift down the node in
# order to maintain the heap property
def shiftDown(i, arr, size):
    maxIndex = i

    # Left Child
    l = leftChild(i)

    if l <= size and arr[l] > arr[maxIndex]:
        maxIndex = l

    # Right Child
    r = rightChild(i)

    if r <= size and arr[r] > arr[maxIndex]:
        maxIndex = r

    # If i not same as maxIndex
    if i != maxIndex:
        arr[i], arr[maxIndex] = arr[maxIndex], arr[i]
        shiftDown(maxIndex, arr, size)


# Function to insert a new element
# in the Binary Heap
def insert(p, arr, size):
    size[0] = size[0] + 1
    arr.append(p)

    # Shift Up to maintain heap property
    shiftUp(size[0], arr)


# Function to extract the element with
# maximum priority
def extractMax(arr, size):
    result = arr[0]

    # Replace the value at the root
    # with the last leaf
    arr[0] = arr[size[0]]
    size[0] = size[0] - 1

    # Shift down the replaced element
    # to maintain the heap property
    shiftDown(0, arr, size[0])
    return result


# Function to change the priority
# of an element
def changePriority(i, p, arr, size):
    oldp = arr[i]
    arr[i] = p

    if p > oldp:
        shiftUp(i, arr)
    else:
        shiftDown(i, arr, size[0])


# Function to get value of the current
# maximum element
def getMax(arr):
    return arr[0]


# Function to remove the element
# located at given index
def remove(i, arr, size):
    arr[i] = getMax(arr) + 1

    # Shift the node to the root
    # of the heap
    shiftUp(i, arr)

    # Extract the node
    extractMax(arr, size)


if __name__ == "__main__":

    #       45
    #     /      \
    #    31      14
    #   /  \    /  \
    #  13  20  7   11
    # /  \
    # 12   7
    # Create a priority queue shown in
    # example in a binary max heap form.
    # Queue will be represented in the
    # form of array as:
    # 45 31 14 13 20 7 11 12 7
    # Insert the element to the
    # priority queue
    arr = []
    size = [-1]
    insert(45, arr, size)
    insert(20, arr, size)
    insert(14, arr, size)
    insert(12, arr, size)
    insert(31, arr, size)
    insert(7, arr, size)
    insert(11, arr, size)
    insert(13, arr, size)
    insert(7, arr, size)

    i = 0

    # Priority queue before extracting max
    print("Priority Queue : ", end="")
    while i <= size[0]:
        print(arr[i], end=" ")
        i += 1

    print()

    # Node with maximum priority
    print("Node with maximum priority : " + str(extractMax(arr, size)))

    # Priority queue after extracting max
    print("Priority queue after extracting maximum : ", end="")
    j = 0
    while j <= size[0]:
        print(arr[j], end=" ")
        j += 1

    print()

    # Change the priority of element
    # present at index 2 to 49
    changePriority(2, 49, arr, size)
    print("Priority queue after priority change : ", end="")
    k = 0
    while k <= size[0]:
        print(arr[k], end=" ")
        k += 1

    print()

    # Remove element at index 3
    remove(3, arr, size)
    print("Priority queue after removing the element : ", end="")
    l = 0
    while l <= size[0]:
        print(arr[l], end=" ")
        l += 1