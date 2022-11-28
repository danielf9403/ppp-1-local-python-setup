def hello():
  print("Hello, I don't know how work!")
  
def pack(wine,vodka,gin):
  return [wine,vodka,gin]


def eat_lunch(my_lst):
  if len(my_lst) == 0:
    print("My lunchbox is empty!")
  else:
    for i in range(len(my_lst)):
      if i == 0:
        print(f"First I eat {my_lst[0]}")
      else:
        print(f"Next I eat {my_lst[i]}")

hello()
print(pack(wine,vodka,gin))
print(pack(1,2,3))
eat_lunch([])
eat_lunch(["sandwich"])
eat_lunch(["apple","banana","sandwich","cookie"])

# I don't think is working everytime when I run on terminal python_setup.py I get errors this "NameError: name 'python_setup' is not defined"