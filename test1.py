#첫째 줄에 N(2 <= N <= 1000), M(1 <= M <= 10000), K(1 <= K <= 10000의 자연수가 주어지며 각자연수는 공백으로 구분한다.
#둘째 줄에 N개의 자연수가 주어진다. 각 자연수는 공백으로 구분한다. 단, 각각의 자연수는 1 이상 10000 이하의 수로 주어진다.
#입력으로 주어지는 K는 항상 M보다 작거나 같다.

#출력 조건: 첫쨰 줄에 동빈이의 큰 수의 법칙에 따라 더해진 답을 출력한다. 

n, m, k = map(int, input().split())

data = list(map(int, input().split()))

data.sort() #입력받은 수 정렬
first = data[-1] #가장 큰 수
second= data[-2] #두 번쨰로 큰 수

result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += first #가장 큰 수를 k번 더하기
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1
    
print(result)    
         
        
#count = int(m/(k+1))*k
#count += m%(k+1)

#result = 0
#result += (count)*first
#result += (m-count)*second

#print(result)