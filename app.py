from lib import lib
import time, json
import serial
import os
def restart():
	os.system("./run.sh")
	exit()
try:
	try:
		ser = serial.Serial("/dev/ttyACM0",9600)
		ser.flushInput()
	except:
		ser = serial.Serial("/dev/ttyACM1",9600)
		ser.flushInput()
	# You should avoid sharing this token,
	#  and should store it in an env variable
	lib = lib(token="FZGu2fc2yuc6zyi1lqq1sqsIj9bJv0kkCXzzrwLvrRu7qwt4j6XeNCzEagXtujug")
	twitter = lib.gkaww.twitter["@0.0.2"]

	#number of polls/min
	pollInterval = 6

	prevTweetID = 0

	prevTweet = "None"

	def restart():
		os.system("./run.sh")
		exit()

	#Turn on servo
	def brewCoffee():
		global ser
		try:
			for x in range(20):
				ser.write("A")
		except:
			restart()
	while True:
		user_timeline = twitter.get(
		  path="search/tweets", # (required)
		  params={
		    "q": "@adamscoffeemak1 since:2019-01-12",
		    "count": "100"
		print "{{NEW REQ}}"

		currTweet = user_timeline['data'][0]['text']
		currTweetID = user_timeline['data'][0]['id']

		print "Curr Tweet: %s"%(currTweet)
		print "Curr ID: %i"%(currTweetID)

		print "Prev Tweet: %s"%(prevTweet)
		print "Prev ID: %i"%(prevTweetID)

		if currTweetID != prevTweetID:
			print "===================="
			print "===BREW Coffee :)==="
			print "===================="
			prevTweetID = currTweetID
			prevTweet = currTweet
			brewCoffee()
		else:
			print "=================="
			print "===NO Coffee :p==="
			print "=================="
		time.sleep(60/pollInterval)
except:
	restart()
# if __name__ == '__main__':
#     main()