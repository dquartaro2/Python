# FILE NAME - bounded_random_number.py

# NAME:Dominick Quartaro
# DATE:September 26, 2026
# BRIEF DESCRIPTION:Bounded_random_number_lab output a random integer between 1 and 10 (inclusive)



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience

import random


########## ENTER YER CODE BELOW THIS LINE ##########


def main():
    bounded_random()

def bounded_random():
    seed = int(input("Enter a seed for the random number generation: "))
    random.seed(seed)
    print(random.randint(1,10))
    

main()


########### END YER CODE ABOVE THIS LINE ###########



########################################
#          SAMPLE OUTPUT
########################################

'''

Enter a seed for the random number generation: 33
10

'''



'''

Enter a seed for the random number generation: 32
2

'''



'''

Enter a seed for the random number generation: 100
3

'''



########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What is a good way to remember if the arguments (parameters) for a bounded number are inclusive or exclusive?
A good way to remember inclusive is that random.randint(a,b) can give both return both a and b instead of only including one.
For exclusive you have random.randrange(a, b) which allows the random number to go up to but not incclude b. 





'''
