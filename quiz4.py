# Quiz) 당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
# 참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다.
# 댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.
# 추첨 프로그램을 작성하시오.

# 조건1 : 편의상 댓글은 20명이 작성하였고 아이디는 1~20 이라고 가정
# 조건2 : 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가
# 조건3 : random 모듈의 shuffle 과 sample을 활용

# (출력 예제)
# -- 당첨자 발표 --
# 치킨 당첨자 : 1
# 커피 당첨자 : [2, 3, 4]
# -- 축하합니다. --

# (활용 예제)
# from random import *
# 1st = [1,2,3,4,5]
# print(1st)
# shuffle(1st)
# print(1st)
# print(sample(1st, 1))


# from random import * 를 붙이게 되면 rando. 을 붙일 필요가 없음.

from random import *

ticket_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(ticket_list)

shuffle(ticket_list)
print(ticket_list)

winner = sample(ticket_list,4)
print(winner)

print("-- 당첨자 발표 --")
print("치킨 당첨자 : {0}".format(winner[0]))

del winner[0]
winner.sort()
print("커피 당첨자 : {0}".format(winner))
print("-- 축하합니다. --")


# 유튜브 정답
from random import *
users = range(1,21)  
users = list(users)
# print(type(users))

print(users)
shuffle(users)
print(users)

winners = sample(users, 4)

print("-- 당첨자 발표 --")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))
print("-- 축하합니다 --")

