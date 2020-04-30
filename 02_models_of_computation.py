# document distance

#0 read the documents
#1 Split Document into words
#2 Compute Word Frequencies in dictionary
#3 Dot Product
#3 Angle


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
        
#1
def get_list_of_words(text):
    for index,char in enumerate(text):
        if char.isalnum()  == False:
            text = text[:index] + " " + text[index+1:]
    listtext = text.split()
    return listtext

#2 
def compute_word_freq(listtext):
    dic ={}
    for word in listtext:
        word = word.lower()
        if word in dic:
            dic[word] += 1
        else:
            dic[word] = 1
    return dic
#3
def dot_product(d1,d2):
    sum = 0
    for word in d1:
        if word in d2:
            sum += d1[word]*d2[word]
    return sum

def get_number_of_words(d1,d2):
    return math.sqrt(dot_product(d1,d1)*dot_product(d2,d2))

def main():
    d1 = compute_word_freq(get_list_of_words(open_texts('Shakespear1.txt')))
    d2 = compute_word_freq(get_list_of_words(open_texts('Shakespear2.txt')))
    print(math.acos(dot_product(d1,d2)/get_number_of_words(d1, d2)))

main()


