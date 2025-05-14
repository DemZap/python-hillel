import string

text = input("Введіть рядок: ").strip()
clean_text = "".join(ch for ch in text if ch not in string.punctuation).split()
hashtag = "#" + "".join(word.capitalize() for word in clean_text)
hashtag = hashtag[:140]

print(hashtag)
pass
