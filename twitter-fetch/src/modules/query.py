from src.util import read_file


def get_queries(filename):
    """Returns the list of queries"""
    json = read_file(filename)["queries"]
    queries = []
    for query in json:
        queries.append(query["query"])
    return queries
