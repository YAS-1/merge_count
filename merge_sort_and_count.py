
def count_inversions(a):
    if len(a) <= 1:
        return a, 0
    
    mid = len(a)//2

    leftHalf,leftInversions=count_inversions(a[:mid])
    rightHalf,rightInversions=count_inversions(a[mid:])

    merged,inversions = merge(leftHalf,rightHalf)

    return merged,leftInversions + rightInversions + inversions

def merge(left,right):

    merged_list = []
    inversions = 0
    i = 0
    j = 0

    while i < len(left) and j < len(right):

        if left[i] <= right[j]:
            merged_list.append(left[i])
            i += 1

        else:
            merged_list.append(right[j])
            inversions += len(left) - i
            j += 1

    merged_list.extend(left[i:])
    merged_list.extend(right[j:])

    return merged_list,inversions

A = [3,2]
Sorted, inversions = count_inversions(A)

print(Sorted)
print(inversions)
