# Write code that will iterate through numbers from 1 to 10 and print the number if it is not equal to 5 (using continue) 
# and stop the loop entirely and print a message when it reaches 8 (using break).

for num in range(1, 10): 
    if num == 5:
        continue  
    if num == 8:
        print(f"Reached {num}, stopping the loop.")
        break  
    print(num)  

