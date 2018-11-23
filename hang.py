"""
This is a quick hangman game to just get the gist of classes and good programming concepts in Python
"""

import random

class hangman_check:
    def __init__(self,word):
        self.word = word
        blanks = ''
        for x in range(0,len(word)):
            blanks = blanks + '_ '
        self.blanks = blanks
        self.blankspos = [i for i,c in enumerate(blanks) if c == '_']

    def check(self,guess):
        if guess in self.word:
            gpos = [i for i,c in enumerate(self.word) if c == guess]
            for pos in gpos:
                self.blanks = self.blanks[:self.blankspos[pos]] + guess + self.blanks[self.blankspos[pos]+1:]
            return self.blanks,1
        else:
            return self.blanks,0
def main():
    words = ['kirtana','amouda','coumara','lalida','kalayarassy']
    rand = random.randint(0,4)

    hc = hangman_check(words[rand])
    print('H A N G M A N -input your letters to guess below')
    print('Blanks: ' + hc.blanks)
    count = 0
    while count < len(words[rand]):
        letter_input = input()
        if len(letter_input) != 1 or letter_input.isalpha() == False:
            print('Try Again')
            continue
        tmpword,good = hc.check(letter_input)
        print(tmpword)
        if good is 0:
            count+=1
        if tmpword.replace(' ','') == words[rand]:
            print('You Won! Congrats')
            break


if __name__ == '__main__':
    main()


