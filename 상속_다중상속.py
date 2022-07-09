# 일반 유닛
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))

# 공격 유닛
class AttackUnit(Unit):
        def __init__(self, name, hp, speed, damage):
            Unit.__init__(self, name, hp, speed)
            self.damage = damage

            print("{0} 유닛이 생성 되었습니다.".format(self.name))
            print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

        def attack(self, location):
            print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
                .format(self.name, location, self.damage))

        def damaged(self, damage):
            print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
            self.hp -= damage
            print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
            if self.hp <= 0:
                print("{0} : 파괴되었습니다.".format(self.name))

class HealUnit(Unit):
    def __init__(self, name, hp, heal):
        Unit.__init__(self, name ,hp)
        self.heal = heal

        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 {0}, 치유력 {1}".format(self.hp, self.heal))

    def healling(self, location):
        print("{0} : {1} 방향으로 아군을 치료합니다.".format(self.name, location))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))
    
# 드랍쉽 : 공중유닛, 수송기. 마린/파이어뱃/탱크 등을 수송. (공격 기능 없음)

# 날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))

# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) # 지상 speed 
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)


# 건물 //
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        #Unit.__init__(self, name, hp, 0)
        super().__init__(name, hp, 0) # super를 쓰는 방법, 괄호가 들어가고 self는 없어야 한다.
        self.location = location

# 서플라이 디폿 : 건물, 1개 건물 = 8 유닛.
supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

# Pass사용법, pass는 구현이 되어 있지 않아도 일단 오류 없이 넘어간다는 뜻.
def game_over():
    pass

game_start()
game_over()


"""
# 벌쳐 : 지상 유닛, 기동성이 좋음
vulture = AttackUnit("벌쳐", 80, 10, 20)
 
# 배틀 크루저 : 공중 유닛, 체력도 좋음, 공격력도 좋음
battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

vulture.move("11시")
battlecruiser.move("9시")

"""

"""
# 메딕 : 의무병 (공격력 없음)
medic1 = HealUnit("메딕", 45, 3)
medic1.healling("5시")

# 파이어뱃 : 공격 유닛, 화염 방사기.
firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")

# 공격 2번 받는다고 가정
firebat1.damaged(25)
firebat1.damaged(25)
"""