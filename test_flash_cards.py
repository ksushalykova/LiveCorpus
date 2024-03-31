import unittest
from parameterized import parameterized
from unittest.mock import Mock, patch, call



questions = ['яблоко', 'хурма']
answers = ['apple', 'persimmon']

answer1 = ['wrong11', 'wrong22']
answer2 = ['wrong11', 'persimmon']

wrong1 = ['Готово! Правильно 0 из 2 слов.']
wrong2 = ['Готово! Правильно 1 из 2 слов.']
right = ['Готово! Правильно 2 из 2 слов.']

possible_prints1 = questions + wrong1
possible_prints2 = questions + wrong2
possible_prints3 = questions + right



class FlashCardsTestCase(unittest.TestCase):
    
    def setUp(self):
        self.flashcards = FlashCards()

    def test_add_word_success_if_not_in(self):
        self.flashcards.add_word('test', 'test')
        self.assertEqual(self.flashcards.cards['test'], 'test')
        self.assertIn('test', self.flashcards.words)

    def test_add_word_success_if_in0(self): # без мок
        self.flashcards.add_word('test', 'test')
        self.flashcards.add_word('test', 'test')
        self.assertEqual(self.flashcards.cards['test'], 'test')

    def test_add_word_success_if_in(self): # через мок
        self.flashcards.add_word('test', 'test')
        with patch('builtins.print', Mock()) as mock_print:
            self.flashcards.add_word('test', 'test')
            self.assertEqual(self.flashcards.cards['test'], 'test')
            mock_print.assert_called_once_with('Такое слово уже есть в словаре')

    def test_add_word_wrong_type0(self): # без мок
        words_before = self.flashcards.cards.copy()
        self.flashcards.add_word(567, 789)
        self.assertEqual(self.flashcards.cards, words_before)

    def test_add_word_wrong_type(self): # через мок
        words_before = self.flashcards.cards.copy()
        with patch('builtins.print', Mock()) as mock_print:
            self.flashcards.add_word(567, 789)
            self.assertEqual(self.flashcards.cards, words_before)
            mock_print.assert_called_once_with('Неправильный тип ввода!')

    def test_delete_word_success_if_in(self):
        self.flashcards.add_word('test', 'test')
        self.flashcards.delete_word('test')
        self.assertEqual
        self.assertNotIn('test', self.flashcards.words)

    def test_delete_word_success_if_not_in0(self): # без мок
        self.flashcards.delete_word('test')
        self.assertEqual

    def test_delete_word_success_if_not_in(self): # через мок
        with patch('builtins.print', Mock()) as mock_print:
            self.flashcards.delete_word('test')
            self.assertEqual
            mock_print.assert_called_once_with('Такого слова нет в словаре')

    def test_delete_word_wrong_type0(self): # без мок
        self.flashcards.delete_word(567)
        self.assertEqual

    def test_delete_word_wrong_type(self): # через мок
        words_before = self.flashcards.cards.copy()
        with patch('builtins.print', Mock()) as mock_print:
            self.flashcards.delete_word(567)
            self.assertEqual(self.flashcards.cards, words_before)
            mock_print.assert_called_once_with('Неправильный тип ввода!')

    def test_play_no_words0(self): # без мок
        self.flashcards.cards = {}
        self.flashcards.play()
        self.assertEqual

    def test_play_no_words(self): # через мок
        self.flashcards.cards = {}
        with patch('builtins.print', Mock()) as mock_print:
            self.flashcards.play()
            self.assertEqual
            mock_print.assert_called_once_with('В словаре нет слов!')


    # правильно 0 из 2
    @patch('random.choice', Mock(side_effect = questions))

    def test_flashcards_success(self):
        
        self.flashcards.add_word('яблоко', 'apple')
        self.flashcards.add_word('хурма', 'persimmon')
        with patch('builtins.input', Mock(side_effect = answer1)):
            with patch('builtins.print', Mock()) as print_mock:
                self.flashcards.play()
            print_mock.assert_has_calls([call(arg) for arg in 
                                         possible_prints1])

            
    # правильно 1 из 2     
    @patch('random.choice', Mock(side_effect = questions))
    
    def test_flashcards_success(self):
        
        self.flashcards.add_word('яблоко', 'apple')
        self.flashcards.add_word('хурма', 'persimmon')
        with patch('builtins.input', Mock(side_effect = answer2)):
            with patch('builtins.print', Mock()) as print_mock:
                self.flashcards.play()
            print_mock.assert_has_calls([call(arg) for arg in 
                                         possible_prints2])
            
            
    # правильно 2 из 2      
    @patch('random.choice', Mock(side_effect = questions))
    
    def test_flashcards_success(self):
        
        self.flashcards.add_word('яблоко', 'apple')
        self.flashcards.add_word('хурма', 'persimmon')
        with patch('builtins.input', Mock(side_effect = answers)):
            with patch('builtins.print', Mock()) as print_mock:
                self.flashcards.play()
            print_mock.assert_has_calls([call(arg) for arg in 
                                         possible_prints3])
            
    

if __name__ == '__main__':
    unittest.main()  # если запускаем в нормальном месте
#    unittest.main(argv=['first-arg-is-ignored'], exit=False) # если запускаем в jupyter
