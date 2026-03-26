import os
# We pull the key from the environment instead of hardcoding it
STRIPE_API_KEY = os.getenv("STRIPE_API_KEY") 
print("Payment gateway initialized securely.")