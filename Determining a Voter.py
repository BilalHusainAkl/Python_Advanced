#WPP to print whether you can vote or not
age=int(input('Enter your age'))
voterid=input("Do you possess a Voter ID (y or n)")
if (age>=18) and (voterid=='y'):
    print("Congratulations! You can Vote")
else:
    print("Sorry, You cannot Vote.")