import os, sys, datetime, math, itertools
try:
	import requests
except:
	print 'the requests module is required'
	exit(1)

def get_calendar(username):
	"""retrieves the github commit calendar data for a username"""
	BASEURL='https://github.com/'
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

def multiplier(max_commits):
	"""calculates a multiplier to scale github colors to commit history"""
	m = max_commits/4.0
	m = math.ceil(m)
	m = int(m)
	return m

def get_start_date():
	'''returns a datetime object for the first sunday after one year ago today at 12:00 noon'''
	d = datetime.datetime.today()
	date = datetime.datetime(d.year-1, d.month, d.day, 12)
	weekday = datetime.datetime.weekday(date)
	while weekday < 6:
		print repr(date)
		date = date + datetime.timedelta(1)
		weekday = datetime.datetime.weekday(date)
	return date

def date_gen(start_date):
	'''generator to return the next day, requires a datetime object as input'''
	for i in itertools.count():
		yield start_date + datetime.timedelta(i)

def values_in_date_order(image, multiplier=1):
	height = 7
	width = len(image[0])
	for h in range(height):
		for w in range(width):
			yield image[h][w]*multiplier

def fake_it(image, start_date, username, repo, multiplier=1):
	template=('git init gitfiti\n'
				'cd gitfiti\n'
				'touch gitfiti\n'
				'git add gitfiti\n'
				'%s\n'
				'git remote add origin git@github.com:%s/%s.git\n'
				'git push -u origin master\n')
	strings = []
	for value, date in zip(values_in_date_order(image, multiplier), date_gen(start_date)):
		for i in range(value):
			strings.append(commit(i, date))
	return template % ("".join(strings), username, repo)
	
def commit(content, commitdate):
	template='''echo %s >> gitfiti\nGIT_AUTHOR_DATE=%s GIT_COMMITTER_DATE= %s git commit -a -m "gitfiti"\n''' 
	return template	% (content, commitdate.isoformat(), commitdate.isoformat())

def main():
	username='gelstudios'
	cal = get_calendar(username)
	x = trim_calendar(cal)
	m = max_commits(cal)
	m = multiplier(m)
	cal = cal[x:]
	fake_it(kitty, get_start_date(), m)

if __name__=='__main__':
	main()

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

hello=[
[0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,3,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,4,4,4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,3,3,3,3,3,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,2,2,0,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,1,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0]]