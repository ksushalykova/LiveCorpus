import random

class FlashCards():
    def __init__(self):
        self.cards = {} 
        
        self.words = []
        for key in self.cards.keys():
            self.words.append(key)
        pass

    def play(self):

        if len(self.cards.keys()) == 0:
            
            print('В словаре нет слов!')

        else:

            i = 0
            for n in range(len(self.cards.keys())):
                word = random.choice(self.cards.keys())
                print(word)
                answer = input().lower()
                if answer == self.cards[word]:
                  i+=1

            print('Готово! Правильно {} из {} слов.'.format(i, len(self.cards.keys())))


        
    def add_word(self, russian: str, english: str):

        if not isinstance(russian, str) or not isinstance(english, str):
            print('Неправильный тип ввода!')
            return
        
        if russian in list(self.cards.keys()):
            print('Такое слово уже есть в словаре')

        else:
            self.cards[russian] = english
            self.words.append(russian)
            print('Добавлено слово', russian)

        
    def delete_word(self, russian: str):

        if not isinstance(russian, str):
            print('Неправильный тип ввода!')
            return
        
        if russian in list(self.cards.keys()):
            del self.cards[russian]
            self.words.remove(russian)
            print('Удалено слово', russian)
        
        else:
            print ('Такого слова нет в словаре')
