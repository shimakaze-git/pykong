import sys
import os

path = os.path.join(os.path.dirname(__file__), '../')
sys.path.append(path)
from pykong.core import PyKongAPI
from pykong.helper import pretty_json


def main():
    path = "../tests/test.json"
    # path = "../tests/test.yml"
    pykong_obj = PyKongAPI(None, 8081)
    # pykong_obj.add_list(path)

    res = pykong_obj.get_list()
    res = pykong_obj.status()
    print(pretty_json(res))

if __name__ == "__main__":
    main()