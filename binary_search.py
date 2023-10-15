import time 
#python decorators 
def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time() 
        print(func.__name__ +" took " + str((end-start)*1000)+" ms")
        return result 
    return wrapper

@time_it
def linear_search(list, target_number):
    for idx, element in enumerate(list):
        if element == target_number:
            return idx 

@time_it
def binary_search(list, target_number):
    left_index = 0 
    right_index = len(list) - 1
    mid_index = 0 
    while left_index < right_index: 
        mid_index = (left_index + right_index) // 2 #double slash forms floor division
        mid_number = list[mid_index]
        
        if mid_number == target_number:
            return mid_index 
        
        # review 
        if mid_number < target_number:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1 
        
    return -1 #if nothing is found

#no loop solution 
def recursive_binary_search(list, target_number, left_index, right_index):
    if right_index < left_index:
        return -1 
    
    mid_index = (left_index + right_index) // 2 #double slash forms floor division
    mid_number = list[mid_index]
    
    if mid_number == target_number:
        return mid_index 
    
    # review 
    if mid_number < target_number:
        left_index = mid_index + 1
    else:
        right_index = mid_index - 1 
    
    recursive_binary_search(list, target_number, left_index, right_index)

if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5, 6, 7, 8]
    target_number = 10
    
    index = binary_search(numbers, target_number)
    print(index)