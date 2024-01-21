import json
import os

import requests
from dotenv import load_dotenv

load_dotenv()


def upload_file_to_gist(gist_id: str, file: str, headers: str) -> requests.Response:
    with open(file, "r") as f:
        content = f.read()

    r = requests.patch(
        "https://api.github.com/gists/" + gist_id,
        data=json.dumps({"files": {os.path.basename(file): {"content": content}}}),
        headers=headers,
    )

    return r


def main():
    gists = [
        {
            "gist_id": "5e96ab8a117b7f749315a31382f3fc74",
            "file": "/mnt/c/Users/Tyler/AppData/Roaming/Code/User/settings.json",
        },
        {
            "gist_id": "d52085e30929c9ed6cb0904ca533168f",
            "file": "/mnt/c/Users/Tyler/AppData/Roaming/Code/User/keybindings.json",
        },
        {
            "gist_id": "33a7eeaddb40c945e19b31af199ed042",
            "file": "/mnt/c/Users/Tyler/AppData/Local/Packages/Microsoft.WindowsTerminal_8wekyb3d8bbwe/LocalState/settings.json",
        },
    ]

    headers = {
        "Authorization": f"Bearer {os.environ.get('GITHUB_TOKEN')}",
        "X-GitHub-Api-Version": "2022-11-28",
    }

    for gist in gists:
        r = upload_file_to_gist(gist["gist_id"], gist["file"], headers)
        if r.status_code == 200:
            print(f"Gist Id {gist['gist_id']} updated successfully")
        else:
            print(f"Failed to update Gist Id {gist['gist_id']}: {r.content}")


if __name__ == "__main__":
    main()
