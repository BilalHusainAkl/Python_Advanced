#WPP to Reverse And Add Until a Palindrome number is obtained.
num=int(input('Enter any number'))
while True:
    str_num=str(num)
    rev_str=str_num[::-1]
    if str_num==rev_str:
        print(num,"Number is Palindrome")
        break   
    num=int(str_num)+int(rev_str)