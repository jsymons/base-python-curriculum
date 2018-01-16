# All in String

The function `all_in_string` receives a phrase and 3 words, and it should count how many of those words appear in the original phrase at least once. 

 Example, given the sentence from our previous assignment:

> Courage is not the absence of fear, but rather the judgement that something else is more important than fear
_(Ambrose Redmoon)_

How many of the following words you see included in that sentence: `fear`, `judgement`, `Python`? The answer is **`2`**,  because only `fear` and `judgement` are part of the original sentence. 

Examples of `all_in_string`:

```python
phrase = "Python is good. Python is Wise. I like Python"

all_in_string(phrase, 'Python', 'good', 'Ruby')  # 2
all_in_string(phrase, 'Python', 'Javascript', 'Ruby')  # 1
all_in_string(phrase, 'Python', 'Wise', 'good')  # 3
all_in_string(phrase, 'Ruby', 'Javascript', 'Perl')  # 0
```

_**Hint**: The `in` operator might be handy._
