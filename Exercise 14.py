def palindrome_checker_2019_1_60_228(str):

    if str == str[::-1]:
        return True
str = input ("Enter any word or number: ")

if  (palindrome_checker_2019_1_60_228(str) == True):

        print("This is a palindrome: ", str)
else:
        print("This is not a palindrome: ", str)

