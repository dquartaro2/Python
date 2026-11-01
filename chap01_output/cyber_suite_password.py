# FILE NAME - cyber_suite_password.py

# NAME:Dominick Quartaro
# DATE:September 26, 2026
# BRIEF DESCRIPTION:Cyber_suite_password Project generating random password with specific format



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience

import random
import string


########## ENTER YER CODE BELOW THIS LINE ##########


def main():
    generate_password()

def generate_password():
    seed = int(input("Enter a seed for the random number generation: "))
    random.seed(seed)

    special = "!@#$&(),-_"

    password = (
        random.choice(special) +
        random.choice(string.ascii_lowercase) +
        random.choice(string.ascii_uppercase) +
        random.choice(string.ascii_lowercase) +
        random.choice(string.ascii_uppercase) +
        random.choice(string.digits) +
        random.choice(string.digits) +
        random.choice(special)
    )

    print("Your random password is:")
    print(password)
    

main()


########### END YER CODE ABOVE THIS LINE ###########



########################################
#          SAMPLE OUTPUT
########################################

'''

Enter a seed for the random number generation: 33
Your random password is:
_fUhI78-

'''



'''

Enter a seed for the random number generation: 22
Your random password is:
#hAtO21(

'''



'''

Enter a seed for the random number generation: 0
Your random password is:
)yNbI87)

'''



########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What was the hardest part of completing this lab?
The hardest part of this project for me was making sure all of the parenthesis and brackets were placed in the correct spot.
The last closing parenthesis after the password coding was the hardest part for me especially and took me some time.





2. What value do you see in the `string` module?
The value I see in the string module is it helps my code have a cleaner and better understanding to read. It made coding this project simplier and less likely to make errors compared to typing in each individual password.





'''
