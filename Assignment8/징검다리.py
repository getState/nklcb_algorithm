def solution(distance, rocks, n):
    rocks = sorted(rocks)
    answer = 0
    left = 0
    right = 1000000000
    while left<=right:
        mid = (left+right)//2
        if check(mid, rocks, n):
            answer = mid
            left = mid+1
        else:
            right = mid-1
        
    return answer


def check(mid, rocks_arr, max_n):
    now = 0
    n_count = 0
    for (index, value) in enumerate(rocks_arr):
        next = value-now
        if next>=mid:
            now = value
        elif next<mid :
            n_count += 1
            if(n_count>max_n):
                return False
    return True