# string=input('enter the string:')
# new=''
# for i in string:
#     if string.index(i)==0 or string.index(i)==3:
#         new=new+i.upper()
#     else:
#         new+=i
# print(new)

#or
string=input('enter the string:')
print(string[0].upper()+string[1:3]+string[3].upper()+string[4:])
