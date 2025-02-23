import requests
import sys

# Function to get the public IP of the machine
def get_ip():
    try:
        ip = requests.get("https://ifconfig.me").text.strip()  # Get the public IP from the ifconfig.me service
        return ip
    except requests.RequestException:
        return None  # Return None if there's an error in the request

# Function to get data related to a given IP
def get_data(ip=None):
    if ip is None:
        print("Something went wrong")
        exit()  # Exit the program if no IP is provided
    
    try:
        response = requests.get(f"https://ip.guide/{ip}")  # Send a request to get data for the IP from ip.guide
        if response.status_code == 200:
            return response.text  # Return the response data if successful
        else:
            print("Could not get data for the IP")
            exit()  # Exit the program if the response status is not 200
    except requests.RequestException:
        print("Error making the request")
        exit()  # Exit the program if there was an error in the request

if __name__ == "__main__":
    # Check if the script is run directly and if an IP was passed as a command-line argument
    if len(sys.argv) > 1:
        ip = sys.argv[1]  # Take the IP from the command-line argument
    else:
        ip = get_ip()  # If no IP is provided, get the public IP automatically

    if ip:
        data = get_data(ip)  # Get the data for the IP
        print(data)  # Print the retrieved data
    else:
        print("Could not get the IP")  # Print an error if no IP could be obtained

