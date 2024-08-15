# Print the season name of the year based on the month number using a dictionary.

monthToSeason = {
    1: 'Winter', 2: 'Winter', 3: 'Spring',
    4: 'Spring', 5: 'Spring', 6: 'Summer',
    7: 'Monsoon', 8: 'Monsoon', 9: 'Autumn',
    10: 'Autumn', 11: 'Autumn', 12: 'Winter'
}

def getSeason(month):
    if 1 <= month <= 12:
        return monthToSeason[month]
    else:
        return 'Invalid month number'

monthNumber = int(input("Enter the month number (1-12): "))
season = getSeason(monthNumber)
print(f"The season for month {monthNumber} is: {season}")
