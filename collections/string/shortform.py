# Input: "National Aeronautics and Space Administration"
# O/P = NASA
# Input: "Python is a Programming Language"
# O/P = PPL

text = 'National Aeronautics and Space Administration'

# short=''
# for i in text.split():
#     if i[0].isupper():
#         short += i[0]
# print(short)

li = text.split()

result = ''.join(map(lambda word: word[0], filter(lambda word: word[0].isupper(), li)))

print(result)
