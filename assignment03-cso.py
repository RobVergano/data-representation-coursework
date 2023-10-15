# Write a program that retrieves the dataset for the "exchequer account (historical series)" from the CSO, and stores it into a file called "cso.json"

# Module requests to make HTTP requests in Python
import requests
# Module json to handle JSON data in python
import json

# Target URL
url = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/2.0/en"

# Target output file
output_file = "cso.json"

# Function to retrieve data from the URL and to store in the file:
def getall():

    # HTTP GET request: 
    response = requests.get(url)

    # Parse the JSON data:
    data = response.json()

    # Open the output file in write text mode:
    with open(output_file, "wt") as file:
            # Write the JSON data into the output file. "indent=2" to format with 2 spaces indendation.
            json.dump(data, file, indent=2)
         
    print(f"Data successfully retrieved and stored in {output_file}")


if __name__ == "__main__":
    getall()


