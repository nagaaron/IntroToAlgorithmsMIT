# document distance

#0 read the documents
#1 Split Document into words
#2 Compute Word Frequencies in dictionary
#3 Dot Product and angle


import math
import string
import sys

#0
def open_texts(filename):
    t = open(filename,'r')
    try:
        text = t.read()
        return text
    except IOError:
        print ("Error opening or reading input file: ",filename)
        sys.exit()
        
translation_table = string.maketrans(string.punctuation+string.uppercase," "*len(string.punctuation)+string.lowercase)

#1
def get_list_of_words(text):
    text = text.translate(translation_table)
    word_list = text.split()
    return word_list


def main():
    
    print(get_list_of_words(open_texts('Shakespear1.txt')))

main()


