# example of input
# What I present here is what I remember of the letter, and what I remember of the letter I remember verbatim.

#import re allows to filter special characters
import re

sentence = input('Enter any sentence, please: ')
words = re.findall('\w+', sentence)

dictionary = {}

for word in words:
    count = dictionary.get(word.lower(), 0)
    dictionary[word.lower()] = count + 1

print(dictionary)






