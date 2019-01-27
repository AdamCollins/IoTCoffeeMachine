from lib import lib
import time, json
import serial
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
pollInterval = 3

prevTweetID = 0

prevTweet = "None"

#Turn on servo
def brewCoffee():
	global ser
	for x in range(20):
		ser.write("A")

while True:
	user_timeline = twitter.get(
  config="{\"consumer_key\":\"ZtSUgVNL9vLVEvMhJZUJwqR7O\",\"consumer_secret\":\"I93nmt7E361jPRD0xw0Z53Ok2uSF7WzOJXcJDwEijUQlrlXOPh\",\"access_token\":\"1036312409151918080-bDBUwjQ2Obfn9GtHXeE8vfkUiuyjUM\",\"access_token_secret\": \"r5K7MU6rj76wICiFtaN96b7YSIME6eam9FpilDwylJbkY\"}", # (required)
  path="statuses/user_timeline")
	print "new req"

	currTweet = user_timeline['data'][0]['text']
	currTweetID = user_timeline['data'][0]['id']

	print "Curr Tweet: %s"%(currTweet)
	print "Curr ID: %i"%(currTweetID)

	print "Prev Tweet: %s"%(prevTweet)
	print "Prev ID: %i"%(prevTweetID)

	if currTweetID != prevTweetID:
		print "===BREW Coffee==="
		prevTweetID = currTweetID
		prevTweet = currTweet
		brewCoffee()
	else:
		print "===NO Coffee :p==="
	time.sleep(60/pollInterval)

# if __name__ == '__main__':
#     main()