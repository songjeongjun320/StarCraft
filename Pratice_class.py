class Unit:
    def __init__(slef):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Flyable, Unit): # FlyableUnit(Unit, Flyable): 하면 "Unit 생성자" 
    def __init__(self):
        super().__init__() # 이렇게 super를 쓰면 앞의 클래스만 상속이 된다.
        Unit.__init__(self)
        Flyable.__init__(self)

#드랍쉽
dropship = FlyableUnit()