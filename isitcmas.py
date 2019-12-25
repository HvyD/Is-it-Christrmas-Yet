#!/usr/bin/env python3.8

# coding: utf-8

# ## Created By HvyD && Phidget_Kitty
# This is a fun little scrypt and notebook built Christmas Eve 2018 with my Daughter.
# This script should work all year around, provided the Python and datetime package is not defunct. 



# imports
import os
import datetime
from datetime import timedelta




# Todays Date and Christmas Variable's
Today = datetime.datetime.today()
Christmas = datetime.datetime(Today.year , 12, 25)


# Boolean conditional statement checking Variable's 
if Today == Christmas:
    print("MERRY CHRISTMAS") # return message

else:
    print("No Presents For You!! it's only",Today.strftime('%b %d,%Y')) # return meesage with date function changed


for i in range(11):
    print('\n')

input("Press the <ENTER> key to continue...")

for i in range(11):
    print('\n')

print("Bye, Bye")
print("Try Again in : {}".format(Christmas - Today))
print('\n')





