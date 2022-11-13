'''
EssayHelper is a tool used to analyze and provide feedback on a written essay.
Created by John Black
11/01/2022
'''

from collections import Counter    # counter to sort arrays by number of occurances
import os.path    # check for bad_phrases.txt and cliches.txt

class Essay:
    
    def __init__(self, essay):
        self.essay = self.format_essay(essay)

    def format_essay(self, essay):
        """Format string for ease of use."""
        e = essay.strip()
        e = e.replace("  ", " ")
        return e
    
    def num_of_words(self):
        """Find the number of words."""
        num_of_words = 1
        for c in self.essay:
            if c == " ":
                num_of_words += 1
        print("Words:", num_of_words)
    
    def num_of_sentences(self):
        """Find the number of sentences. Not finished."""
        not_end_of_sentence = ["Mr", "Mrs", "Inc"] # words with trailing periods which do not denote the end of a sentece   # NEEDS WORK - add more words, fix for quotes
        num_of_sentences = 0
        for c in self.essay:
            if c == "." or c == "!" or c == "?":
                num_of_sentences += 1
        print("Sentences:", num_of_sentences)

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
        first_words.append(self.essay[0: self.essay.find(" ")]) # add first word in string (position 0 to first space)
        position = 0
        not_end_of_sentence = ["Mr", "Mrs", "Inc"] # words with trailing periods which do not denote the end of a sentece   # NEEDS WORK - add more words, fix for quotes

        for c in self.essay:
            if c == ".":
                if position == len(self.essay) - 1:
                    break
                elif self.essay[self.essay.rfind(' ', 0, position)+1: position] in not_end_of_sentence: # don't count abbreviations as end of sentence    # NEEDS WORK
                    pass
                else: # find the first space (or comma) after the space directly after the period
                    start = position + 2
                    end = self.essay.find(" ", position + 2)
                    if self.essay.find(",", position + 2) < end and self.essay.find(",", position + 2) > 0: # if a comma comes before the first space, use the comma as the end of the word    # Efficieny?
                            end = self.essay.find(",", position + 2)
                    first_words.append(self.essay[start:end])
                
            position += 1
            
        # sort the items in the first_words list by the number of occurances
        sorted_first_words = [item for items, c in Counter(first_words).most_common() for item in [items] * c]
        # remove duplicate words from list (sorted)
        res = []
        for i in sorted_first_words:
            if i not in res:
                res.append(i)
        
        # find the number of occurances of each word
        words_and_occurs = {}
        
        occur = Counter(sorted_first_words)
        for item in res:
            words_and_occurs[item] = occur[item] # add items to dictionary
            print('"{}" starts {} sentences'.format(item, occur[item])) # print how many times each word occurs

    def word_occurances(self):
        """Find the number of times each word occurs."""
        words = []
        words.append(self.essay[0: self.essay.find(" ")].lower())
        position = 0
        for c in self.essay:
            if c == " ":
                if position == len(self.essay) - 1:
                    break
                else: # find the first space after the space directly after the period
                    start = position + 1
                    end = self.essay.find(" ", position + 2)
                    words.append(self.essay[start:end].lower())
                
            position += 1
            
        # sort the items in the words list by the number of occurances
        sorted_words = [item for items, c in Counter(words).most_common() for item in [items] * c]
        # remove duplicate words from list (sorted)
        res = []
        for i in sorted_words:
            if i not in res:
                res.append(i)
        
        # find the number of occurances of each word
        words_and_occurs = {} # dictionary to store words and number of occurances
        occur = Counter(sorted_words)
        for item in res:
            words_and_occurs[item] = occur[item] # add items to dictionary
            print('"{}" is used {} times'.format(item, occur[item])) # print how many times each word occurs
    
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

with open('essay.txt', 'r') as f:
    essay = f.read()

check_essay(essay)