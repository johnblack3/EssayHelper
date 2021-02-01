from collections import Counter    # counter to sort arrays by number of occurances

john_essay = """In the novel, the Younger family experiences intense discrimination. The cruelty imposed by society has negative effects on the family, who despite this, all still have dreams about a better life with lesser suffering. In my opintion, Raisin in the Sun is terrible. I don't like it"""
#           ^    ^    ^    ^    ^    ^    ^    ^    ^    ^    ^    ^    ^    ^    ^    ^    ^
#position:  0    5    10   15   20   25   30   35   40   45   50   55   60   65   70   75   80


class Essay():
    # find the number of words
    def num_of_words(self, essay):
        num_of_words = 1
        for c in essay:
            if c == " ":
                num_of_words += 1
        print("Words:", num_of_words)
        
    
    # find the number of sentences    # NEEDS WORK
    def num_of_sentences(self, essay):
        num_of_sentences = 0
        for c in essay:
            if c == "." or c == "!" or c == "?":
                num_of_sentences += 1
        print("Sentences:", num_of_sentences)
              

    # find the number of characters
    def num_of_chars(self, essay):
        num_of_chars = 0
        for c in essay:
            num_of_chars += 1
        print("Characters:", num_of_chars)
        
        
    # find the number of times each word starts a sentence
    def start_of_sentence(self, essay):
        # declare and initialize varaibles
        first_words = []
        first_words.append(essay[0: essay.find(" ")]) # add first word in string (position 0 to first space)
        position = 0 # position counter for string loop
        not_end_of_sentence = [" Mr", "Mrs", "Inc"] # words with trailing periods which do not denote the end of a sentece   # NEEDS WORK
        
        for c in essay:
            if c == ".":
                if position == len(essay) - 1: # don't count the last period
                    break
                elif essay[position - 3: position] in not_end_of_sentence: # don't count Mr, Mrs, etc. as end of sentence    # NEEDS WORK
                    pass
                else: # find the first space (or comma) after the space directly after the period
                    start = position + 2
                    end = essay.find(" ", position + 2)
                    if essay.find(",", position + 2) < end and essay.find(",", position + 2) > 0: # if a comma comes before the first space, use the comma as the end of the word    # Efficieny?
                            end = essay.find(",", position + 2)
                    first_words.append(essay[start:end])
                
            # position in string counter
            position += 1
            
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
    def word_occurances(self, essay):
        # declare and initialize varaibles
        words = []
        words.append(essay[0: essay.find(" ")].lower())
        position = 0
        
        for c in essay:
            if c == " ":
                if position == len(essay) - 1: # don't count the last period
                    break
                else: # find the first space after the space directly after the period
                    start = position + 1
                    end = essay.find(" ", position + 2)
                    words.append(essay[start:end].lower())
                
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
            
    

# format string for ease of use
def format_essay(essay):
    # remove white spaces from beginning and end
    essay = essay.strip()
    
    # double spaces -> single space
    essay = essay.replace("  ", " ")
    
    # return formatted essay
    return essay


def check_essay():
    
    essay_to_check = john_essay
    essay_to_check = format_essay(essay_to_check)
    
    essay = Essay()
    print('')
    essay.num_of_words(essay_to_check)
    print('')
    essay.num_of_sentences(essay_to_check)
    print('')
    essay.num_of_chars(essay_to_check)
    print('')
    essay.start_of_sentence(essay_to_check)
    print('')
    essay.word_occurances(essay_to_check)
    
    
check_essay()