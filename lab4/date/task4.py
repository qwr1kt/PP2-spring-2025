from datetime import datetime

def date_difference_in_seconds(date1, date2):
    diff = date2 - date1
    return diff.total_seconds()

date1_str = input("Enter the first date (YYYY-MM-DD HH:MM:SS):")
date1 = datetime.strptime(date1_str, "%Y-%m-%d %H:%M:%S")

date2_str = input("Enter the second date (YYYY-MM-DD HH:MM:SS):")
date2 = datetime.strptime(date2_str, "%Y-%m-%d %H:%M:%S")

difference = date_difference_in_seconds(date1, date2)

print("Difference in seconds:", int(difference))