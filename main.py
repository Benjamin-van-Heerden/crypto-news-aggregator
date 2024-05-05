import numpy as np

def check_a_thing():
  count = 0 
  for i in range(10):
    count += 1
    print(np.random.randint(1, 10))
  print(count)


if __name__ == "__main__":
  check_a_thing()
  print("I am here")
   
