import random

upper_alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower_alpha = upper_alpha.lower()
digit = '0123456789'
symbols = '!@#%&'

upper, lower, dig, sym = True, True, True, True
all = ''

if upper:
    all += upper_alpha
if lower:
    all += lower_alpha
if dig:
    all += digit
if sym:
    all += symbols

len = int(input("Enter the Length of the password you wanted: "))
print(''.join(random.sample(all, len)))