def count_words(a_string):
    words = a_string.split(" ")
    word_count = {}
    for word in words:
        word_count.setdefault(word, 0)
        word_count[word] += 1
    return word_count


def get_list_of_duplicates(word_count_dict):
    duplicate_list = []
    for word, count in word_count_dict.items():
        if word not in duplicate_list and count > 1:
            duplicate_list.append(word)
    duplicate_list.sort()
    return duplicate_list

string = """Alice was beginning to get very tired of sitting by her sister on the bank and of having nothing to do once or twice she had peeped into the book her sister was reading but it had no pictures or conversations in it and what is the use of a book thought Alice without pictures or conversation

So she was considering in her own mind as well as she could for the hot day made her feel very sleepy and stupid whether the pleasure of making a daisy chain would be worth the trouble of getting up and picking the daisies when suddenly a White Rabbit with pink eyes ran close by her

There was nothing so very remarkable in that nor did Alice think it so very much out of the way to hear the Rabbit say to itself Oh dear Oh dear I shall be late when she thought it over afterwards it occurred to her that she ought to have wondered at this but at the time it all seemed quite natural but when the Rabbit actually took a watch out of its waistcoat
pocket and looked at it and then hurried on Alice started to her feet for it flashed across her mind that she had never before seen a rabbit with either a waistcoat pocket or a watch to take out of it and burning with curiosity she ran across the field after it and fortunately was just in time to see it pop down a large rabbit hole under the hedge"""

print(count_words(string))
print(get_list_of_duplicates(count_words(string)))