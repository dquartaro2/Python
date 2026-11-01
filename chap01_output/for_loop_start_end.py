# FILE NAME - for_loop_start_end.py

# NAME: Dominick Quartaro
# DATE: October 15th, 2026
# BRIEF DESCRIPTION:For_Loop_Start_End_Lab  



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience






########## ENTER YER CODE BELOW THIS LINE ##########

print("Starting point:")
start = int(input())
print("Ending point:")
end = int(input())

for number in range(start, end + 1):
    if number == end:
        print(number)
    else:
        print(number, end=" ")
        









########### END YER CODE ABOVE THIS LINE ###########




########################################
#          SAMPLE OUTPUT
########################################

'''
Starting point: 3
Ending point: 7
3 4 5 6 7
'''


'''
Starting point: -4
Ending point: 4
-4 -3 -2 -1 0 1 2 3 4
'''


'''
Starting point: 0
Ending point: 1
0 1
'''
