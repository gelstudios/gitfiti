#gitfiti
#generate a value insertion plan for a 7xN matrix
#github new repo in account
#git init new repo
#	git add gitfiti_output
#	start of file:
#	git commit -date $(date in the past) gitfiti_output
#	for day in matrix:
#		for value in day:
#			add a character to gitfiti file
#			git commit -m -date $date_value gitfiti_output "g"
#git add remote (get github url)
#git push -f master

import os, sys, datetime, math
try:
	import requests
except:
	print 'the requests module is required'
	exit(1)

BASEURL='https://github.com/'
color_commit_values=[0,1,2,3,4]

def get_calendar(username):
	"""retrieves the github commit calendar data for a username"""
	url = BASEURL + 'users/' + username + '/contributions_calendar_data'
	req = requests.get(url)
	return req.json()

def max_commits(input):
	"""finds the highest number of commits in one day"""
	output = set()
	for i, j in enumerate(input):
		output.add(input[i][1])
	output = list(output)
	output.sort()
	output.reverse()
	return output[0]

def trim_calendar(input):
	"""returns index of first sunday in the input"""
	for i, j in enumerate(input):
		day = input[i][0]
		day = datetime.datetime.strptime(day, '%Y/%m/%d')
		weekday = datetime.datetime.weekday(day)
		if weekday == 6:
			return i

kitty=[
[0,0,0,4,0,0,0,0,4,0,0,0],
[3,3,4,2,4,4,4,4,2,4,3,3],
[0,0,4,2,2,2,2,2,2,4,0,0],
[3,3,4,2,4,2,2,4,2,4,3,3],
[0,0,4,2,2,3,3,2,2,4,0,0],
[3,3,4,2,2,2,2,2,2,4,3,3],
[0,0,0,4,4,4,4,4,4,0,0,0]]

oneup=[
[0,0,4,4,4,4,4,4,4,0,0],
[0,4,2,2,1,1,1,2,2,4,0],
[4,3,2,2,1,1,1,2,2,3,4],
[4,3,3,4,4,4,4,4,3,3,4],
[0,4,4,1,4,1,4,1,4,4,0],
[0,0,4,1,1,1,1,1,4,0,0],
[0,0,0,4,4,4,4,4,0,0,0]]

#each column starts on SUNDAY
def multiplier(max_commits):
	"""calculates a multiplier to scale github colors to commit history"""
	m = max_commits/4.0
	m = math.ceil(m)
	m = int(m)
	return m

def fakeit(image, reference, multiplier=1):
	height = range(7)
	width = len(image[0])
	cal_index = 0
	for w in range(width):
		for h in height:
			count = image[h][w]*multiplier
			if count == 0:
				cal_index += 1
				continue
			for c in range(count):
				date = reference[cal_index][0]
				date = datetime.datetime.strptime(date, '%Y/%m/%d').isoformat()
				shelloutput(c, date)
			cal_index += 1

def shelloutput(content, commitdate):
	print '''echo ''' + str(content) + ''' >> gitfiti'''
	print '''GIT_AUTHOR_DATE=''' + commitdate + ''' GIT_COMMITTER_DATE=''' + commitdate + ''' git commit -a -m "''' + "gitfiti" +'''"'''


#git init gitfitii
#cd gitfiti
#touch gitfiti
#git add gitfiti
###SHELLOUTPUT
#git remote add origin git@github.com:gelstudios/kitty.git
#git push -u origin master

username='gelstudios'
cal = get_calendar(username)
x = trim_calendar(cal)
m = max_commits(cal)
m = multiplier(m)
cal = cal[x:]
fakeit(kitty, cal, m)