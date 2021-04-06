def solution(money):
    N = len(money)
    dp1 = [0]*len(money) #첫 집을 훔친상태
    dp2 = [0]*len(money) 
    dp1[0] = money[0]
    dp1[1] = money[0]
    dp2[1] = money[1]
    
    for index in range(2,len(money)-1):
        dp1[index] = max(dp1[index-1], dp1[index-2]+money[index])
        dp2[index] = max(dp2[index-1], dp2[index-2]+money[index])
        
    dp1[N-1] = dp1[N-2]
    dp2[N-1] = max(dp2[N-2], dp2[N-3]+money[N-1])
    
    return max(dp1[N-1], dp2[N-1])