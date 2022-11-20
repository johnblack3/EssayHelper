# EssayHelper
EssayHelper provides feedback on written texts, including instances of repetitive language, unfavorable verbiage, and readability metric scores.

## Usage
```python
from essay_helper import EssayHelper

e = Essay(text)

e.start_of_sentence()
e.word_occurances()
e.bad_phrases()
e.flesch_kincaid()
e.flesch()
e.ari()
e.gunning_fog()
e.smog()
```