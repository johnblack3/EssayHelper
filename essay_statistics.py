class EssayStatistics:
    
    def __init__(self, text):
        self.essay = text
    
    @property
    def word_count(self):
        """Find the number of words."""
        num_of_words = 1
        for c in self.essay:
            if c == " ":
                num_of_words += 1
        #print("Words:", num_of_words)
        return num_of_words

    @property
    def sentence_count(self):
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
        #print("Sentences:", num_of_sentences)
        return num_of_sentences

    def get_char_count(self):
        """Find the number of characters."""
        char_count = 0
        space_count = 0
        for c in self.essay:
            char_count += 1
            if c == ' ':
                space_count += 1
        return char_count, char_count - space_count
        #print("Characters:", char_count, '\nCharacters (excluding spaces):', char_count-space_count)

    @property
    def char_count(self):
        return self.get_char_count()[0]

    @property
    def char_count_without_spaces(self):
        return self.get_char_count()[1]

    def get_syllables(self, word):
        """Find the number of syllables in a word"""
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
        return count

    @property
    def syllable_count(self):
        """Find the number of syllables in the entire text"""
        total_syllables = 0
        no_punct = ""
        for c in self.essay:
            if c not in '''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~''' or c == ' ':
                no_punct += c
        for word in no_punct.split():
            total_syllables += self.get_syllables(word)
        return total_syllables

    @property
    def avg_words_per_sentence(self):
        return self.word_count/self.sentence_count

    @property
    def avg_syllables_per_sentence(self):
        return self.syllable_count/self.sentence_count

    def get_statistics(self):
        return {
            "word_count": self.word_count,
            "sentence_count": self.sentence_count,
            "char_count": self.char_count,
            "char_count_without_spaces": self.char_count_without_spaces,
            "syllable_count": self.syllable_count,
            "avg_words_per_setence": self.avg_words_per_sentence,
            "avg_syllables_per_setence": self.avg_syllables_per_sentence,
        }