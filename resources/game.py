from resources.words import get_word


class GameHandler:
    @classmethod
    def new_game(cls):
        game = {}
        game['word_info'], game['answer'], game['hint'] = get_word()
        game['word_length'] = len(game['answer'])
        game['entry'] = ['_' for i in range(game['word_length'])]
        game['lives'] = game['word_length'] // 2
        game['level'] = 0
        game['total_scores'] = 0
        game['is_new_game'] = True

        return game

    @classmethod
    def enter_char(cls, ch, game):
        game['is_new_game'] = False
        if ch not in game['word_info']:
            game['lives'] -= 1
            return False
        for i in game['word_info'][ch]: game['entry'][i] = ch
        game['total_scores'] += len(game['word_info'][ch])
        del game['word_info'][ch]
        return True

    @classmethod
    def level_passed(cls, game):
        return bool(not game['word_info'])

    @classmethod
    def is_game_over(cls, game):
        return bool(game['lives'] <= 0)

    @classmethod
    def next_level(cls, game):
        game['level'] += 1
        game['word_info'], game['answer'], game['hint'] = get_word()
        game['word_length'] = len(game['answer'])
        game['entry'] = ['_' for i in range(game['word_length'])]
        game['lives'] = game['word_length']//2



class Game:
    def __init__(self):
        self.word_info, self.answer, self.hint = get_word()
        self.word_length = len(self.answer)
        self.entry = [' ' for i in range(self.word_length)]
        self.level = 0
        self.lives = self.word_length//2
        self.total_scores = 0

    def enter_char(self, ch):
        if ch not in self.word_info:
            self.lives -= 1
            return False
        for i in self.word_info[ch]: self.entry[i] = ch
        self.total_scores += len(self.word_info[ch])
        del self.word_info[ch]
        return True

    def level_passed(self):
        return bool(not self.word_info)

    def is_game_over(self):
        return bool(self.lives == 0)

    def next_level(self):
        self.level += 1
        self.word_info, self.answer, self.hint = get_word()
        self.word_length = len(self.answer)
        self.entry = [' ' for i in range(self.word_length)]
        self.lives = self.word_length // 2

    def get_entry(self):
        return ''.join(self.entry)








