import unittest
class check_mul(unittest.TestCase):
def test_mul(a,b):
    c=[[0,0],
      [0,0]]
    for i in range (len(a)):
        for j in range (len(b[0])):
            for k in range(len(b)):
                c[i][j]+=a[i][j]*b[i][j]
    for d in c:
        print(d)
a=[[1,2],
  [3,4]]
b=[[3,3],
  [4,4]]
mul(a,b)
if __name__ == '__main__':
    unittest.main ()
