# FILE NAME - random_seeded_number.py

# NAME:Dominick Quartaro
# DATE:September 26, 2026
# BRIEF DESCRIPTION:Random_seeded_number_lab 



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience

import random


########## ENTER YER CODE BELOW THIS LINE ##########


def main():
    generate_seeded_random_number()

def generate_seeded_random_number():
    ## TODO: Replace the code below with your code
    seed = int(input("Enter a seed for the random number generation: "))
    random.seed(seed)
    print(random.random())


main()


########### END YER CODE ABOVE THIS LINE ###########



########################################
#          SAMPLE OUTPUT
########################################

'''

Enter a seed for the random number generation: 33
0.5703284231368732

'''



'''

Enter a seed for the random number generation: 0
0.8444218515250481

'''



'''

Enter a seed for the random number generation: 10
0.5714025946899135

'''



########################################
#          REFLECTION QUESTIONS
########################################

'''

1. In your own words, explain what "seeded" means (for instance, "seeding a random number generator").

Seeding in my own words for this lab means giving the random number generator a starting value allowing it to have a sequence of predictable numbers.
Without the seeds the numbers would be different each time the program was ran.





'''
