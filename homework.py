# Function starts
def mergesort(list):

    # Stop at one item
    if len(list) > 1:

        # Find middle position
        m = len(list) // 2

        # Left half
        L = list[:m]

        # Right half
        R = list[m:]

        # Sort left half
        mergesort(L)

        # Sort right half
        mergesort(R)

        # Create three cursors
        a = b = c = 0

        # Compare competitors
        while a < len(L) and b < len(R):

            # Left wins?
            if L[a] > R[b]:

                # Write left winner
                list[c] = L[a]

                # Move left cursor
                a += 1

            else:

                # Write right winner
                list[c] = R[b]

                # Move right cursor
                b += 1

            # Move write cursor
            c += 1

        # Leftovers in left half
        while a < len(L):

            # Copy remaining number
            list[c] = L[a]

            # Move left cursor
            a += 1

            # Move write cursor
            c += 1

        # Leftovers in right half
        while b < len(R):

            # Copy remaining number
            list[c] = R[b]
            b += 1
            c += 1


def printList(list):
    for i in range(len(list)):
        print(list[i], end=" ")
   
    
# Unsorted data
list = [21,54,79,11,83,44,67,10,124]


print("Before sort: {}".format(list))
mergesort(list)
print("After sort:",list)
