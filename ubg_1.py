import sys
import copy
from collections import Counter
from string import ascii_lowercase
from spellchecker import SpellChecker

CIPHER_LETTERS = 'nzghqkcdmyfoialxevtswrupjb'
ALPHABET = "abcdefghijklmnopqrstuvwxyz"
ALPHADICT = {x:0 for x in ALPHABET}
BY_FREQ = "etaoinshrdlcumwfgypbvkjxqz"

def main():
    fl = list(get_encoded_text())
    

    # determine frequency of each letter in the file
    freq_dict = letter_freq_file(fl)

    #create alphabet sorted by frequency of occurence in the file.
    alphabet_by_freq = sorted(freq_dict,
                                key = lambda x: freq_dict[x],
                                reverse=True)

    # print substituted version of the file
    for line in fl:
        print(substitute(line, alphabet_by_freq))

def get_encoded_text():
    input_text = input('Text to cipher: ')
    encoded_text = encode(input_text.lower())
    print(encoded_text)
    file = open('ciphertext.txt', 'w')
    file.write(encoded_text)
    file.close()
    print('Encoded text saved to file.')
    
    return encoded_text

def letter_freq(s, freq_dict):
    for letter in s:
        if letter.lower() in ALPHABET:
            freq_dict[letter.lower()] += 1

# takes a list of strings and returns a dict
# containing the frequency of every character
def letter_freq_file(string_list):
    freq_dict = copy.deepcopy(ALPHADICT)
    for s in string_list:
        letter_freq(s, freq_dict)

    return freq_dict

def alpha_position(letter):
    return ALPHABET.index(letter.lower()) + 1

def substitute(string, alphabet_by_freq):
    ret = ''
    for letter in string:
        if letter.lower() in ALPHABET:
            ret += alphabet_by_freq[alpha_position(letter)-1]
        else:
            ret += letter
    return ret

def is_word(s):
    # test whether a string is in a dictionary.
    spell = SpellChecker()
    misspelled = spell.unknown([s])
    return len(misspelled) == 0

def is_decoded(sl):
    new_sl = []
    for s in sl:
        s = s.strip().split(" ")
        new_sl.append(s)

    # new_sl is now a list of lists of words
    # check randomly chosen words to appear in a dictionary or not
    word_count = 0
    for i in range(10):
        if is_word(random.choice(random.choice(new_sl))):
            word_count += 1

    if word_count >= 3: #TODO find a good number to require to be in dictionary. Inherently involves a degree of uncertainty
        return True
    else:
        return False

def ngrams(word, n):
    if n>len(word):
        return
    for i in range(len(word)-n+1):
        yield word[i:i+n]

def count_ngrams(s, n):
    counter = Counter()
    for word in s.split():
        for ngram in ngrams(word, n):
            counter[ngram] += 1
    return counter
    
def encode(text):
    trans = str.maketrans(ascii_lowercase, CIPHER_LETTERS)
    return text.translate(trans)
    

main()