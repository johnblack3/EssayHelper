import math
from essay_statistics import EssayStatistics

class EssayReadability:

    def __init__(self, text):
        self.statistics = EssayStatistics(text)

    def flesch(self):
        """Calculates Flesch reading-ease score of a text"""
        stats = self.statistics
        reading_ease_score = (206.835 - 1.015 * (stats.avg_words_per_sentence) - 
            84.6 * (stats.avg_syllables_per_word))
        return "Flesch reading-ease score: {}".format(reading_ease_score)

    def flesch_kincaid(self):
        """Calculates Flesch-Kincaid grade level of a text"""
        stats = self.statistics
        grade_level = (0.39 * (stats.avg_words_per_sentence) + 
            11.8 * (stats.avg_syllables_per_word) - 15.59)
        return "Flesch-Kincaid grade level: {}".format(grade_level)

    def ari(self):
        """Calculates automated readability index (ARI) grade level of a text"""
        stats = self.statistics
        ari_score = (4.71 * (stats.letter_count/stats.word_count) +
            0.5 * (stats.avg_words_per_sentence) - 21.43)
        return "ARI score: {}".format(ari_score)

    def gunning_fog(self):
        """Calculates Gunning Fog index score of a text"""
        stats = self.statistics
        gf_grade_level = 0.4 * (stats.avg_words_per_sentence + 100 *
            (stats.poly_syllable_word_count/stats.word_count))
        return "Gunning Fog grade level: {}".format(gf_grade_level)

    def smog(self):
        """Calculates SMOG (Simple Measure of Gobbledygook) score of a text"""
        stats = self.statistics
        if stats.sentence_count < 30:
            return "SMOG grade level: Requires 30 sentences, only {} found".format(stats.sentence_count)
        smog_grade_level = 1.0430 * math.sqrt(stats.poly_syllable_word_count *
            30 / stats.sentence_count) + 3.1291
        return "SMOG grade level: {}".format(smog_grade_level)