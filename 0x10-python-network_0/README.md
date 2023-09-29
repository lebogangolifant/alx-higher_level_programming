# 0x10. Python - Network #0

This project involves creating Bash and Python scripts to perform various network-related tasks. The scripts are created to interact with web servers using the `curl` command or Python.

## Dependencies

- Files scripts are interpreted/compiled on on __Ubuntu 20.04 LTS__ using python3 __(version 3.8.5).__
- **curl:** A command-line tool for transferring data with URLs.
- **pycodestyle (version 2.8.*):** A tool to check Python code against style conventions.

## Project Tasks

| File Name             | Description                                                |
|-----------------------|------------------------------------------------------------|
| `0-body_size.sh`      | Display the size of the response body in bytes.           |
| `1-body.sh`           | Display the body of the response if status code is 200.   |
| `2-delete.sh`         | Send a DELETE request and display the response body.      |
| `3-methods.sh`        | Display the HTTP methods the server accepts.              |
| `4-header.sh`         | Send a GET request with a custom header.                   |
| `5-post_params.sh`    | Send a JSON POST request with specific parameters.         |
| `6-peak.py`           | Python script to find a peak in an integer list.          |
| `100-status_code.sh`  | Display the status code of a request.                     |
| `101-post_json.sh`    | Send a JSON POST request from a file.                     |
| `102-catch_me.sh`     | Trigger a server response with "You got me!" message.     |

## Usage

1. Make the scripts executable by running 
```
chmod +x script_name.sh` for each script.
```
2. Run perform the specified tasks
```
./0-body_size.sh 0.0.0.0:5000
```
3. Test the scripts using the web server running on port 5000 
