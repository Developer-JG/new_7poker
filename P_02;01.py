from random import randint

class Player:
    def __init__(self, deck, deck_num, deck_pat):
        self.deck = deck
        self.deck_num = deck_num
        self.deck_pat = deck_pat

def display_pat(pat):
    pat = int(pat)
    if pat == 1:
        return '스페이드'
    elif pat == 2:
        return '다이아'
    elif pat == 3:
        return '하트'
    elif pat == 4:
        return  '클로버'
    else:
        return display_pat((pat - (pat % 100)) / 100)

def print_deck(player_1, computer_1, who, len):
    if who == "player":
        print("{0:-^60}".format(" 나의 손카드 "))
        if len >= 1:
            print(f"첫번째 카드 : {display_pat(player_1.deck_pat[0])} {player_1.deck_num[0]}")
        if len >= 2:
            print(f"두번째 카드 : {display_pat(player_1.deck_pat[1])} {player_1.deck_num[1]}")
        if len >= 3:
            print(f"세번째 카드 : {display_pat(player_1.deck_pat[2])} {player_1.deck_num[2]}")
        if len >= 4:
            print(f"네번째 카드 : {display_pat(player_1.deck_pat[3])} {player_1.deck_num[3]}")
        if len >= 5:
            print(f"다섯번째 카드 : {display_pat(player_1.deck_pat[4])} {player_1.deck_num[4]}")
        if len >= 6:
            print(f"여섯번째 카드 : {display_pat(player_1.deck_pat[5])} {player_1.deck_num[5]}")
        if len >= 7:
            print(f"일곱번째 카드 : {display_pat(player_1.deck_pat[6])} {player_1.deck_num[6]}")


def shuffle(computer_1, player_1):
    while True:
        for i in range(0,8):
            player_1.deck_num.append(randint(1, 13))
            player_1.deck_pat.append(randint(1, 4))
            computer_1.deck_num.append(randint(1, 13))
            computer_1.deck_pat.append(randint(1, 4))

        for j in range(0, 8):
            player_1.deck.append((player_1.deck_pat[j] * 100) + (player_1.deck_num[j]))
            computer_1.deck.append((computer_1.deck_pat[j] * 100) + (computer_1.deck_num[j]))

        deck = player_1.deck + computer_1.deck

        if len(list(set(deck))) == 16:
            break
        else:
            computer_1 = Player([], [], [])
            player_1 = Player([], [], [])

def main():
    while True:
        print("\nthe New_7Poker game project\n")
        input("게임을 시작하려면 아무키나 누르세요.")
        print("\n게임시작 (카드버리기)\n")
        computer_1 = Player([], [], [])
        player_1 = Player([], [], [])

        shuffle(computer_1, player_1)

        print_deck(player_1, computer_1, "player", 3)
        print(f"네번째 카드 : {display_pat(player_1.deck_pat[7])} {player_1.deck_num[7]}")

        del_plag = 'n'
        del_ans = 0

        while del_plag == 'n':
            del_ans = input("\n어떤 카드를 버리시겠습니까? [1, 2, 3, (4)] : ")

            try:
                del_ans = int(del_ans)
                if del_ans == 1:
                    del_plag = input("첫번째 카드를 버리시겠습니까? [(y), n] : ")
                elif del_ans == 2:
                    del_plag = input("두번째 카드를 버리시겠습니까? [(y), n] : ")
                elif del_ans == 3:
                    del_plag = input("세번째 카드를 버리시겠습니까? [(y), n] : ")
                elif del_ans == 4:
                    del_plag = input("네번째 카드를 버리시겠습니까? [(y), n] : ")
                else:
                    del_plag = input("네번째 카드를 버리시겠습니까? [(y), n] : ")
            except:
                del_plag = input("네번째 카드를 버리시겠습니까? [(y), n] : ")

        try:
            if int(del_ans) <= 1:
                player_1.deck_pat[0] = player_1.deck_pat[1]
                player_1.deck_num[0] = player_1.deck_num[1]
            if int(del_ans) <= 2:
                player_1.deck_pat[1] = player_1.deck_pat[2]
                player_1.deck_num[1] = player_1.deck_num[2]
            if int(del_ans) <= 3:
                player_1.deck_pat[2] = player_1.deck_pat[7]
                player_1.deck_num[2] = player_1.deck_num[7]
        except:
            pass

        player_1.deck_pat[7] = '-'
        player_1.deck_num[7] = '-'

        print("\n" * 4)
        print_deck(player_1, computer_1, "player", 3)

        open_plag = 'n'
        open_ans = 0

        while open_plag == 'n':
            open_ans = input("\n어떤 카드를 공개하겠습니까? [1, 2, 3, (4)] : ")

            try:
                open_ans = int(open_ans)
                if open_ans == 1:
                    open_plag = input("첫번째 카드를 공개하시겠습니까? [(y), n] : ")
                elif open_ans == 2:
                    open_plag = input("두번째 카드를 공개하시겠습니까? [(y), n] : ")
                elif open_ans == 3:
                    open_plag = input("세번째 카드를 공개하시겠습니까? [(y), n] : ")
                else:
                    open_plag = input("세번째 카드를 공개하시겠습니까? [(y), n] : ")
            except:
                open_plag = input("세번째 카드를 공개하시겠습니까? [(y), n] : ")

        try:
            if int(open_ans) == 1:
                player_1.deck_pat[7] = player_1.deck_pat[0]
                player_1.deck_num[7] = player_1.deck_num[0]
            elif int(open_ans) == 2:
                player_1.deck_pat[7] = player_1.deck_pat[1]
                player_1.deck_num[7] = player_1.deck_num[1]
            elif int(open_ans) == 3:
                player_1.deck_pat[7] = player_1.deck_pat[2]
                player_1.deck_num[7] = player_1.deck_num[2]
            else:
                player_1.deck_pat[7] = player_1.deck_pat[2]
                player_1.deck_num[7] = player_1.deck_num[2]
        except:
            player_1.deck_pat[7] = player_1.deck_pat[2]
            player_1.deck_num[7] = player_1.deck_num[2]

        computer_1.deck_pat[7] = computer_1.deck_pat[1]
        computer_1.deck_num[7] = computer_1.deck_num[1]

        print("\n" * 10)
        print(f"상대방의 오픈카드 : {display_pat(computer_1.deck_pat[1])} {player_1.deck_num[7]} \n\n"
              f"오픈카드 : {display_pat(player_1.deck_pat[7])} {player_1.deck_num[7]}")
        print_deck(player_1, computer_1, "player", 3)

        input()



if __name__ == "__main__":
    main()
