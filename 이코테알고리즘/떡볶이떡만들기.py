# 떡볶이 떡 만들기
# 떡볶이 떡의 길이가 일정하지않음 -> 한 봉지 안에 들어가는 떡의 총길이는 절단기로 맞춰줌
# 절단기에 높이를 지정하면 (H) 줄지어진 떡 한번에 절단 -> 긴떡 -> 위에부분잘림, 낮은떡 안잘림
# 절단기로 자르고 난 다음의 높이만큼을 손님에게 줘야한다.
# -> 손님이 요청한 길이가 M일 때 적어도 M만큼의 떡을 얻기 위해 절단기에 설저알 수 있는 높이의 최댓값 출력

# 조건이 2억까지이므로 전형적인 이진탐색 문제, 파라메트릭 서치 유형 -> 현재 이 높이로 자르면 조건만족가능한가
# 피라메트릭 서치 : 최적화 문제를 결정 문제(예,아니오로 답하는 문제)
# 계획 : 정렬 후에 절단기의 높이를 이진탐색으로 찾고 해당 위치부터 끝까지 더한후 더한 개수만큼의 절단기높이뺀값 비교.
import sys


N,M = map(int, sys.stdin.readline().split())    # 떡개수, 떡길이제한
lengs = list(map(int, sys.stdin.readline().split()))

start,end = 0, max(lengs)
result =[]
while start<=end:
    mid = (start+end)//2
    _sum = 0

    for leng in lengs:
        if mid < leng:
            _sum+= leng-mid

    if _sum<M:  # 잘린 길이가 부족한경우
        end-=mid-1  # 덜 자르게 end-1함
    else: # 잘린길이가 충족한경우
        result.append(mid)  # 다른 길이와 비교하기 위해 저장
        start+=1       # 충족하니까 더 자르게 start+1를 해서 mid를 키움

print(max(result))

# 굳이 정렬하지 않아도 이진탐색을 사용할 수 있다는 것을 알았다.
# 배열의 길이로 판별하지않고 가장큰수의 사이즈만으로 중간점을 도출하였고, 값을 하나씩 비교하며 더했다.
# 하나씩 비교하기 보다 처음에 정렬하고 mid보다 큰수가 나오는 지점부터 끝을 모두 더한후 -mid*해당배열길이 해도 될거같았다
# 중요한 것은 중단점 즉 start>=end가 중요하다. (시작과 끝이 엇갈리면 비효율적)