# 널리 잘 알려진 자료구조 중 최소 힙이 있다. 최소 힙을 이용하여 다음과 같은 연산을 지원하는 프로그램을 작성하시오.

# 배열에 자연수 x를 넣는다.
# 배열에서 가장 작은 값을 출력하고, 그 값을 배열에서 제거한다.
# 프로그램은 처음에 비어있는 배열에서 시작하게 된다.

# import sys
# import heapq

# N = int(sys.stdin.readline())
# heap = []

# for _ in range(N):
#     x = int(sys.stdin.readline())
#     if x == 0:
#         if heap:
#             print(heapq.heappop(heap))
#         else:
#             print('0')
#     else:
#         heapq.heappush(heap, x)


import sys
import heapq

N = int(sys.stdin.readline())
heap = []

for i in range(N):  # n번 순회하면서 값을 받는다.
    x = int(sys.stdin.readline())
    if x ==0:
        if heap:
            print(heapq.heappop(heap))
        else:
            print('0')
    else: heapq.heappush(heap, x)