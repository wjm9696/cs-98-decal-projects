dictionary = {'A': '.-',     'B': '-...',   'C': '-.-.', 

      'D': '-..',    'E': '.',      'F': '..-.',
      'G': '--.',    'H': '....',   'I': '..',
      'J': '.---',   'K': '-.-',    'L': '.-..',
      'M': '--',     'N': '-.',     'O': '---',
      'P': '.--.',   'Q': '--.-',   'R': '.-.',
      'S': '...',    'T': '-',      'U': '..-',
      'V': '...-',   'W': '.--',    'X': '-..-',
      'Y': '-.--',   'Z': '--..',

       

      '0': '-----',  '1': '.----',  '2': '..---',

      '3': '...--',  '4': '....-',  '5': '.....',

      '6': '-....',  '7': '--...',  '8': '---..',

      '9': '----.'}

def return_code(word):

        string=dictionary[word[0]]
        word=word[1:]
        while word:
                if word[0]==" ":
                        word=word[1:]
                string=string+" "+dictionary[word[0]]
                word=word[1:]
        return string

def main2():
  word = input("what to encrypt? ").upper()
  print(return_code(word))





     