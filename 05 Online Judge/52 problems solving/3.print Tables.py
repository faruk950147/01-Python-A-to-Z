# Bismillahir Rahmanir Rahim

count = 0 
for num in range(1000, 0, -2):  # 1000 to 2 (odd numbers)
    print(num, end="\t")  # print number with tab
    count += 1
    
    if count % 5 == 0:  # print new line after 5 numbers
        print()
   
   
'''      
n = int(input("Enter a number (n): "))  # user input
count = 0  # count for 5 numbers per line
# n to 2 (odd numbers)
for num in range(n if n % 2 == 0 else n - 1, 1, -2):  
    print(num, end="\t")  # print number with tab
    count += 1
    
    if count % 5 == 0:  # print new line after 5 numbers
        print()
'''