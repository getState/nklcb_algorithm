# 문제 설명
# 정수를 저장한 배열, arr 에서 가장 작은 수를 제거한 배열을 리턴하는 함수, 
# solution을 완성해주세요. 
# 단, 리턴하려는 배열이 빈 배열인 경우엔 배열에 -1을 채워 리턴하세요. 
# 예를들어 arr이 [4,3,2,1]인 경우는 [4,3,2]를 리턴 하고, [10]면 [-1]을 리턴 합니다.
def solution(arr):
    min_num = arr[0]
    for elem in arr:
        if(min_num>elem):
            min_num = elem
    arr.remove(min_num)
    
    # 배열의 원소가 없는 경우 
    if len(arr)==0:
        arr.append(-1)
    
    return arr