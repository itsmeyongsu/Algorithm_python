#N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
#sol
#이 문제는 sort 함수를 사용하면 쉽게 풀 수 있는 문제이다.

N = int(input()) 

num = []

for i in range(N) : 
    num.append(int(input()))

num.sort()      #sort함수: 자동으로 오름차순

for j in num:
    print(j)


#다른 풀이: 버블소트
# bobble sort는 이번에 처음 들었는데, 복잡해보이는데 좋은 풀이라고 한다.
# 

N = int(input())

num = []

for _ in range(N) : 
    num.append(int(input()))

#Bobble sort code
for i in range(len(num)) : 
    for j in range(len(num)) : 
        if num[i] < num[j] : 
            num[i], num[j] = num[j], num[i]
            
for n in num: 
    print(n)