import random
def play_lotto():
    """
    :return: 6 lotto number
    """
    lotto = [ n for n in range(1, 46)]
    random.shuffle(lotto)

    choice = []
    choice.append(lotto.pop())
    choice.append(lotto.pop())
    choice.append(lotto.pop())
    choice.append(lotto.pop())
    choice.append(lotto.pop())
    choice.append(lotto.pop())
    choice = sorted(choice)
    return choice


def check_lotto(my_lotto, game_lotto):
    """
    :param my_lotto:
    :param game_lotto:
    :return: my place
     1: if 6 numbers match
     3: if 5 numbers match
     4: if 4 numbers match
     5: if 5 numbers match
     0: else: means you get nothing... sorry
    """
    count = 0
    for n in my_lotto:
        if n in game_lotto:
            count += 1
    if count == 6:
        return 1
    elif count == 5:
        return 3
    elif count == 4:
        return 4
    elif count == 3:
        return 5
    else:
        return 0


def calc_money(my_place):
    """

    :param my_place:
    :return: amount

    """
    if my_place == 1:
        return 1000000000
    elif my_place == 3:
        return 500000
    elif my_place == 4:
        return 50000
    elif my_place == 5:
        return 5000
    else:
        return 0

n = input("How many games do you want? :")
n = int(n)
all_list = []
print("Your number is ...")
for i in range(n):
    my_lotto = play_lotto()
    # print(my_lotto)
    all_list.append(my_lotto)

res_lotto = play_lotto()
print("Lotto number is ...")
print(res_lotto)
tot_money = 0
for lot in all_list:
    place = check_lotto(lot, res_lotto)
    money = calc_money(place)
    tot_money += money
    if money != 0:
        if money > 50000:
            print(lot, place, money, "----------------------------------------")
        else:
            print(lot, place, money)
print(n*1000, tot_money)