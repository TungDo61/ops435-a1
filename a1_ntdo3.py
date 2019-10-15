#!/usr/bin/env python3
''' OPS435 Assignment 1 - Fall 2019
Program: a1_ntdo3.py
Author: Nguyen Tung Do
The python code in this file a1_ntdo3.py is original work written by
Tung Do. No code in this file is copied from any other source 
except those provided by the course instructor, including any person, 
textbook, or on-line resource. I have not shared this python script 
with anyone or anything except for submission for grading.  
I understand that the Academic Honesty Policy will be enforced and 
violators will be reported and appropriate action will be taken
'''
import sys

#Checking the number of arguments pass on to the script
def usage(number):
    '''
    usage(number) -> str
    usage() checks the number of arguments to make sure that it is
    between 2 and 3. If false, return usage instruction 
    e.g. usage('2017/12/31', '5') -> True
         usage('2017/12/31', '5', '--step') -> True
         usage('2017/12/31') -> 'Usage: a1_rchan.py [--step] YYYY/MM/DD +/-n'
         usage('2017/12/31', '5', '--step', 'sdoif', '234') -> 'Usage: a1_rchan.py [--step] YYYY/MM/DD +/-n'
'''
    number = len(sys.argv)
    if number <= 2:
        print('Usage: a1_rchan.py [--step] YYYY/MM/DD +/-n')
        return False
    elif number > 4:
        print('Usage: a1_rchan.py [--step] YYYY/MM/DD +/-n')
        return False
    else:
        return True

#Checking if the date enter is valid
def valid_date(today):
    '''
    valid_date(today) -> str
    valid_date() takes a valid date string in 'YYYY/MM/DD' format and verify 
    either the string entered is in the correct 'YYYY/MM/DD' format.
    e.g. valid_date('2017/012/31') -> 'Error: wrong date entered'
         valid_date('2018/23/31') -> 'Error: wrong month entered'
         valid_date('2018/02/56') -> 'Error: wrong day entered'
'''
    today = sys.argv[1]
    if len(today) != 10:
        return "Error: wrong date entered"
        sys.exit()
    else:
        str_year, str_month, str_day = today.split('/')
        year = int(str_year)
        month = int(str_month)
        day = int(str_day)
        if month > 12:
            return "Error: wrong month entered"
            sys.exit()
        elif day > 31:
            return "Error: wrong day entered"
            sys.exit() 
        else:
            return "Valid date"

#Checking if year is leap year
def leap_year(today):
    '''
    leap_year(today) -> str
    leap_year() takes a valid date string in 'YYYY/MM/DD' format and check 
    whether or not the year is a leap year
    e.g. leap_year('2012/12/31') -> 'True'
         leap_year('2015/01/31') -> 'False'
'''
    leap = False
    str_year, str_month, str_day = today.split('/')
    year = int(str_year)

    lyear = year % 4
    if lyear == 0:
        leap = True
    lyear = year % 400
    if lyear == 0:
        leap = True

    if leap == True:
        return True
    return False

#Determine the number of days of each months in the year
def day_in_mon(today):
    '''
    day_in_mon(today) -> str
    day_in_mon() takes a valid date string in 'YYYY/MM/DD' format and return a 
    dictionary with the month and number of days in month as a pair of keys:values.
    e.g. day_in_mon('2019/01/01') -> '{1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}'
'''
    str_year, str_month, str_day = today.split('/')
    year = int(str_year)

    if leap_year(today) == True:
         mon_max = { 0:31, 1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
         return mon_max
    else:
         mon_max = { 0:31, 1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
         return mon_max

# Return the date in YYYY/MM/DD after the given day 
def after(today):
       '''
    after(today) -> str
    after() takes a valid date string in 'YYYY/MM/DD' format and return a 
    date string for the next day in 'YYYY/MM/DD' format.
    e.g. after('2017/12/31') -> '2018/01/01'
         after('2018/01/31') -> '2018/02/01'
         after('2018/02/28') -> '2018/03/01'
'''
       str_year, str_month, str_day = today.split('/')
       year = int(str_year)
       month = int(str_month)
       day = int(str_day)

       tmp_day = day + 1 # next day

       mon_max = day_in_mon(today)
       if tmp_day > mon_max[month]:
          to_day = 1 # if tmp_day > this month's max, reset to 1
          tmp_month = month + 1
       else:
          to_day = tmp_day
          tmp_month = month + 0

       if tmp_month > 12:
           to_month = 1
           year = year + 1
       else:
           to_month = tmp_month + 0

       next_date = str(year)+"/"+str(to_month).zfill(2)+"/"+str(to_day).zfill(2)
     
       return next_date

# Return the date in YYYY/MM/DD before the given day
def before(today):
       '''
    before(today) -> str
    before() takes a valid date string in 'YYYY/MM/DD' format and return a 
    date string for the previous day in 'YYYY/MM/DD' format.
    e.g. after('2018/01/01') -> '2017/12/31'
         after('2018/02/01') -> '2018/01/31'
         after('2018/03/20') -> '2018/03/19'
'''
       str_year, str_month, str_day = today.split('/')
       year = int(str_year)
       month = int(str_month)
       day = int(str_day)

       mon_max = day_in_mon(today)
       tmp_day = day -1
       if tmp_day == 0:
          to_day = mon_max[month-1] # if day=1 then return the final day of last month
          tmp_month = month - 1
       else:
          to_day = tmp_day
          tmp_month = month + 0

       if tmp_month == 0:
           to_month = 12
           year = year - 1
       else:
           to_month = tmp_month + 0

       pre_date = str(year)+"/"+str(to_month).zfill(2)+"/"+str(to_day).zfill(2)
     
       return pre_date

#Take a day and a number and return the day before or after based on the number.
def dbda(date,days):
	'''
    dbda(date,days) -> str
    dbda(date,days) takes two string, first one is a date in YYYY/MM/DD format,
    second string is an integer and return a date before or after the
    first date based on the number
    e.g. dbda('2019/01/01', '5') -> '2019/01/06'
         dbda('2019/01/01', '-5')) -> '2018/12/27'
'''
	number = 0
	tmp_date = date
	count = int(days)
	if count > 0:
		while number < count:
			tmp_date = after(tmp_date)
			number = number + 1
		return tmp_date
	elif count < 0:
		while count < number:
			tmp_date = before(tmp_date)
			number = number - 1
		return tmp_date
		
if __name__ == "__main__":
    cmd_arg = sys.argv[:]
    number = len(cmd_arg)
    if number == 4:
      if "--step" in sys.argv[:]:
        cmd_arg.remove("--step")
        count = 0
        today = cmd_arg[1]
        days = int(cmd_arg[2])
        if days > 0:
          while count < days:
            print(after(today))
            today = after(today)
            count = count + 1
        else:
          while count > days:
            print(before(today))
            today = before(today)
            count = count - 1
    else:
      if usage(number):
        today = sys.argv[1]
        days = sys.argv[2]
        if valid_date(today) == "Valid date":
          print(dbda(today,days))
        else:
          print(valid_date(today))
