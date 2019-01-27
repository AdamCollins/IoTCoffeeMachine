from lib import lib
import time

# You should avoid sharing this token,
#  and should store it in an env variable
lib = lib(token="FZGu2fc2yuc6zyi1lqq1sqsIj9bJv0kkCXzzrwLvrRu7qwt4j6XeNCzEagXtujug")
twitter = lib.gkaww.twitter["@0.0.2"]

#number of polls/min
pollInterval = 1

def getTweets(since):
    return twitter.statuses.user_timeline(
        config="{\"consumer_key\":\"ZtSUgVNL9vLVEvMhJZUJwqR7O\",\"consumer_secret\":\"I93nmt7E361jPRD0xw0Z53Ok2uSF7WzOJXcJDwEijUQlrlXOPh\",\"access_token\":\"1036312409151918080-bDBUwjQ2Obfn9GtHXeE8vfkUiuyjUM\",\"access_token_secret\": \"r5K7MU6rj76wICiFtaN96b7YSIME6eam9FpilDwylJbkY\"}", # (required)
        screen_name="pyram66",
        since_id=since
        )

# def brewCoffee():
#     return

def main():
    lastPost = 0
    global pollInterval
    while True:
        print('hello')
        result = getTweets(lastPost)    # gets tweets since last data
        if newRequest(result):
            lastPost = result.data[0].id
            #brewCoffee():

        time.sleep(60/pollInterval)


# result = twitter.statuses.user_timeline(
#   config="{\"consumer_key\":\"ZtSUgVNL9vLVEvMhJZUJwqR7O\",\"consumer_secret\":\"I93nmt7E361jPRD0xw0Z53Ok2uSF7WzOJXcJDwEijUQlrlXOPh\",\"access_token\":\"1036312409151918080-bDBUwjQ2Obfn9GtHXeE8vfkUiuyjUM\",\"access_token_secret\": \"r5K7MU6rj76wICiFtaN96b7YSIME6eam9FpilDwylJbkY\"}", # (required)
#   screen_name="pyram66",
#   since_id=0
# )


if __name__ == '__main__':
    main()