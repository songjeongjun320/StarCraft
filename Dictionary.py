cabinet = {3:"유재석", 100:"김태호"}
# print(cabinet[3])
# print(cabinet[100])

# print(cabinet.get(3))

# key값이 없는경우 밑처럼 할 경우 프로그램 바로 멈춤
# print(cabinet[5])
# print("hi")

# key 값이 없는경우 밑처럼 할 경우 hi출력됨.
# print(cabinet.get(5))
# print(cabinet.get(5), "사용 가능")
# print("hi")

# print(3 in cabinet) 
# print(5 in cabinet)

cabinet = {"A-3":"유재석", "B-100":"김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])

# 새손님
print(cabinet)
cabinet["A-3"] = "김종국"
cabinet["C-20"] = "조세호"
print(cabinet)

# 간 손님
del cabinet["A-3"]
print(cabinet)

# key들만 출력
print(cabinet.keys())

# value 들만 출력
print(cabinet.values())

# key, value 쌍으로 출력
print(cabinet.items())

# 목욕탕 폐점
cabinet.clear()
print(cabinet, type(cabinet))