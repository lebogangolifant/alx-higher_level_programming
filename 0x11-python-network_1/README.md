# 0x11. Python - Network #1

This project contains Python scripts that demonstrate network-related tasks using Python libraries such as urllib and requests.

## Dependencies

- Files scripts are interpreted/compiled on on __Ubuntu 20.04 LTS__ using python3 __(version 3.8.5).__
- **pycodestyle (version 2.8.*):** A tool to check Python code against style conventions.

## Project Tasks

| File Name              | Description                                      |
|------------------------|--------------------------------------------------|
| 0-hbtn_status.py       | Fetches 'https://alx-intranet.hbtn.io/status' using urllib and displays response details. |
| 1-hbtn_header.py       | Sends a request to a URL and displays the value of the X-Request-Id header using urllib. |
| 2-post_email.py        | Sends a POST request with an email parameter using urllib and displays the response body. |
| 3-error_code.py        | Sends a request to a URL, handles HTTPError exceptions, and displays HTTP status codes. |
| 4-hbtn_status.py       | Fetches 'https://alx-intranet.hbtn.io/status' using the requests library and displays the response. |
| 5-hbtn_header.py       | Sends a request to a URL, retrieves the X-Request-Id header, and displays it using requests. |
| 6-post_email.py        | Sends a POST request with an email parameter and displays the response body using requests. |
| 7-error_code.py        | Sends a request to a URL, handles HTTPError exceptions, and displays HTTP status codes using requests. |
| 8-json_api.py          | Sends a POST request with a letter parameter and displays a formatted response using requests. |
| 10-my_github.py        | Uses Basic Authentication with a personal access token to display your GitHub user ID. |
| 100-github_commits.py  | Lists the 10 most recent commits from a GitHub repository by owner and name using the GitHub API. |


## Usage

 1. Make the scripts executable by running 
```
chmod +x script_name.sh` for each script.
```
2. To run the specified task

```
./script_name.py
```
