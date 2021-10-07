#알파벳 대소문자로 된 단어가 주어지면,
#이 단어에서 가장 많이 사용된 알파벳이 
#무엇인지 알아내는 프로그램을 작성하시오. 
#단, 대문자와 소문자를 구분하지 않는다.

word = input().upper()  #대문자로 애초에 설정
word_list=list(set(word))   #set함수를 사용해서 중복을 제거하고, list로 묶음
cnt  = [] #가장 많이 사용된 알파벳을 알기 위해서 리스트로 초기화
#word = "MISSISSIPI"
#word list = ['M', 'I', 'S', 'P']

for x in word_list: #for문으로 반복
    count = word.count(x)   #count변수를 새로 생성해서 word를 세어준다.
    cnt.append(count)   #cnt 리스트에 추가(append)해준다.
#cnt = [4,4,1,1] << 이 되겠지?

if cnt.count(max(cnt)) >= 2:    #그리고 여기부터 아예 손도 못댔는데 자꾸 ?만 떠서 머리가 터져버릴 것 같았다. 
    print("?")  #근데 알고보니 2개 이상이어야 한단다. max가 두개 이상이라는 개념이란다 참나.
else:
    print(word_list[(cnt.index(max(cnt)))]) #그래서 나머지의 경우 최대값(max)의 것을 출력해주면 된다.
#즉, word = "abca"에서 word_list = [a,c,b] cnt = [2,1,1]이 되니까, max(cnt)는 2가 되고, word_list[1]은 a를 가리킨다// 개어렵네
#  # 간단해보였는데 진짜 어려웠다. 머리가 터져버릴 것 같았지만 잘 참았다. 
# 초반에 문자를 받아서 대문자로 통일시키고 set함수로 중복된 값을 제거하는 거 까지는 잘했으나, 
# 나머지가 개판이었다.