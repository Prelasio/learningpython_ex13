"""
Write a password generator in Python. Be creative with how you 
generate passwords - strong passwords have a mix of lowercase 
letters, uppercase letters, numbers, and symbols. The passwords
should be random, generating a new password every time the user 
asks for a new password. Include your run-time code in a main method.
"""

import random
base = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ`,.<>!@#$%^&*()?~[]|/"
longitud = 8
contra = "".join(random.sample(base,longitud))
print(contra)