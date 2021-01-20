import random
import time

print("---Wanted to take decision enter the starting and ending number---")
time.sleep(2)
try:
    min_num = int(input("Enter starting Number: "))
    max_num = int(input("Enter ending Number: "))
except:
    print("Number only!!please re-run the code")
    exit()
print(random.randint(min_num, max_num))
