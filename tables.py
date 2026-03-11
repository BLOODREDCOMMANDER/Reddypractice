# Program to print the multiplication table of a given number
a = int(input("enter a number"));
for i in range (1,21):
  print(a,"x",i,"=",a*i);
for j in range(1,21):
  if j%2==0:
    print(a,"x",j,"=",a*j);

