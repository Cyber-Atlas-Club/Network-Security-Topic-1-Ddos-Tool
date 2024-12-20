import threading  # Import threading library to create multiple threads
import requests   # Import requests library to send HTTP requests

# Target URL (change this to your local server for testing)
target_url = "http://your-target-server-url"  # Example: "http://192.168.1.106:80/"

# Function that sends continuous GET requests to the target URL
def send_requests():
    while True:  # Keep sending requests indefinitely
        try:
            response = requests.get(target_url)  # Send GET request
            print(f"Request sent: {response.status_code}")  # Print HTTP status code of the response
        except Exception as e:
            print(f"Error: {e}")  # Print any errors that occur

# Number of threads to simulate
num_threads = 10  # You can change this number to simulate more threads
threads = []

# Create threads to send requests simultaneously
for i in range(num_threads):
    thread = threading.Thread(target=send_requests)  # Create a new thread
    thread.start()  # Start the thread
    threads.append(thread)  # Append the thread to the list of threads

# Wait for all threads to finish (they won't, as they are running indefinitely)
for thread in threads:
    thread.join()
