n =int(input("Enter you Roll number: "))
# print("your enterd roll number is: ",n)
for i in range(1,101):
  # print(i)
  while(n!=i):
    int(input("enterd correct roll number: "))
    break
else: 
  print("thanks for confirmation")