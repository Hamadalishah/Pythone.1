from typing import List,Dict
def sum(nums:List[int],t:int)->List[int]:
    my_dict: dict = {}
    
    for i, num in enumerate(nums):
       
        diff = t - num
        if diff in my_dict:
            return [my_dict[diff],i]
        my_dict[num] = i
    return []
print(sum([2, 7, 11, 15], 9))  # Output: [0, 1]
print(sum([3, 2, 4], 6))       # Output: [1, 2]
print(sum([3, 3], 6))    
print(sum([3, 2,4,5,61,7], 64))    # Output: [0, 1]

# os.remove("data1.txt")




# def first_n_natural(n):
#     if (n==0):
#         return 0
    
#     return first_n_natural(n-1) + n
    
# n= int(input("Please enter any Number "))
# sum = first_n_natural(n)
# print(sum)










# data = filter(lambda x: x % 2 == 0, range(1, 100))

# # Use next() to get the first even number
# print(next(data))
# print(next(data))
# print(next(data))
# print(next(data))
# print(next(data))
# print(list(data))









# from typing import Callable
# add: Callable[[int, int], int] = lambda x, y : x**y
# result = add(10,20)
# print(result)
