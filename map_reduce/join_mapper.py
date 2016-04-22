#!/usr/bin/env python
import sys

chans   = ['ABC','DEF','CNO','NOX','YES','CAB','BAT','MAN','ZOO','XYZ','BOB']

for line in sys.stdin:
    line       = line.strip()   #strip out carriage return
    key_value  = line.split(",")   #split line, into key and value, returns a list
    key_in     = key_value[0]   #key is first item in list
    value_in   = key_value[1]   #value is 2nd item 

    #print key_in
    if (value_in in chans):
	if value_in == 'ABC':
        	print( '%s\t%s' % (key_in, value_in) )  #print a string, tab, and string
    else:
        print( '%s\t%s' % (key_in, value_in) )  #print a string tab and string

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
