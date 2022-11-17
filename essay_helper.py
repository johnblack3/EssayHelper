"""
EssayHelper is a tool used to analyze and provide feedback on a written essay.
Created by John Black
11/01/2022
"""

from collections import Counter
import os.path
import cmudict
import re

class Essay:
    """
    This class creates Essay objects and holds methods to analyze the Essay Objects
    """
    def __init__(self, essay, num_of_spaces_after_period=1):
        self.essay = self.format_essay(essay)
        self.num_of_spaces_after_period = num_of_spaces_after_period
        self.word_count = self.num_of_words()
        self.sentence_count = self.num_of_sentences()
        self.syllable_count = self.num_of_syllables()

    def __str__(self):
        return self.essay

    __repr__ = __str__

    def format_essay(self, essay):
        """Format string for ease of use."""
        e = essay.strip()
        e = e.replace("  ", " ")
        e = e.replace("\n", " ")
        return e
    
    def num_of_words(self):
        """Find the number of words."""
        num_of_words = 1
        for c in self.essay:
            if c == " ":
                num_of_words += 1
        print("Words:", num_of_words)
        return num_of_words
    
    def num_of_sentences(self):
        """Find the number of sentences. Not finished."""
        not_end_of_sentence = ["Mr", "Mrs", "Inc"] # words with trailing periods which do not denote the end of a sentece   # NEEDS WORK - add more words, fix for quotes
        num_of_sentences = 0
        position = 0
        for c in self.essay:
            if c in [".", "?", "!"]:
                if position == len(self.essay) - 1:
                    break
                elif self.essay[position + 1] == " ":
                    num_of_sentences += 1
            position += 1
        print("Sentences:", num_of_sentences)
        return num_of_sentences

    def num_of_chars(self):
        """Find the number of characters."""
        char_count = 0
        space_count = 0
        for c in self.essay:
            char_count += 1
            if c == ' ':
                space_count += 1
        print("Characters:", char_count, '\nCharacters (excluding spaces):', char_count-space_count)
        
    def start_of_sentence(self):
        """Find the number of times each word starts a sentence."""
        first_words = []
        first_words.append(self.essay[0: self.essay.find(" ")])
        position = 0
        not_end_of_sentence = ["Mr", "Mrs", "Inc"] # words with trailing periods which do not denote the end of a sentece   # NEEDS WORK - add more words, fix for quotes
        for c in self.essay:
            if c in [".", "?", "!"]:
                if position == len(self.essay) - 1:
                    break
                elif self.essay[self.essay.rfind(' ', 0, position)+1: position] in not_end_of_sentence: # don't count abbreviations as end of sentence    # NEEDS WORK
                    pass
                elif self.essay[position + 1] != " ":
                    pass
                else:
                    start = position + self.num_of_spaces_after_period + 1
                    end = self.essay.find(" ", position + self.num_of_spaces_after_period + 1)
                    if (self.essay.find(",", position + self.num_of_spaces_after_period + 1) < end and
                            self.essay.find(",", position + self.num_of_spaces_after_period + 1) > 0):
                        end = self.essay.find(",", position + self.num_of_spaces_after_period + 1)
                    first_words.append(self.essay[start:end])
            position += 1
            
        # sort the items in the first_words list by the number of occurances
        sorted_first_words = [item for items,
            c in Counter(first_words).most_common() for item in [items] * c]
        # remove duplicate words from list (sorted)
        res = []
        for i in sorted_first_words:
            if i not in res:
                res.append(i)
        
        words_and_occurs = {}
        occur = Counter(sorted_first_words)
        for item in res:
            words_and_occurs[item] = occur[item]
            print('"{}" starts {} sentences'.format(item, occur[item]))

    def word_occurances(self):
        """Find the number of times each word occurs."""
        words = []
        words.append(self.essay[0: self.essay.find(" ")].lower())
        position = 0
        for c in self.essay:
            if c == " ":
                if position == len(self.essay) - 1:
                    break
                else:
                    start = position + 1
                    end = self.essay.find(" ", position + 2)
                    words.append(self.essay[start:end].lower())
                
            position += 1
            
        # sort the items in the words list by the number of occurances
        sorted_words = [item for items,
            c in Counter(words).most_common() for item in [items] * c]
        # remove duplicate words from list (sorted)
        res = []
        for i in sorted_words:
            if i not in res:
                res.append(i)
        
        words_and_occurs = {}
        occur = Counter(sorted_words)
        for item in res:
            words_and_occurs[item] = occur[item]
            print('"{}" is used {} times'.format(item, occur[item]))
    
    def bad_phrases(self):
        """Find terms, phrases, and cliches that should be removed."""
        if os.path.exists('bad_phrases.txt'):
            with open('bad_phrases.txt') as f:
                bad_phrases = [line.lower().rstrip('\n') for line in f]
            bad_phrases_used = []

            for i in bad_phrases:
                if i in self.essay.lower(): bad_phrases_used.append(i)

            if bad_phrases_used == []:
                print("There are no terms/phrases that are recommended to be removed")
            else:
                print("Consider not using the following terms/phrases:")
                for x in bad_phrases_used: print('"' + x.capitalize() + '"')
        else:
            print("There is no list of terms/phrases to be checked for.")

        if os.path.exists('cliches.txt'):
            with open('cliches.txt') as f:
                cliches = [line.lower().rstrip('\n') for line in f]
            cliches_used = []

            for i in cliches:
                if i in self.essay.lower(): cliches_used.append(i)

            if cliches_used == []:
                print("There are no cliches that are recommended to be removed")
            else:
                print("Consider not using the following cliches:")
                for x in cliches_used: print('"' + x.capitalize() + '"')
        else:
            print("There is no list of cliches to be checked for.")

    def get_flesh_kincaid_score(self):
        reading_ease_score = 206.835 - 1.015 * (self.word_count/self.sentence_count) - 84.6 * (self.syllable_count/self.word_count)
        return reading_ease_score

    def get_syllables(self, word):
        word = word.lower()
        count = 0
        vowels = "aeiouy"
        if word[0] in vowels:
            count += 1
        for index in range(1, len(word)):
            if word[index] in vowels and word[index - 1] not in vowels:
                count += 1
        if word.endswith("e"):
            count -= 1
        if count == 0:
            count += 1

        if count != self.sylco(word):
            print(word, count, self.sylco(word))
        return count

    def num_of_syllables(self):
        total_syllables = 0
        no_punct = ""
        for c in self.essay:
            if c not in '''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~''' or c == ' ':
                no_punct += c
        for word in no_punct.split():
            total_syllables += self.get_syllables(word)
        return total_syllables


def check_essay(essay):
    
    e1 = Essay(essay)
    print('')
    e1.num_of_words()
    print('')
    e1.num_of_sentences()
    print('')
    e1.num_of_chars()
    print('')
    e1.start_of_sentence()
    print('')
    e1.word_occurances()
    print('')
    e1.bad_phrases()
    print('')
    e1.get_flesh_kincaid_score()

with open('essay.txt', 'r') as f:
    essay = f.read()

#check_essay(essay)
e1 = Essay(essay)
print('here')
print(e1.get_flesh_kincaid_score())