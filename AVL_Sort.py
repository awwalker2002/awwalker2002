from Binary_Search_Tree import Binary_Search_Tree
from Fraction import Fraction

if __name__ == '__main__':
  print("This test evaluates the ability to sort an array of Fractions.")
  bst = Binary_Search_Tree()
  a = Fraction(1,2)
  b = Fraction(1,4)
  c = Fraction(1,8)
  d = Fraction(1,16)
  e = Fraction(1,32)
  f = Fraction(1,64)
  g = Fraction(1,128)
  h = Fraction(1,256)
  i = Fraction(1,512)
  j = Fraction(1,1024)

  powerfracs = [a,b,c,d,e,f,g,h,i,j]
  print(powerfracs)
  for frac in powerfracs:
    bst.insert_element(frac)

  powerfracs_sorted = bst.to_list()
  print(powerfracs_sorted)
