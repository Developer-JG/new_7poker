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

def shuffle(computer_1, player_1):
    while True:
        for i in range(0,7):
            player_1.deck_num.append(randint(1, 13))
            player_1.deck_pat.append(randint(1, 4))
            computer_1.deck_num.append(randint(1, 13))
            computer_1.deck_pat.append(randint(1, 4))

        for j in range(0, 7):
            player_1.deck.append((player_1.deck_pat[j] * 100) + (player_1.deck_num[j]))
            computer_1.deck.append((computer_1.deck_pat[j] * 100) + (computer_1.deck_num[j]))

        deck = player_1.deck + computer_1.deck

        if len(list(set(deck))) == 14:
            break
        else:
            computer_1 = Player([], [], [])
            player_1 = Player([], [], [])

def main():
    computer_1 = Player([], [], [])
    player_1 = Player([], [], [])

    shuffle(computer_1, player_1)

    print(player_1.deck)

if __name__ == "__main__":
    main()
