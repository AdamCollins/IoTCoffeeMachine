from lib import lib

# You should avoid sharing this token,
#  and should store it in an env variable
lib = lib(token="FZGu2fc2yuc6zyi1lqq1sqsIj9bJv0kkCXzzrwLvrRu7qwt4j6XeNCzEagXtujug")
import ipdb;ipdb.set_trace()
twitter = lib.gkaww.twitter["@0.0.2"]

result = twitter.get(
  config="{\"consumer_key\":\"ZtSUgVNL9vLVEvMhJZUJwqR7O\",\"consumer_secret\":\"I93nmt7E361jPRD0xw0Z53Ok2uSF7WzOJXcJDwEijUQlrlXOPh\",\"access_token\":\"1036312409151918080-bDBUwjQ2Obfn9GtHXeE8vfkUiuyjUM\",\"access_token_secret\": \"r5K7MU6rj76wICiFtaN96b7YSIME6eam9FpilDwylJbkY\"}", # (required)
  path="statuses/user_timeline"
)