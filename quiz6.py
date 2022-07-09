"""
Quiz) 표준 체중을 구하는 프로그램을 작성하시오

*포준 체중 : 각 개인의 키에 적당한 체중

(성별에 따른 공식)
남자 : 키(m) x 키(m) x 22
여자 : 키(m) x 키(m) x 21

조건1 : 표준 체중은 별도의 함수 내에서 계산
        *함수명 : std_weight
        *전달값 : 키(height), 성별(gender)
조건2 : 표준 체중은 소수점 둘째자리까지 표시

(출력 예제)
키 175cm 남자의 표준 체중은 67.38kg 입니다.
"""

def std_weight(height, gender):
    if gender == "Male":
        return height*height*22
    elif gender == "Female":
        return height*height*21

male_average_weight = round(std_weight(1.75, "Male"),2)
female_average_weigit = std_weight(1.68, "Female")

print("키 {0}cm 남자의 표준  체중은 {1}kg 입니다.".format(175, male_average_weight, ))
print("키 {0}cm 여자의 표준  체중은 {1:.2f}kg 입니다.".format(160, female_average_weigit))