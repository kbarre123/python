#!/usr/bin/python
from datetime import date
import math

#1) ********** Volume of a sphere **********

radius = 5
now = date.today()

volume = (4 * (math.pi * pow(radius, 3))) / 3
#print "Today's date is " + str(now) + ". The volume of the sphere is " + str(volume) + "."

# Today's date is 2013-10-17. The volume of the sphere is 523.598775598.

#2) ********** Book Prices **********

price = 24.95
discount = (1 - 0.4)
ship1 = 3.00
ship2 = 0.75
volume = 60

batch1 = (price * (1-discount)) + ship1
batch2 = ((price * (1-discount)) + ship2) * (volume - 1)
total = batch1 + batch2

#print "Total order price for " + str(volume) + " books = $" + str(total) + "."

# Total order price for 60 books = $646.05.

#3) ********** Timed Run **********

# Define start and end time
start_time_hours = 6
start_time_minutes = 52
start_time_seconds = 0
end_time_hours = 0
end_time_minutes = 0
end_time_seconds = 0

# Define velocities
easy_pace_hours = 0
easy_pace_minutes = 8
easy_pace_seconds = 15
tempo_pace_hours = 0
tempo_pace_minutes = 7
tempo_pace_seconds = 12

print "Start time: 6:52:00 AM."

# Define func to convert time to seconds
def convert (hours, minutes, seconds):
    converted_seconds = (hours * 60 * 60) + (minutes * 60) + seconds
    return converted_seconds

# Convert start time to seconds
start_time = convert(6, 52, 0)
#print "Start time: " + str(start_time) + " seconds."

# Convert velocities to seconds
easy_pace_vel = convert(0, 8, 15)
#print "Easy pace velocity: " + str(easy_pace_vel) + " seconds per mile."

tempo_pace_vel = convert(0, 7, 12)
#print "Tempo pace velocity: " + str(tempo_pace_vel) + " seconds per mile."

# Define func to convert lap time into seconds
def lap_seconds(miles, pace):
    lap = miles * pace
    return lap

# Calc lap times
easyLap = lap_seconds(2, easy_pace_vel)
#print "Easy laps took : " + str(easyLap) + " seconds."

tempoLap = lap_seconds(3, tempo_pace_vel)
#print "Tempo laps took : " + str(tempoLap) + " seconds."

totalLap = easyLap + tempoLap
print "Total laps took: " + str(totalLap) + " seconds."

# Add lap times to start time in seconds
endTime = start_time + totalLap
print "End time: " + str(endTime) + " seconds."

# Convert endTime seconds back to hours, minutes and seconds format
endTime_hours = (endTime / 60) / 60
endTime_minutes = (endTime / 60) % 60
endTime_sec = (endTime % 60) % 60

# Print end time
print "End time: " + str(endTime_hours) + ":" + str(endTime_minutes) + ":" + str(endTime_sec) + " AM."