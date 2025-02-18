sentence = "hello world"
words = sentence.split()

for word in words:
    print(word[::-1],'\t',end="")

