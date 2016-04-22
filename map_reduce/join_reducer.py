#!/usr/bin/env python
import sys

prev_word          = "  " #initialize previous word  to blank string
line_cnt           = 0  #count input lines
total		   = 0
show_on            = False

for line in sys.stdin:
    line       = line.strip()       #strip out carriage return
    key_value  = line.split('\t')   #split line, into key and value, returns a list
    line_cnt   = line_cnt+1     

    curr_word  = key_value[0]         #key is first item in list, indexed by 0
    value_in   = key_value[1]         #value is 2nd item

    if curr_word != prev_word:
        if line_cnt>1 and show_on:
		print('{0} {1}'.format(prev_word,total))
	total = 0
	show_on = False
        prev_word = curr_word  #set up previous word for the next set of input lines
	
    if (value_in == 'ABC'): 
	show_on = True
    else:
        total = total + int(value_in)

if show_on:
	print('{0} {1}'.format(prev_word,total))

# Description of map/reduce problem is below:
#
# The datasets contain the following information:

# join2_gennum*.txt consist of <TV show, count> (A TV show title and the number of viewers)

# Example join2_gennum*.txt:

# Almost_News, 25
# Hourly_Show,30
# Hot_Cooking,7
# Almost_News, 35
# Postmodern_Family,8
# Baked_News,15
# Dumb_Games,60
# …
# join2_genchan*.txt consists of <TV show title, channel> (A TV show title and the channel it was on)

# Example join2_genchan*.txt:

# Almost_News, ABC
# Hourly_Show, COM
# Hot_Cooking, FNT
# Postmodern_Family, NBC
# Baked_News, FNT
# Dumb_Games, ABC
# …
# 4. Your Task: Implement the following join request in Map/Reduce:

# What is the total number of viewers for shows on ABC?

# The show-to-channel relationship is Many-to-Many. In other words, each show might appear on many channels, and each channel might broadcast many shows.

# In pseudo-SQL it might be something like:

#     select sum( viewer count) from File A, File B where FileA.TV show = FileB.TV show and FileB.Channel='ABC' grouped by TV show

#     5. Upload the resulting output from the reducers, use numReduceTasks=1

#     The output will look like: <TVshow_title total_viewers>

#     Example Output:

#     Almost_News 60
#     Dumb_Games 60
#     …
