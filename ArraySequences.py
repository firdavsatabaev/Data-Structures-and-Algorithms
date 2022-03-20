import sys
n = 10
data = []
for i in range(n):
    # Number of elements in list Data
    a = len(data)

    # Actual size of the list data in bytes
    b = sys.getsizeof(data)

    print(a,b)

    data.append(n)