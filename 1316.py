# 이번 문제는 연속된 단어가 앞에서 한 번 언급 되었을 때,
# 뒤에서 한번 더 언급되면 인정하지 않는 문제다. 
# 그룹 단어의 개수를 출력해주면 된다.

N = int(input())
result = N
for i in range(0,N):
    word=input()
    for j in range(0,len(word)-1):
        if word[j]==word[j+1]:
            pass
        elif word[j] in word[j+1:]:
            result-=1
            break
print(result)