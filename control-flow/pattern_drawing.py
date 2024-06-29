user = int(input("Enter the size of the pattern: "))
row = 0
pat = False

while row < user:
  for pat in range(user):
    print("*", end='')
  print()
  row += 1
