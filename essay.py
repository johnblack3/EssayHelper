"""
EssayHelper is a tool used to analyze and provide feedback on a written essay.
Created by John Black
11/01/2022
"""

from collections import Counter
import os.path
from essay_statistics import EssayStatistics

class Essay:
    """
    This class creates Essay objects and holds methods to analyze the Essay Objects
    """
    def __init__(self, essay, num_of_spaces_after_period=1):
        self.essay = self.format_essay(essay)
        self.statistics = EssayStatistics(self.essay)
        self.num_of_spaces_after_period = num_of_spaces_after_period

    def __str__(self):
        return self.essay

    __repr__ = __str__

    def format_essay(self, essay):
        """Format string for ease of use."""
        e = essay.strip()
        e = e.replace("  ", " ")
        e = e.replace("\n", " ")
        return e
        
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
        if os.path.exists('texts/bad_phrases.txt'):
            with open('texts/bad_phrases.txt') as f:
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

        if os.path.exists('texts/cliches.txt'):
            with open('texts/cliches.txt') as f:
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
        stats = self.statistics
        print(stats.word_count, stats.sentence_count, stats.syllable_count)
        print(stats.avg_words_per_sentence, stats.word_count/stats.sentence_count)
        print(stats.avg_syllables_per_sentence, stats.syllable_count/stats.sentence_count)
        reading_ease_score = 206.835 - 1.015 * (stats.word_count/stats.sentence_count) - 84.6 * (stats.syllable_count/stats.sentence_count)
        return reading_ease_score


def check_essay(essay):
    
    e1 = Essay(essay)
    print('')
    print("Word Count:", e1.statistics.word_count)
    print('')
    print("Sentence Count:", e1.statistics.sentence_count)
    print('')
    print("Character Count:", e1.statistics.char_count)
    print('')
    print("Character Count Without Spaces:", e1.statistics.char_count_without_spaces)
    print('')
    print("Syllable Count:", e1.statistics.syllable_count)
    print('')
    e1.start_of_sentence()
    print('')
    e1.word_occurances()
    print('')
    e1.bad_phrases()

with open('texts/essay.txt', 'r') as f:
    essay = f.read()

check_essay(essay)
e1 = Essay(essay)