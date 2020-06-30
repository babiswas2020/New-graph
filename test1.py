class A:
  def __init__(self,a):
      self.a=a
  def __iter__(self):
     self.b=0
     return self
  def __next__(self):
     item=0
     if self.b>self.a:
        raise StopIteration
     else:
        item=self.b
        self.b=self.b+1
        return item

if __name__=="__main__":
   a=A(10)
   iter(a)
   print(next(a))
   print(next(a))
   print(next(a))
   print(next(a))
   print(next(a))
   print(next(a))
   print(next(a))



     