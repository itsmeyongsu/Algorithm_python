# 일곱난쟁이문제
# 총 키의 합이 100이 되도록 해라

list = []  
for i in range(9):
    list.append(int(input()))
sum_l = sum(list)

one = 0
two = 0
for i in range(8):
    for j in range(i+1, 9):
        if sum_l - (list[i] + list[j]) == 100:
            one = list[i]
            two = list[j]
list.remove(one)    #제거
list.remove(two)    #제거
list.sort()     #오름차순정렬
for i in list:
    print(i)

#9명중 두명을 빼서 100이 되면 그 원소들을 전부 리스트에서 빼주고 정렬 후 출력한다.