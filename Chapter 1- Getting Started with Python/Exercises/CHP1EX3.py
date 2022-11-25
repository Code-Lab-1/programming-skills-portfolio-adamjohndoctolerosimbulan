#Import the current package
import datetime
currentdt = datetime.datetime.now()
#Prints the cuurent date and time
print ("Current Date & Time:"),
print(currentdt.strftime("%Y-%m-%d %H:%M:%S"))