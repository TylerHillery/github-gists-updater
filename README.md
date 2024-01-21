# Overview

This is a simple python script that I put on a cron job to update GitHub gists. I use it to make sure that my vs code settings and window terminal settings are backed up.

## How to use

If you want to use this script for yourself all you need to do is create a `gists.json` file in the data folder with the following schema: 

```json
[
    {
        "gist_id": "abcdefghikl123456789",
        "file": "/path/to/file.ext"
    },
    {
        "gist_id": "abcdefghikl123456789",
        "file": "/path/to/file.ext"
    },
    {
        "gist_id": "abcdefghikl123456789",
        "file": "/path/to/file.ext"
    }
]
```

Create a `.env` file in the root folder with `GITHUB_TOKEN={{YOUR TOKEN}}` and make sure your token has the `gists` scope.

I have this script log the results of each run to `gists_uploads.logs`.