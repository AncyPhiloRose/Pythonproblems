def num(list1):
    sum=0
    for i in list1:
        if (type(i)==int):
            sum=sum+i
        else:
          for j in i:
              sum=sum+j
    print(sum)
list1=[[1,2,3],4,[5,6]]
num(list1)