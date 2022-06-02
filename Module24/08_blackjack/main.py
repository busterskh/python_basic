import random


class Card:
    def __init__(self, name, suit, rang):
        self.name = name
        self.suit = suit
        self.rang = rang

    def on_hand(self):
        return [self.name, self.suit, self.rang]


class Deck:
    name = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'В', 'Д', 'К', 'Т']
    suit = ["♠️", "♥️", "♦️", "♣️"]

    def __init__(self):
        self.card_value = self.name[random.randint(0, len(self.name) - 1)]
        self.suit = self.suit[random.randint(0, len(self.suit)) - 1]
        self.rang = 0
        if self.card_value.isdigit():
            self.rang = int(self.card_value)
        elif self.card_value == 'Т':
            self.rang = 11
        else:
            self.rang = 10

    def return_card(self):
        return Card(self.card_value, self.suit, self.rang).on_hand()


class Player:

    def __init__(self, name, card):
        self.name = name
        self.card = card

    def print_info(self):
        total_score = 0
        print(f'У {self.name} в руке: ')
        for i in self.card:
            print('-' * 10)
            print('|', '    '.join(i[:2]), end='|')
            print(('\n|' + (' ' * 8) + '|') * 2)
            print('|', '    '.join(i[1::-1]), end='|\n')
            print('-' * 10)
            if i[0] == 'Т':
                if (total_score > 21) or (total_score + i[2] > 21):
                    total_score += 1
                else:
                    total_score += i[2]
            else:
                total_score += i[2]

        print(f'\nОбщая сумма очков: {total_score}')
        return total_score


def first_move():
    card_1 = Deck().return_card()
    card_2 = Deck().return_card()
    return [card_1, card_2]


def second_move():
    user_score = user_1.print_info()
    if user_score < 21:
        more = input('Хватит или еще?\n')
        if more.lower() == 'еще':
            card_3 = Deck().return_card()
            user_1.card.append(card_3)
            second_move()
        elif more.lower() == 'хватит':
            game_over(user_score)
    elif user_score > 21:
        game_over(user_score)


def game_over(user_score):
    with open('game_history.txt', 'a') as history:
        if user_score > 21:
            print(f'\n{user_1.name} проиграл.')
            history.write(f'{user_1.name} проиграл.\n')
        else:
            diller = Player('Diller', first_move())
            diller_score = diller.print_info()
            if user_score > diller_score:
                print(f'\n{user_1.name} выиграл.')
                history.write(f'{user_1.name} выиграл.\n')
            elif user_score < diller_score:
                print(f'\n{user_1.name} проиграл.')
                history.write(f'{user_1.name} проиграл.\n')
            elif user_score == diller_score:
                print('Ничья.')
                history.write('Ничья.\n')


while True:
    menu = input('\n1. Играть'
                 '\n2. Показать историю игр'
                 '\n3. Выйти из игры\n')
    if menu == '1':
        user_1 = Player('Костя', first_move())
        second_move()

    elif menu == '2':
        with open('game_history.txt', 'r', encoding='utf=8') as history:
            print(history.read())

    elif menu == '3':
        print('\nДо новых встреч!')
        break




