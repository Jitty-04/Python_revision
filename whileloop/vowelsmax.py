sentence=input("enter the sentence").strip()
words=sentence.split()

max_vowels=0
word_max=""
for word in words:
    count=0
    for ch in word:
        if ch in 'aeiouAEIOU':
            count+=1
    if count > max_vowels:
        max_vowels=count
        word_max=word
print(word_max)