# Program that tells you what to do as an activity so you don't have to choose 
# Logic: user tells cpu how many activities they want to choose from, user tells cpu what activities are, 
# cpu makes a list of all the activities, cpu randomly chooses an activity for user and prints it

import random

num_activities = input('How many activities do you want to choose from? : ')

num_activities = int(num_activities)

activities = []

for num in range(num_activities):
    activities.append(input('enter activity: '))

answer = random.choice(activities)

print(answer)