import unittest
class check_add(unittest.TestCase):
def test_add(a,b):
    c=[[0,0],
      [0,0]]
    for i in range (len(a)):
        for j in range (len(a[0])):
            c[i][j]=a[i][j]+b[i][j]
    for d in c:
        print(d)
a=[[1,2],
  [3,4]]
b=[[3,3],
  [4,4]]
add(a,b)
if __name__ == '__main__':
    unittest.main ()