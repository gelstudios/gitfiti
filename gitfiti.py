#!/usr/bin/env python
#
# Copyright (c) 2013 Eric Romano (@gelstudios)
# released under The MIT license (MIT) http://opensource.org/licenses/MIT
#
"""
gitfiti

noun : Carefully crafted graffiti in a github commit history calendar

"""

import datetime
import math
import itertools
import urllib2
import json

TITLE = '''
          _ __  _____ __  _ 
   ____ _(_) /_/ __(_) /_(_)
  / __ `/ / __/ /_/ / __/ / 
 / /_/ / / /_/ __/ / /_/ /  
 \__, /_/\__/_/ /_/\__/_/   
/____/ 
'''

KITTY = [
[0,0,0,4,0,0,0,0,4,0,0,0],
[0,0,4,2,4,4,4,4,2,4,0,0],
[0,0,4,2,2,2,2,2,2,4,0,0],
[2,2,4,2,4,2,2,4,2,4,2,2],
[0,0,4,2,2,3,3,2,2,4,0,0],
[2,2,4,2,2,2,2,2,2,4,2,2],
[0,0,0,3,4,4,4,4,3,0,0,0]]

ONEUP = [
[0,4,4,4,4,4,4,4,0],
[4,3,2,2,1,2,2,3,4],
[4,2,2,1,1,1,2,2,4],
[4,3,4,4,4,4,4,3,4],
[4,4,1,4,1,4,1,4,4],
[0,4,1,1,1,1,1,4,0],
[0,0,4,4,4,4,4,0,0]]

ONEUP2 = [
[0,0,4,4,4,4,4,4,4,0,0],
[0,4,2,2,1,1,1,2,2,4,0],
[4,3,2,2,1,1,1,2,2,3,4],
[4,3,3,4,4,4,4,4,3,3,4],
[0,4,4,1,4,1,4,1,4,4,0],
[0,0,4,1,1,1,1,1,4,0,0],
[0,0,0,4,4,4,4,4,0,0,0]]

HACKERSCHOOL = [
[4,4,4,4,4,4],
[4,3,3,3,3,4],
[4,1,3,3,1,4],
[4,3,3,3,3,4],
[4,4,4,4,4,4],
[0,0,4,4,0,0],
[4,4,4,4,4,4]]

OCTOCAT = [
[0,0,0,4,0,0,0,4,0],
[0,0,4,4,4,4,4,4,4],
[0,0,4,1,3,3,3,1,4],
[4,0,3,4,3,3,3,4,3],
[0,4,0,0,4,4,4,0,0],
[0,0,4,4,4,4,4,4,4],
[0,0,4,0,4,0,4,0,4]]

OCTOCAT2 = [
[0,0,4,0,0,4,0],
[0,4,4,4,4,4,4],
[0,4,1,3,3,1,4],
[0,4,4,4,4,4,4],
[4,0,0,4,4,0,0],
[0,4,4,4,4,4,0],
[0,0,0,4,4,4,0]]

HELLO = [
[0,1,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,4],
[0,2,0,0,0,0,0,0,0,2,0,2,0,0,0,0,0,4],
[0,3,3,3,0,2,3,3,0,3,0,3,0,1,3,1,0,3],
[0,4,0,4,0,4,0,4,0,4,0,4,0,4,0,4,0,3],
[0,3,0,3,0,3,3,3,0,3,0,3,0,3,0,3,0,2],
[0,2,0,2,0,2,0,0,0,2,0,2,0,2,0,2,0,0],
[0,1,0,1,0,1,1,1,0,1,0,1,0,1,1,1,0,4]]

HIREME = [
[1,0,0,0,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[3,3,3,0,2,0,3,3,3,0,2,3,3,0,0,3,3,0,3,0,0,2,3,3],
[4,0,4,0,4,0,4,0,0,0,4,0,4,0,0,4,0,4,0,4,0,4,0,4],
[3,0,3,0,3,0,3,0,0,0,3,3,3,0,0,3,0,3,0,3,0,3,3,3],
[2,0,2,0,2,0,2,0,0,0,2,0,0,0,0,2,0,2,0,2,0,2,0,0],
[1,0,1,0,1,0,1,0,0,0,1,1,1,0,0,1,0,1,0,1,0,1,1,1]]

ASCII_TO_NUMBER = {
  '_': 0,
  '_': 1,
  '~': 2,
  '=': 3,
  '*': 4
}

def str_to_sprite(content):
    # Break out lines and filter any excess
    lines = content.split('\n')
    def is_empty_line(line):
        return len(line) != 0
    lines = filter(is_empty_line, lines)
    # Break up lines into each character
    split_lines = map(list, lines)
    # Replace each character with its numeric equivalent
    for line in split_lines:
        for index, char in enumerate(line):
            line[index] = ASCII_TO_NUMBER.get(char, 0)
    # Return the formatted str
    return split_lines

ONEUP_STR = str_to_sprite("""
 ******* 
*=~~-~~=*
*~~---~~*
*=*****=*
**-*-*-**
 *-----* 
  *****  
""")

IMAGES = {
'kitty': KITTY,
'oneup':ONEUP,
'oneup2':ONEUP2,
'hackerschool':HACKERSCHOOL,
'octocat':OCTOCAT,
'octocat2':OCTOCAT2,
'hello':HELLO,
'hireme':HIREME,
'oneup_str':ONEUP_STR
}

def load_images(img_names):
    """loads user images from given file(s)"""
    if img_names[0] == '':
        return dict()
    for image_name in img_names:
        img = open(image_name)
        loaded_imgs = {}
        img_list = ''
        img_line = ' '
        name = img.readline().replace('\n', '')
        name = name[1:]

        while True:
            img_line = img.readline()
            if img_line == '':
                break
            img_line.replace('\n', '')
            if(img_line[0] == ':'):
                loaded_imgs[name] = json.loads(img_list)
                name = img_line[1:]
                img_list = ''
            else:
                img_list += img_line
        loaded_imgs[name] = json.loads(img_list)
        return loaded_imgs

def get_calendar(username, base_url='https://github.com/'):
    """retrieves the github commit calendar data for a username"""
    base_url = base_url + 'users/' + username
    try:        
        url = base_url + '/contributions'
        page = urllib2.urlopen(url)
    except (urllib2.HTTPError,urllib2.URLError) as e:
        print ("There was a problem fetching data from {0}".format(url))
        print (e)
        raise SystemExit
    return page.readlines()

def max_commits(input):
    """finds the highest number of commits in one day"""
    output = set()
    for line in input:
        for day in line.split():
            if "data-count=" in day:
                commit = day.split('=')[1]
                commit = commit.strip('"')
                output.add(int(commit))
    output = list(output)
    output.sort()
    output.reverse()
    return output[0]

def multiplier(max_commits):
    """calculates a multiplier to scale github colors to commit history"""
    m = max_commits/4.0
    if m == 0: return 1
    m = math.ceil(m)
    m = int(m)
    return m

def get_start_date():
    """returns a datetime object for the first sunday after one year ago today
    at 12:00 noon"""
    d = datetime.datetime.today()
    date = datetime.datetime(d.year-1, d.month, d.day, 12)
    weekday = datetime.datetime.weekday(date)
    while weekday < 6:
        date = date + datetime.timedelta(1)
        weekday = datetime.datetime.weekday(date)
    return date

def date_gen(start_date, offset=0):
    """generator that returns the next date, requires a datetime object as
    input. The offset is in weeks"""
    start = offset * 7
    for i in itertools.count(start):
        yield start_date + datetime.timedelta(i)

def values_in_date_order(image, multiplier=1):
    height = 7
    width = len(image[0])
    for w in range(width):
        for h in range(height):
            yield image[h][w]*multiplier

def commit(content, commitdate):
    template = ("""echo {0} >> gitfiti\n"""
    """GIT_AUTHOR_DATE={1} GIT_COMMITTER_DATE={2} """
    """git commit -a -m "gitfiti" > /dev/null\n""")
    return template.format(content, commitdate.isoformat(), 
            commitdate.isoformat())

def fake_it(image, start_date, username, repo, offset=0, multiplier=1,
        git_url='git@github.com'):
    template = ('#!/bin/bash\n'
        'REPO={0}\n'
        'git init $REPO\n'
        'cd $REPO\n'
        'touch README.md\n'
        'git add README.md\n'
        'touch gitfiti\n'
        'git add gitfiti\n'
        '{1}\n'
        'git remote add origin {2}:{3}/$REPO.git\n'
        'git pull\n'
        'git push -u origin master\n')
    strings = []
    for value, date in zip(values_in_date_order(image, multiplier),
            date_gen(start_date, offset)):
        for i in range(value):
            strings.append(commit(i, date))
    return template.format(repo, "".join(strings), git_url, username)

def save(output, filename):
    """Saves the list to a given filename"""
    f = open(filename, "w")
    f.write(output)
    f.close()

def main():
    print (TITLE)
    print ("Enter github url")
    ghe = raw_input("Enter nothing for https://github.com/ to be used: ")
    print ('Enter your github username:')
    username = raw_input(">")
    if not ghe:
        git_base = "https://github.com/"
        cal = get_calendar(username)
    else:
        cal = get_calendar(username,base_url=ghe)
        git_base = ghe
    m = multiplier(max_commits(cal))

    print ('Enter name of the repo to be used by gitfiti:')
    repo = raw_input(">")

    print ('Enter the number of weeks to offset the image (from the left):')
    offset = raw_input(">")
    if not offset.strip():
        offset = 0
    else:
        offset = int(offset)

    print ('By default gitfiti.py matches the darkest pixel to the highest\n'
           'number of commits found in your github commit/activity calendar,\n'
           '\n'
           'Currently this is : {0} commits\n'
           '\n'
           'Enter the word "gitfiti" to exceed your max\n'
           '(this option generates WAY more commits)\n'
           'Any other input will cause the default matching behavior'
           ).format(max_commits(cal))
    match = raw_input(">")
    if match == "gitfiti": 
        match = m
    else: 
        match = 1

    print ('enter file(s) to load images from (blank if not applicable)')
    img_names = raw_input(">").split(' ')
    images = dict(IMAGES, **load_images(img_names))

    print ('enter the image name to gitfiti')
    print ('images: ' + ", ".join(images.keys()))
    image = raw_input(">")
    if not image:
        image = IMAGES['kitty']
    else:
        try: 
            image = images[image]
        except: 
            image = IMAGES['kitty']
    if not ghe:
        output = fake_it(image, get_start_date(), username, repo, offset,
                m*match)
    else:
        git_url = raw_input("Enter git url like git@site.github.com: ")
        output = fake_it(image, get_start_date(), username, repo, offset,
                m*match,git_url=git_url)

    save(output, 'gitfiti.sh')
    print ('gitfiti.sh saved.')
    print ('Create a new(!) repo at: {0}new and run it.'.format(git_base))

if __name__ == '__main__':
    main()
