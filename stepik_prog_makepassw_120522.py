import random

class Psw:
    def __init__(self, digits, low_let, up_let, punc, char):
        self.digits = digits
        self.low_let = low_let
        self.up_let = up_let
        self.punc = punc
        self.char = char

    def req_user(self):
        num_pas = input('Количество паролей для генерации: ')
        len_pas = input('Длина одного пароля: ')
        dig_pas = input('Включать ли цифры "0123456789"? (Y/N) ')
        ul_pas = input('Включать ли прописные буквы "ABCDEFGHIJKLMNOPQRSTUVWXYZ"? (Y/N) ')
        ll_pas = input('Включать ли строчные буквы "abcdefghijklmnopqrstuvwxyz"? (Y/N) ')
        sym_pass = input('Включать ли символы "!#$%&*+-=?@^_"? (Y/N) ')
        troubsymb_pass = input('Исключать ли неоднозначные символы "il1Lo0O"? (Y/N) ')

        # digits = '0123456789'
        # lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
        # uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        # punctuation = '!#$%&*+-=?@^_'


if __name__ == '__main__':
    Psw.req_user(Psw)








