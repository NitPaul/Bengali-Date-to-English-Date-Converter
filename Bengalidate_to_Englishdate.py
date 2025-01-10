# MIT License
# Copyright (c) 2025 Aonyendo Paul
# See the LICENSE file for details.

# Import necessary modules
from datetime import datetime
import time

# Mapping of Bengali months to English months
bengali_months = {
    'জানুয়ারি': 'January',
    'ফেব্রুয়ারি': 'February',
    'মার্চ': 'March',
    'এপ্রিল': 'April',
    'মে': 'May',
    'জুন': 'June',
    'জুলাই': 'July',
    'আগস্ট': 'August',
    'সেপ্টেম্বর': 'September',
    'অক্টোবর': 'October',
    'নভেম্বর': 'November',
    'ডিসেম্বর': 'December'
}

# Function to convert Bengali numbers to English numbers
def bengali_to_english(num_list):
    """
    Convert Bengali numerical digits to English numerical digits.

    Args:
        num_list (list): A list of Bengali numbers (as strings).

    Returns:
        list: A list of corresponding English numbers.
    """
    bengali_number = ["১", "২", "৩", "৪", "৫", "৬", "৭", "৮", "৯", "০"]
    english_number = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    converted_number = []

    # Iterate through the list and convert Bengali digits to English digits
    for num in num_list:
        english_num = ''
        for char in num:
            if char in bengali_number:
                i = bengali_number.index(char)
                english_num += english_number[i]
        converted_number.append(english_num)

    return converted_number

# Function to convert a Bengali date to an English date
def convert_bengali_date_to_english(bengali_date):
    """
    Convert a Bengali date to an English date.

    Args:
        bengali_date (str): A date in Bengali (e.g., "জানুয়ারি ৮, ২০২৫").

    Returns:
        date: A datetime object representing the converted date.
    """
    try:
        # Split the date string into month, day, and year
        month_bengali, day_bengali, year_bengali = bengali_date.split(' ')
        day_bengali = day_bengali.strip(',')

        # Convert Bengali month to English
        month_english = bengali_months.get(month_bengali.strip(), None)
        day_english = bengali_to_english([day_bengali.strip()])[0]
        year_english = bengali_to_english([year_bengali.strip()])[0]

        # If the month is valid, construct the English date string
        if month_english:
            english_date_str = f"{month_english} {day_english}, {year_english}"
            # Convert to datetime object
            article_date = datetime.strptime(english_date_str, "%B %d, %Y")
            return article_date.date()
        else:
            raise ValueError("Invalid Bengali month")
    except Exception as e:
        print(f"Error: {e}")
        return None

# Example Input and Output
if __name__ == "__main__":
    # Input: Bengali Date
    bengali_date = "জানুয়ারি ৮, ২০২৫"

    # Convert Bengali date to English date
    english_date = convert_bengali_date_to_english(bengali_date)

    # Output: English Date
    if english_date:
        print(f"Input Bengali Date: {bengali_date}")
        print(f"Output English Date: {english_date}")
    else:
        print("Failed to convert the Bengali date.")
