#"OOXXOXXOOO"와 같은 OX퀴즈의 결과가 있다. O는 문제를 맞은 것이고, X는 문제를 틀린 것이다. 
# 문제를 맞은 경우 그 문제의 점수는 그 문제까지 연속된 O의 개수가 된다. 예를 들어, 10번 문제의 점수는 3이 된다.
#"OOXXOXXOOO"의 점수는 1+2+0+0+1+0+0+1+2+3 = 10점이다.
#OX퀴즈의 결과가 주어졌을 때, 점수를 구하는 프로그램을 작성하시오.


N = int(input()) 

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

#뭔소린지 몰랐다. 하지만 몇번의 시도 끝에 성공했고, 
#문자열을 입력받아서 한 글자씩 비교해서 O가 연속으로 나올 경우 점수가 올라가고,
#X가 나오면 점수가 초기화시켰다.