#palindrome
string='malayalam'
def palindrome(str):
    if len(str)<2:
        pass
    else:
        if str!=reversed(str):
            str1=str[:len(str)-1]
            palindrome(str1)
        elif str==reversed(str):
            str1=str[:len(str)-1]
            palindrome(str1)
            print(str)


palindrome(string)