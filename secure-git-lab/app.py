import os

# This pulls the value from your .env file (Task 4)
API_KEY = os.getenv("API_KEY")

print("Safe Code Running")

# This is just to check if it worked during your lab demo
if API_KEY:
    print(f"API Key loaded safely: {API_KEY}")
else:
    print("No API Key found. (Check your .env file!)")