import logging

# Configure basic logging to print messages to the console
logging.basicConfig(level=logging.INFO)

def predict(data):
    logging.info("Processing data: %s", data)
    # Your AI/ML logic here
    result = "Prediction result"
    logging.info("Prediction result: %s", result)
    return result
