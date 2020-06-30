def decorator(func):
   print("Decorator executed")
   def wrapper(*args):
      print("Executing Wrapper")
      return func(*args)
   return wrapper

@decorator
def func(*args):
   for obj in args:
      print(obj)

if __name__=="__main__":
   func("hello","mello","Bello")