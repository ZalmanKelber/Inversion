def inversions (arr):
    sorted = []
    invs = 0
    n = len(arr)
    if n <= 1:
        return [arr, invs]
    else:
        arr1, arr2 = inversions(arr[ : n / 2])[0], inversions(arr[n / 2 : ])[0]
        invs += inversions(arr[ : n / 2])[1] + inversions(arr[n / 2 : ])[1]
        arr1_counter, arr2_counter = 0, 0
        for i in range(n):
            if arr1_counter == n / 2:
                sorted.append(arr2[arr2_counter])
                arr2_counter += 1
            elif arr2_counter == n - n / 2:
                sorted.append(arr1[arr1_counter])
                arr1_counter += 1
            elif arr1[arr1_counter] <= arr2[arr2_counter]:
                sorted.append(arr1[arr1_counter])
                arr1_counter += 1
            else:
                sorted.append(arr2[arr2_counter])
                arr2_counter += 1
                invs += n / 2 - arr1_counter
        return [sorted, invs]

input_array = []
f = open("IntegerArray.txt", "r")
next_int = f.readline()
while len(next_int) > 0:
    input_array.append(int(next_int))
    next_int = f.readline()
print(inversions(input_array)[1])

