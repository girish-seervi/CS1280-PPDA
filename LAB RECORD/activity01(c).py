def find_largest():
    print("Find the largest of five numbers")
    
    nums = []  
    for i in range(1, 6):
        num = float(input(f"Enter number {i}: "))
        nums.append(num)

    largest = max(nums)  
    
    print(f"The largest number is {largest}")

find_largest()

