import sys


# print("Python", "Java", "JavaScript", sep=" , ") #, end = "?")  // end의 의미는 문장의 끝을 뭘로 바꾼다는 의미
# print("무엇이 더 재밌을까요?")

# import sys
# print("Python", "Java", file=sys.stdout)
# print("Python", "Java", file=sys.stderr)

# scores = {"수학":0, "영어":50, "코딩":100}
# for subject, score in scores.items():
#     # print(subject, score)
#     print(subject.ljust(5), str(score).rjust(4), sep=":")

# 은행 대기순번표
# 001, 002, 003 ...
for num in range(1,21):
    print("대기번호 : " + str(num).zfill(3))


# 표준입력
answer = input("아무값이나 입력하세요 : ")
print("입력하신 값은 " + str(answer) +"입니다.")