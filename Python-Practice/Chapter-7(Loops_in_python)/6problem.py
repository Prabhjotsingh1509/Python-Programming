# Wap to greet all the person names in a list 'l' and which starts with S.
# l= ["Harry","Sohan","Sachin","Rahul"]
l= ["Harry","Sohan","Sachin","Rahul"]

for item in l:
    if(item.startswith("S")):
        print(f"Hello {item}")

