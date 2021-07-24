# This simple program was made by Woox
# github.com/WooxHimself




print("""  ___                    _      ___             _        ___   _      
 |   \  __ __ __  _ _   | |    / __|  _ __   __| |      / __| | |  __ 
 | |) | \ V  V / | ' \  | |    \__ \ | '_ \ / _` |     | (__  | | / _|
 |___/   \_/\_/  |_||_| |_|    |___/ | .__/ \__,_|      \___| |_| \__|
                                     |_|                              
                                     Download Speed Calculator in Python3
                                     """)
#In this input, user will define the download speed.
speed = int(input("Enter your download speed (Megabytes): "))

#In this input, user will define the file size.
size = int(input("Enter file size (Megabytes): "))

#This will print the download time
print ("The download time will be: ...")

#This is how is the time being calculated.
result = size/(speed/8)

#This will print the result time. (The %.2f will force the program to print only 2 decimal numbers.)
print("%.2f" % result, "seconds")
