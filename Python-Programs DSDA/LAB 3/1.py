# Write a function called check_season, it takes a month parameter and
# return the season: Autumn, Winter, Spring or Summer.
def check_season(month):
    if month in ("April", "May", "June"):
        return "Summer"
    elif month in ("July", "August", "September"):
        return "Autumn"
    elif month in ("October", "November", "December"):
        return "Winter"
    elif month in ("January", "February", "March"):
        return "Spring"
    else:
        return "NA"

m = input('Enter Month: ')
res = check_season(m)
if res:
    print('Season: ', res)
else:
    print('Invalid Month Entered')
