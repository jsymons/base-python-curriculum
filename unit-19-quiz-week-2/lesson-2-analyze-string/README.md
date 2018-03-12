# Analyze String

Write a function that takes a large string, cleans it up and breaks it into individual words, counts how many times each word is used, and then returns a list of words that are repeated.

That sounds like a lot of things, so break it up into two functions and simplify the problem.

Complete the functions `count_words` so that it receives `a_string` as an input and processes the string so it becomes a list of words. Then return a dictionary with a each word in the list as a key and how many times that word is repeated (the count) as the value.

Then complete the function `get_list_of_duplicates` that receives that word count dictionary and returns a *SORTED* list of each of the items in it that are repeated more than once.

We need to sort the final list answer because dictionaries are unordered and lists are ordered, so when we are creating our list it will likely be created in a different order each run.

```python
string = """Happy Python Programming Programming Programming Happy Me"""

count_words(string) == {"Me": 1, "Python": 1, "Programming": 3, "Happy": 2}
get_list_of_duplicates({"Me": 1, "Python": 1, "Programming": 3, "Happy": 2}) == ["Happy", "Programming"]
```