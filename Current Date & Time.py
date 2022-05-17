#WPP to print current date & time.
import datetime
now = datetime.datetime.now()
print("Current date and time : ")
print(now.strftime("%D/%M%Y %H:%M:%S"))
