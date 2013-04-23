#!/bin/env python
#gitfiti_web
from bottle import request, route, run, post, template

@route("/")
def index():
	return template('index')

@route()

def main():
	run(host='localhost', port=8080, debug=True, reloader=True)

if __name__ == '__main__':
	main()