# 좌표정렬하기
#첫째줄에 N받고 x,y 위치가 주어지고 항상 정수고, 위치가 같은 두 점은 없다.

import sys      #sys 활용해보기
N = int(sys.stdin.readline()) ##이게 인풋느낌인거임
list = []

for i in range(N):
    list.append(list(map(int, sys.stdin.readline().split))) #받는거 추가해라
list.sort(key=lambda x: (x[0], x[1]))       #lamda인자: 표현식 >> 해서 증가해주는 구현식 생성
for i in list:
    print(i[0], i[1])

#다른 풀이

N = int(input())
list = []
for i in range(N):
    [a,b] = map(list(int, input().split()))
    list.append([a,b])

list.sort

for i in range(N):
    print(list([i][0], list[i][1]))

# 메모리 초과 >> pypy로 돌려야 성공

