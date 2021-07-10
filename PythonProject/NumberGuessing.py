import random
rand_num = random.randint(1,100)

user_value = int(input("Please enter a number: \n"))

if isinstance(user_value, int) == True:
    print(user_value, rand_num)
    while user_value != rand_num:
        if user_value < rand_num:
            user_value = int(input("Your value is inferior than the guess number, Please enter another number: \n"))
        else:
            user_value = int(input("Your value is superior than the guess number, Please enter another number: \n"))
        
    print("Congratulations, you made it!!!!!!!!!!!!!")
else:
    raise TypeError("YOu should Enter a number")