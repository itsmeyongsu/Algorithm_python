#N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
#2750번과 똑같이 해봤는데 시간초과로 틀렸었다. 왜일까?
#도저히 몰라서 풀이를 봤다.
#그런데 블로그 글을 보니 pypy3로 돌려보면 된다고 해서 해봤는데 됐다...! 코드 전환상 더 빠르다고 한다.
#그래도 파이썬 풀이를 한번 다시 찾아봤더니 해당 코드를 보고 공부해보았다. 

#시간이 에러가 났기 때문에 input()과 print()함수를 사용하지 않고 import sys를 통해서 system input과 system output을 사용해했다.

import sys #sys import한다.

N = int(input())
M = []

for i in range(N):
    M.append(int(sys.stdin.readline())) #sys함수(sys.stdin.readline()) << 근데 이걸 내가 기억할 수 있을지 모르겠다.
for i in sorted(M):
    sys.stdout.write(str(i)+'\n')

# 호기심에 pypy로 바꿔서 해봤는데 이 정도는 메모리초과더라