import numpy as np

# task 01:
print("TASK 01:")
arr = np.arange(start=1, stop=31)
arr2 = arr.reshape((6, 5))

print(f"the starting array: \n{arr2}")

print("the selected section form the task:")
print(arr2[2:4,0:2])

# task 02:
print("TASK 02:")
def is_prime(x: int):
    if x <= 1: 
        return False
    for i in range(2, int(np.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

primes_list = [x for x in range(1000) if is_prime(x)][0:50]
print(primes_list)
print(f"the size of the primes_list is {len(primes_list)}")

# TASK 03
print("TASK 03:")
arr = np.arange(start=1, stop=31)
arr2 = arr.reshape((6, 5))

print(f"the starting array: \n{arr2}")
print("the selected part is:")

print(arr2[[0,1,2,3], [1,2,3,4]])