import sys
import os

path = os.path.join(os.path.dirname(__file__), '../')
sys.path.append(path)
from pykong.cli_core import PyKongCLI
from pykong.core import PyKongAPI
from pykong.helper import pretty_json
from pykong.helper import handle_json_response


def main():
    path = "../tests/test.json"
    # path = "../tests/test.yml"
    pykong_cli = PyKongCLI(None, 8081)
    # res = pykong_cli.get_api_list()
    # print(res)

    # res = pykong_cli.get_api("name")
    # print(res)

    # res = pykong_cli.post_api(params=vars())
    # print(res)

if __name__ == "__main__":
    main()