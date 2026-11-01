# FILE NAME - coin_toss.py

# NAME: Dominick Quartaro
# DATE: October 3rd, 2026
# BRIEF DESCRIPTION:Coin_Toss_Lab flip a coin from 1-100 (51 or greater is tails,otherwise it's heads.)



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience



########## ENTER YER CODE BELOW THIS LINE ##########
import random

number = random.randint(1, 100)

print("===== Coin Flipper =====")
if number >= 51:
    print("Tails")
else:
    print("Heads")








########### END YER CODE ABOVE THIS LINE ###########

    



########################################
#          SAMPLE OUTPUT
########################################
'''
===== Coin Flipper =====
Heads
'''



'''
===== Coin Flipper =====
Tails
'''


########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What was the hardest part of completing this lab? 
Remembering that I don't have to switch the randint range helped me get through this lab because since the range is in between 1-100, you can leave it as default.






'''
