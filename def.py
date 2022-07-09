def open_account():
    print("새로운 계좌과 생성되었습니다.")

def deposit(balance, money):
    print("입금이 완료되었습니다. 잔액은 {0} 원입니다. ".format(balance + money))
    return balance + money

def withdraw(balance, money):
    if balance < money:
        print("잔액 부족. 잔액은 {0} 원입니다.".format(balance))
        return balance
    else:
        print("출금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance-money))
        return balance - money


def withdraw_night(balance, money):
    commission = 100

    if balance < money + commission:
        print("잔액 부족. 잔액은 {0} 원입니다.".format(balance))

    else:
        print("출금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance-money - commission))
        return commission, balance - money - commission

open_account()
balance = 0
balance = deposit(balance, 1000)
print(balance)

commisson, balance = withdraw_night(balance, 500)
print("수수료는 {0} 원 이며, 잔액은 {1} 원 입니다.".format(commisson, balance))