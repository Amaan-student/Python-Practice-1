# rollNumber = int(input("Enter your Roll Number: "))
# for i in range(1,101):
#   while(rollNumber!=i):
#     print(int(input("Enter correct roll no.: ")))
# else:
#   print("Your enterd correct roll no.")
 
#   # print(i)
# rollNumber = int(input("Enter your Roll Number: "))
# for i in range(1,101):
#   while(rollNumber>i):
#    rollNumber = int(input("Enter correct Roll Number: "))
#   else:
#     print("thanks for confirmation")
#   break
# sir logic
while True:
  roll= int(input("Enter your Roll number "))
  if roll in range(1,101):
    print("Roll number found!")
    break
else:
  print("enter correct roll number: ")