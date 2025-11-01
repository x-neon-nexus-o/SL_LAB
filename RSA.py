from sympy import isprime, gcd,mod_inverse

def generate_keys(p,q,e):
  if not(isprime(p) and isprime(q)):
    raise ValueError("Both numbers must be prime.")

  if p==q:
    raise ValueError("p and q cannot be equal.")

  n=p*q
  phi_n=(p-1)*(q-1)

  if gcd(e,phi_n)!=1:
    raise ValueError(f"e={e} is not co-prime with phi_n={phi_n}. Choose a different e")

  d=mod_inverse(e,phi_n)


  print(f"\n Computed Values:")
  print(f"n={n}")
  print(f"phi_n={phi_n}")
  print(f"Private Key d={d}")

  return (e,d,n)


def encrypt(message,e,n):
  return pow(message,e,n)

def decrypt(cipher,d,n):
  return pow(cipher,d,n)



# if __name__=="__main__":
 
p=int(input("Enter a prime number p: "))
q=int(input("Enter a diffferent prime number q: "))
e=int(input("Enter a public exponent e (coprime with phi_n): "))

(e,d,n)=generate_keys(p,q,e)
message=int(input("\n Enter a number message to encrypt(as integer):"))

cipher=encrypt(message,e,n)
print(f"Encrypted message: {cipher}")

decrypted=decrypt(cipher,d,n)
print(f"Decrypted message: {decrypted}")


#   except ValueError as ve:
#     print(f"Error: {ve}")