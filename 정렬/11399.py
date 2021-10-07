# ATM
# 문제 설명만 길었지 생각보다 쉬운 문제다. 앞에서 등장한 수를 모두 더하는 식을 만들고 최솟값을 설정해줄 수 있다.
# 하지만 나는 그렇게 생각하지 않고 아예 일처리를 빨리 할 수 있는 사람을 모두 앞에서 일을 처리하는 상황을 설정하는 것도 괜찮겠다고 생각했다.
# 풀이:  Ai = A1 + A2 + ...... + Ai-1 + Ai 이기 때문이다.

N = int(input())
P = list(map(int, input().split())  #list(map(int, __)) <<를 사용하여 map함수를 활용하자. 그리고 입력받은 정수값을 split를 사용해서 나눠준다.

P.sort() #sort를 사용해서 내림차순으로 미리 정한다.

answer = 0
for i in range(1, N+1):
    answer += sum(P[:i])

print(answer)
