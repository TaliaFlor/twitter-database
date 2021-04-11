from twitter import Twitter

from modules.auth import get_oauth

credentials_filename = "../resources/credentials.json"
oauth = get_oauth(credentials_filename)

twitter = Twitter(auth=oauth)

# &next_results
next_token = ""
while True:
    try:
        data = twitter.search.tweets(q="books" + next_token)
        next_token = data["search_metadata"]["next_results"]
        print(data)
    except:
        break
# print()
# print(twitter.search.tweets(q="books&count=100")["search_metadata"])

# queries_filename = "resources/query.json"
# queries = get_queries(queries_filename)

# data = []
# for query in queries:
#     data.append(twitter.search.tweets(q=query))

# print(len(data))
# print(data)

# parser = Parser()
# parser.parse(data)
