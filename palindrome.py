# this code checks if a word is a palindrome
# a palindrome is a word, number, phrase, or other sequence of symbols that 
# reads the same backwards as forwards, such as madam or racecar

def palindrome(str):
    # str[:1] -> first character
    # str[-1:] -> last character
    if str == str[::-1]:
        return True
    else:
        return False
# print(palindrome(userinput))


# main palindrome function
def main():
    # asks the user for their input
    userinput = input('Please enter a word, number, or number that you would like to check if its a palindrome: ')
    # checks if it is a palindrome by checking the input by its reverse
    # [::1] reverses the string
    if userinput == userinput[::-1]:
        print(userinput, 'is a palindrome.')
    else:
        print(userinput, 'is not a palindrome')

############# MAIN #############

print('Hi user! This is a palindrome detection program.' \
        ' \n-------------------------------------------------'\
        ' \nA palindrome is a word, number, phrase, or other sequence' \
        ' of symbols that reads the same backwards as forwards, such as madam or racecar.' \
        ' This program is used to detect if your input is a palindrome.')
play_again = ''
while play_again != 'n':
    main()
    play_again = input('Would you like to try another? (y/n): ')
    