N = int(input()) ##문자열을 입력받아서 한 글자씩 비교해서 O가 연속으로 나올 경우 점수가 올라가고 X가 나오면 점수가 초기화되면 되는 문제이다.

for i in range(N):
    a = input()
    score = 0
    sumScore = 0
    for j in a:
        if j == 'O':
            score += 1
        else:
            score = 0
        sumScore += score
    print(sumScore)    