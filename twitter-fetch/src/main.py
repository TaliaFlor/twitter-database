from exporter import Exporter
from fetcher import Fetcher
from parser import Parser

config_file = "../resources/config.json"

data_folder = "../../sql/data/"

try:
    print('App initialized')

    fetcher = Fetcher(config_file)
    posts = fetcher.fetch()

    parser = Parser(posts)
    collection = parser.parse()

    exporter = Exporter(data_folder, collection)
    exporter.export()

    print('App finalized')
except Exception as exp:
    print(exp)
