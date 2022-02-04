# 설탕공장 
# 설탕 정확하게 N킬로그램 배달
# 설탕 봉지 : 3킬로, 5킬로
# 최대한 적은 봉지 -> 18킬로그램 -> 5킬로3+3킬로1개 > 3킬로6개

# 풀이( 수도코드)
# k5 = N킬로 // 5     # 큰킬로개수부터 구한다
# k3 = (N킬로 % 5)    # 나머지는 작은 킬로로 구한다.
# if  k3 %3 != 0: # 정확하게 배달할수없을때
#       if N킬로%3 == 0:
            # return(N%3)
        #else:
#           return(-1)
# else:
    # k3 = k3 // 3
    # return(k5+k3)

# 코드
def solution(N):
    k5 = N // 5  # 큰킬로개수부터 구한다
    k3 = (N % 5)  # 나머지는 작은 킬로로 구한다.
    if  k3 % 3 != 0: # 나머지가 정확하게 떨어지지않는경우
        for i in range(0,N,5):  # 나머지에 5를 더하며 3으로 나뉘어떨어지는지본다.
            if (k3+i)%3==0:
                return((k5-(i//5))+((k3+i)//3))
        return(-1)
    return(k5+(k3//3))  # 나머지가 3으로 잘 나뉘는경우 개수더해준다.

N = int(input())
print(solution(N))

# 17, 11, 16 같이 3과 5를 적절히 배분해야만 풀수 있는 숫자가 있어 까다로웠다
# 이런 숫자들은 폴문을 돌려 5로 나누어놓은 나머지에 5씩 더해가며 3으로 나뉘어지는지 골라냈다
# 만약 17이면 5한개 + 3네개이므로 조건에 걸려서
#   5키로로나눈k5에 더한 5의 개수를 빼고
#   여기다가 3키로봉지의 개수를 더해주었다.
# 이렇게 폴문을 돌려도 정확하게 떨어지지않으면 -1을 리턴하였다.

# 정리하자면 체크할 경우는 4가지이다.
# 1. 5로 나눈 나머지가 3으로 나누어떨어지는경우
# 2. 3으로만 나뉘는 경우
# 3. 5로 나눈 나머지에 5를 추가로 더해야만 3으로 나뉘는 경우
# 4. 모든 조건을 사용해도 정확하게 나뉘지않는 경우