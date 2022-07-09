# 튜플 쓰는법
menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])

# 튜플은 수정하는 기능 불가
# menu.add("생선까스")

# name = "김종국"
# age = 20
# hobby = "코딩"
# print(name, age, hobby)

(name, age, hobby) = ("김종국", 20, "코딩")
print(name, age, hobby)