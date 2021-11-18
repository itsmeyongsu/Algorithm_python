# 널리 잘 알려진 자료구조 중 최대 힙이 있다. 최대 힙을 이용하여 다음과 같은 연산을 지원하는 프로그램을 작성하시오.

# 배열에 자연수 x를 넣는다.
# 배열에서 가장 큰 값을 출력하고, 그 값을 배열에서 제거한다.
# 프로그램은 처음에 비어있는 배열에서 시작하게 된다.

# heapq 모듈은 기본적으로 최소힙만을 지원하기 때문에 최대힙을 구하려면 튜플이나 리스트형식으로 넣어 0번째 인덱스의 값을 기준으로 최소힙을 구성해야한다.

import sys
import heapq

N = int(sys.stdin.readline())
heap = []

for _ in range(N):      # n번 순회하면서 값을 넣는다.
    x = int(sys.stdin.readline())
    if x == 0:
        if heap:
            print(heapq.heappop(heap)[1])   # 여기서 차이나네
        else:
            print('0')
    else:
        heapq.heappush(heap, [-x,x])    # 인덱스 값을 기준으로 트리의 상단과 하단을 미리 설정한다는 개념이다.

#최소힙
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
