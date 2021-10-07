##N개의 숫자가 공백 없이 쓰여있다. 이 숫자를 모두 합해서 출력하는 프로그램을 작성하시오.

n = input()
nums = input()
sum = 0

for i in nums:
    sum += int(i)  # total= total+int(i)
print(sum)

#코드 작성에 대한 전체적인 풀이
#숫자 n을 입력받으면 n개만큼의 공백 없이 쓰여있는 숫자를 입력받고서 숫자들의 합을 구하는 문제이다. 
#숫자의 합은 for문으로도 구할 수 있고 sum 함수로 간단하게 구할 수 있다. 


##다른 방법(구글링) -- 더빠름
a = input()

print(sum(map(int, input())))   ##map 함수를 사용하기 근데 나는 map을 몰랐음. (map(적용시킬 함수,적용할 값들))