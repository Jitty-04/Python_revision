#{key:value} key->string or integer value->str,int,bool,float,lis,tuple,dict

detail = {"name":"hello","age":26,"place":"chennai"} #terable
for i in detail:
    print(i)
print(detail["name"])
print(detail.get("place"))
print(detail.get("hello")) #return None if not present
print("hello world executes successfll")

#methods
detail.update({"course":"python","fees":2000})
print(detail.items())#key value as tuple
print(detail.keys())#list of keys
print(detail.values())
print(detail.pop("fees"))#remove key an return value
