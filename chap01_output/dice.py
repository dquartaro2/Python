# FILE NAME - dice.py

# NAME:Dominick Quartaro
# DATE:Septemmber 26, 2026
# BRIEF DESCRIPTION:Dice_Lab simulate rolling dice 



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience

import random


########## ENTER YER CODE BELOW THIS LINE ##########


def main():
    roll_die()

def roll_die():
    seed = int(input("Enter a seed for the random number generation: "))
    random.seed(seed)
    print("Die roll one is", random.randint(1, 6))
    print("Die roll two is", random.randint(1, 6))



main()


########### END YER CODE ABOVE THIS LINE ###########



########################################
#          SAMPLE OUTPUT
########################################

'''

Enter a seed for the random number generation: 33
Die roll one is 5
Die roll two is 2

'''



'''

Enter a seed for the random number generation: 22
Die roll one is 2
Die roll two is 2

'''



'''

Enter a seed for the random number generation: -30
Die roll one is 5
Die roll two is 3

'''



########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What is the purpose of "seeding" the random number generator?

The purpose of seeding the random number generator is to make the sequence of random numbers predictable and repreatable.
Using the same seed will always get the same sequence of numbers.




'''
