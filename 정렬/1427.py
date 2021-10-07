# 배열을 정렬하는 것은 쉽다. 수가 주어지면, 그 수의 각 자리수를 내림차순으로 정렬해보자.
# 간단한 배열문제

n = int(input())
 
list = []
for i in str(n):
    list.append(int(i))


list.sort(reverse=True) # 내림차순
 
for i in list:
    print(i,end='') #end=''를 추가하여 한 줄에 출력이 되도록 한다.

