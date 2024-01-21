import json
import logging
import os
from pathlib import Path

import requests
from dotenv import load_dotenv

parents_dir = Path(__file__).parent.absolute().parent
data_dir = parents_dir / "data"
logs_dir = parents_dir / "logs"

logs_dir.mkdir(exist_ok=True)

logging.basicConfig(
    filename=logs_dir / "gist_uploads.log",
    format="%(asctime)s - %(message)s",
    level=logging.INFO,
)

logger = logging.getLogger(__name__)

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
    headers = {
        "Authorization": f"Bearer {os.environ.get('GITHUB_TOKEN')}",
        "X-GitHub-Api-Version": "2022-11-28",
    }

    with open(data_dir / "gists.json", "r") as f:
        gists = json.loads(f.read())

    for gist in gists:
        r = upload_file_to_gist(gist["gist_id"], gist["file"], headers)
        if r.status_code == 200:
            logger.info(f"Gist Id {gist['gist_id']} updated successfully")
        else:
            logger.error(f"Failed to update Gist Id {gist['gist_id']}: {r.content}")


if __name__ == "__main__":
    main()
