# FILE NAME - grade_converter.py

# NAME: Dominick Quartaro
# DATE: October 3rd, 2026
# BRIEF DESCRIPTION: Grade_Converter_lab 



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience



########## ENTER YER CODE BELOW THIS LINE ##########

print("===== Grade Converter =====")
print("Enter a numerical grade (1-100):")
grade = float(input())

if grade > 100:
    print("A+")   
else:
    if grade >= 90:
        print("A")
    else:
        if grade >= 80:
            print("B")
        else:
            if grade >= 70:
                print("C")
            else:
                if grade >= 65:
                    print("D")
                else:
                    print("F")
            
          








########### END YER CODE ABOVE THIS LINE ###########

    



########################################
#          SAMPLE OUTPUT
########################################

'''
===== Grade Converter =====
Enter a numerical grade (1-100): 101
A+
'''


'''
===== Grade Converter =====
Enter a numerical grade (1-100): -78
F
'''


'''
===== Grade Converter =====
Enter a numerical grade (1-100): 64
F
'''


'''
===== Grade Converter =====
Enter a numerical grade (1-100): 65
D
'''


'''
===== Grade Converter =====
Enter a numerical grade (1-100): 66
D
'''

########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What is something you would tell a future student to be careful about when
   doing this lab?

Be very careful with making sure you have proper spacing and indentation for each line. This was for sure one of the harder assignments for me in terms of breaking down and checking each line.





'''
