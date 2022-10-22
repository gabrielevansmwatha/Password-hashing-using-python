#install hashlib using
#pip install hashlib
import hashlib as hs
#Get the input(password) from the user
password = input("Enter your password: ")
#hash your password using different hashing algorithms i.e sha2/3 (256,384, 512)
hashed_password = hs.sha3_384(password.encode("utf8")).hexdigest()
#print the hashed password
print(hashed_password)