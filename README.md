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
```

## Usage
Run the script without arguments (auto-fetches your public IP):

```bash
python ip_data_retriever.py
```
This will automatically fetch your public IP from the ifconfig.me service and get detailed data for that IP.

## Run the script with a custom IP:
```bash
python ip_data_retriever.py <your-ip-address>
```
Replace <your-ip-address> with any IP you want to get information about. If no IP is provided, the script will fetch your public IP.

## Example Output
If the script successfully retrieves data, you'll see something like:

```vbnet
{
  "ip": "140.82.121.4",
  "network": {
    "cidr": "140.82.121.0/24",
    "hosts": {
      "start": "140.82.121.1",
      "end": "140.82.121.254"
    },
    "autonomous_system": {
      "asn": 36459,
      "name": "GITHUB",
      "organization": "GitHub, Inc.",
      "country": "US",
      "rir": "ARIN"
    }
  },
  "location": {
    "city": "Frankfurt am Main",
    "country": "Germany",
    "timezone": "Europe/Berlin",
    "latitude": 50.1169,
    "longitude": 8.6837
  }
}
```
If there's an error, the script will output an error message like:

```nginx
Something went wrong
```

## License
This project is licensed under the MIT License - see the LICENSE file for details.
