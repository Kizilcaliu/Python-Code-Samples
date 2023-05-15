#Each time a number reaches an even number, raise the count by 1.
number = 11 # Test number. Try to change it to a different value.
counter = 0

# Loop, starting from 1 and going up to the value exclusive.
for i in range(1, number):
    # Condition to check if a certain criteria is met. If not do something. In this case continue the loop.
    if i % 2 == 0:
        # Raise 'counter' variable by 1 for each matching condition check, returning true.
        counter += 1
        print(counter)
    else:
        continue
    
         
        
        
    
