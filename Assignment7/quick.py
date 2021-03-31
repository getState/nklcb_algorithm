# def quicksort(x):
#     if len(x) == 1:
#         return x
    
#     pivot = x[0]

#     left = 1
#     right = len(x)-1

#     for index in range(1, len(x)):
#         if x[left] >pivot :
#             x[left], x[right] = x[right], x[left]
#             right -= 1
#         else:
#             left += 1
    
#     queicksort(x[left:right])+[pivot]+quicksort(x[right:])


def quicksort(x):
    def quick(low, high):
        if low >= high:
            return
        pivot = x[low]

        left = low+1
        right = high
        
        while left<right:
            if x[left] > pivot :
                x[left], x[right] = x[right], x[left]
                right -= 1
                print(x)
            else:
                left += 1
        x[left-1], x[low] = x[low], x[left-1]
        quick(low, left-1)
        quick(right, high)
    quick(0, len(x)-1)
    

arr = [2, 6, 1, 4, 2, 3, 4]
print(arr)
quicksort(arr)
print(arr)

