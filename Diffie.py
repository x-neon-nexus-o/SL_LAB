from sympy import *

def diffie(n,g,x,y):
  if (isprime(n)==False):
    print("Not a prime number")
  else:
    A=pow(g,x)%n
    print("The value of Alice is",A)
    B=pow(g,y)%n
    print("The value of Bob is",B)

    k1=pow(B,x)%n
    print("The computed secret key for Alice is",k1)
    k2=pow(A,y)%n
    print("The computed secret key for Alice is",k2)
    if k1==k2:
      print("The key exchange is successful",k1)
    else:
      print("The key exchange is unsuccessful")

n=int(input("Enter the prime number "))
g=int(input("Enter the primitive root "))
x=int(input("Enter the private key for Alice "))
y=int(input("Enter the private key for Bob "))

diffie(n,g,x,y)