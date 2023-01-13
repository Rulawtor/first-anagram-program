# Created by Rulawtor
# Credit to dwyl for the list of words

import json
words = json.load(open("words_dictionary.json", "r"))
ref_word = input()
not_same_word = ref_word # this is used to make sure the program doesn't just spit the same word back at you

for testWords in words:
    words_broken_down = testWords # this breaks down all the letters in a word so that the program can compare the arrays and see if they are anagrams
    words_broken_down = sorted(words_broken_down)
    ref_word = sorted(ref_word)
    
    if words_broken_down == ref_word and testWords != not_same_word: # if the array of the word being tested to be an anagram is the same as the users words array, and the word being tested is not the same as your original word, print the word being tested
        print(testWords)
    else: # else go back to the top and check the next word
        continue