# 문제
# 정수(1 ~ 100) 1개가 입력되었을 때 카운트다운을 출력해보자.

# while 조건식 :
#   ...
#   ...

# 반복 실행구조를 사용해 보자.

# 입력예시
# 5

# 출력예시
# 4
# 3
# 2
# 1
# 0

# 풀이
num = int(input())
while num != 0:
    num -= 1
    print(num)