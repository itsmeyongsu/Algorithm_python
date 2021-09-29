#알파벳 소문자로만 이루어진 단어 S가 주어진다. 
# 각각의 알파벳에 대해서, 단어에 포함되어 있는 경우에는 처음 등장하는 위치를, 
# 포함되어 있지 않은 경우에는 -1을 출력하는 프로그램을 작성하시오.

S = input()                                          #단어 S 선언
alphabet = list('abcdefghijklmnopqrstuvwxyz')       #알파벳 갯수(아스킷코드 = list(range(97,123))도 가능)

for x in alphabet :
    print(S.find(chr(x)))

#다른 풀이
word = input()
alphabet = list(range(97,123))  # 아스키코드 숫자 범위

for x in alphabet :
    print(word.find(chr(x))) 
