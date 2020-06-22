str1="aBcDEFz"
str2=""
for i in (str1):
    if i.upper()==i:
       i=i.lower()
    else:
        i=i.upper()
    str2=str2+i
print(str1+" "+str2)