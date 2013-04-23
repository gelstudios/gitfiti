#gitfiti
import os, sys
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

def trim_calendar(input):
	"""remote the first 6 days to align data with sundays"""
	trim=input[6:]
	return trim
 
def squash_calendar(input):
	"""group days into weeks for formatting"""
	c=[]
	input.pop	
	return c

#find date range for N weeks
#each column starts on SUNDAY

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

#profit!

test=[
[4,3,2,1,0],
[3,2,1,0,4],
[2,1,0,4,3],
[1,0,4,3,2],
[0,4,3,2,1]
]

#GIT_AUTHOR_DATE='your date' GIT_COMMITTER_DATE='your date' git commit -m 'new (old) files'
