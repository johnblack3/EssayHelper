from collections import Counter    # counter to sort arrays by number of occurances
import os.path    # check for bad_phrases.txt and cliches.txt

class Essay:
    
    # constructor
    def __init__(self, essay):
        self.essay = format_essay(essay)
    
    
    # find the number of words
    def num_of_words(self): # include dash?, fix for quotes
        num_of_words = 1
        for c in self.essay:
            if c == " ":
                num_of_words += 1
        print("Words:", num_of_words)
        
    
    # find the number of sentences    # NEEDS WORK
    def num_of_sentences(self):
        not_end_of_sentence = ["Mr", "Mrs", "Inc"] # words with trailing periods which do not denote the end of a sentece   # NEEDS WORK - add more words, fix for quotes
        num_of_sentences = 0
        for c in self.essay:
            if c == "." or c == "!" or c == "?":
                num_of_sentences += 1
        print("Sentences:", num_of_sentences)
              

    # find the number of characters
    def num_of_chars(self):
        char_count = 0
        space_count = 0
        for c in self.essay:
            char_count += 1
            if c == ' ':
                space_count += 1

        print("Characters:", char_count, '\nCharacters (excluding spaces)', char_count-space_count)
        
        
    # find the number of times each word starts a sentence
    def start_of_sentence(self):
        # declare and initialize variables
        first_words = []
        first_words.append(self.essay[0: self.essay.find(" ")]) # add first word in string (position 0 to first space)
        position = 0 # position counter for string loop
        not_end_of_sentence = ["Mr", "Mrs", "Inc"] # words with trailing periods which do not denote the end of a sentece   # NEEDS WORK - add more words, fix for quotes

        # loop through string, 
        for c in self.essay:
            if c == ".":
                if position == len(self.essay) - 1: # don't count the last period
                    break
                elif self.essay[self.essay.rfind(' ', 0, position)+1: position] in not_end_of_sentence: # don't count abbreviations as end of sentence    # NEEDS WORK
                    pass
                else: # find the first space (or comma) after the space directly after the period
                    start = position + 2
                    end = self.essay.find(" ", position + 2)
                    if self.essay.find(",", position + 2) < end and self.essay.find(",", position + 2) > 0: # if a comma comes before the first space, use the comma as the end of the word    # Efficieny?
                            end = self.essay.find(",", position + 2)
                    first_words.append(self.essay[start:end])
                
            position += 1  # position in string counter
            
        # sort the items in the first_words list by the number of occurances
        sorted_first_words = [item for items, c in Counter(first_words).most_common() for item in [items] * c]
        
        # remove duplicate words from list (sorted)
        res = []
        for i in sorted_first_words:
            if i not in res:
                res.append(i)
        
        # find the number of occurances of each word
        words_and_occurs = {} # dictionary to store words and number of occurances
        
        occur = Counter(sorted_first_words)
        for item in res:
            words_and_occurs[item] = occur[item] # add items to dictionary
            print('"{}" starts {} sentences'.format(item, occur[item])) # print how many times each word occurs
            

    # find the number of times each word occurs
    def word_occurances(self):
        # declare and initialize varaibles
        words = []
        words.append(self.essay[0: self.essay.find(" ")].lower())
        position = 0
        
        for c in self.essay:
            if c == " ":
                if position == len(self.essay) - 1: # don't count the last period
                    break
                else: # find the first space after the space directly after the period
                    start = position + 1
                    end = self.essay.find(" ", position + 2)
                    words.append(self.essay[start:end].lower())
                
            # position in string counter
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

    
    # check for terms, phrases, and cliches that should be removed
    def bad_phrases(self):
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
        

# format string for ease of use
def format_essay(essay):
    # remove white spaces from beginning and end
    e = essay.strip()
    
    # double spaces -> single space
    e = e.replace("  ", " ")
    
    # return formatted essay
    return e


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