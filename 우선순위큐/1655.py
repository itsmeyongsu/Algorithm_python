# 백준이는 동생에게 "가운데를 말해요" 게임을 가르쳐주고 있다. 백준이가 정수를 하나씩 외칠때마다 동생은 지금까지 백준이가 말한 수 중에서 중간값을 말해야 한다. 
# 만약, 그동안 백준이가 외친 수의 개수가 짝수개라면 중간에 있는 두 수 중에서 작은 수를 말해야 한다.

# 예를 들어 백준이가 동생에게 1, 5, 2, 10, -99, 7, 5를 순서대로 외쳤다고 하면, 동생은 1, 1, 2, 2, 2, 2, 5를 차례대로 말해야 한다. 
# 백준이가 외치는 수가 주어졌을 때, 동생이 말해야 하는 수를 구하는 프로그램을 작성하시오.

# 두 개의 heap이 필요하고, 주어진 수의 개수가 짝수라면 두 개의 heap에 들어가는 수의 갯수가
# 같을 것이다. 같다면 중간값의 기준이 되는 위의heap에 넣는다.
# 반면, 길이가 같지 않다면 길이를 맞추기 위해 다른 heap에도 수를 하나 넣어준다


import sys
import heapq

N=int(sys.stdin.readline())

upperheap = []
lowerheap = []
midean = []
for _ in range(N):

    x = int(sys.stdin.readline())

    if len(upperheap) == len(lowerheap):
        heapq.heappush(upperheap, (-x, x))
    else: 
        heapq.heappush(lowerheap, (x,x))

    if lowerheap and upperheap[0][1] > lowerheap[0][0]:
        min = heapq.heappop(lowerheap)[0]
        max = heapq.heappop(upperheap)[1]
        heapq.heappush(upperheap, (-min, min))
        heapq.heappush(lowerheap, (max, max))

    midean.append(upperheap[0][1])

for i in midean:
    print(i)

