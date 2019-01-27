from lib import lib
import time, json
import serial
import os
def restart():
	os.system("./run.sh")
	exit()
try:
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
		try:
			ser = serial.Serial("/dev/ttyACM0",9600)
			ser.flushInput()
		except:
			ser = serial.Serial("/dev/ttyACM1",9600)
			ser.flushInput()
		try:
			for x in range(20):
				ser.write("A")
		except e:
			print(e)
		finally:
			ser.close()
	while True:
		user_timeline = twitter.get(
		  config="{\"consumer_key\":\"ZtSUgVNL9vLVEvMhJZUJwqR7O\",\"consumer_secret\":\"I93nmt7E361jPRD0xw0Z53Ok2uSF7WzOJXcJDwEijUQlrlXOPh\",\"access_token\":\"1036312409151918080-bDBUwjQ2Obfn9GtHXeE8vfkUiuyjUM\",\"access_token_secret\":\"r5K7MU6rj76wICiFtaN96b7YSIME6eam9FpilDwylJbkY\"}", # (required)
		  path="search/tweets", # (required)
		  params={
		    "q": "@adamscoffeemak1 since:2019-01-12",
		    "count": "100"}
		)
		print("--NEW REQ--")


		currTweet = user_timeline['data']['statuses'][0]['text']
		currTweetID = user_timeline['data']['statuses'][0]['id']

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