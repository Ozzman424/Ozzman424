def main():
  number = get_number()
  meow(number)

def get_number():
  while True:
    n = int(input("What's n? "))
    if n > 0:
      break
  return n

def meow(n):
  for _ in range(n):
    print("meow") 

main()


#Old code
#i = 0
#while i < 3:
#  print("meow")
#  i += 1

#for _ in range(3):
#  print("meow")

#print("meow\n" * 3, end="")

#n = int(input("what's n? "))
#if n < 0:
#  n = input("What's n? ")
#  if n < 0:
#    n = int(input())

#while True:
#  n = int(input("What's n? "))
#  if n > 0:
#    break
#
#for _ in range(n):
#  print("meow")
