# IP Data Retriever

This Python script retrieves the public IP address of your machine and fetches additional information about that IP using the `ip.guide` service. You can either provide the IP as a command-line argument or let the script automatically fetch your public IP.

## Features

- Automatically fetches your public IP if none is provided.
- Retrieves detailed information about the given IP using the `https://ip.guide/` service.
- Handles errors gracefully and exits the program with a meaningful message if something goes wrong.

## Requirements

- Python 3.x
- `requests` library (you can install it via `pip`)

To install the `requests` library, run:
```bash
pip install requests
