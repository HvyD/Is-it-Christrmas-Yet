
# coding: utf-8

# Created BY HvyD


import datetime

Today = datetime.date.today()
Christmas = datetime.date(Today.year , 12, 25)

if Today == Christmas:
    print("MERRY CHRISTMAS")

else:
    print("No Presents For You!! it's only",Today.strftime('%b %d,%Y'))

