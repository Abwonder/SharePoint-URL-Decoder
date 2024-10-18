import urllib.parse

def extract_sharepoint_url(encoded_url):
    # Split the URL into base and query parameters
    url_parts = urllib.parse.urlsplit(encoded_url)
    
    # Base URL without query parameters
    base_url = url_parts.scheme + "://" + url_parts.netloc + url_parts.path
    
    # Decode query parameters
    query_params = urllib.parse.parse_qs(url_parts.query)
    
    # Decode each component in the query parameters
    decoded_params = {key: [urllib.parse.unquote(value) for value in values] for key, values in query_params.items()}
    
    # Construct the final decoded URL and parameters
    print(f"\nBase URL: {base_url}\n")
    
    print("Decoded Query Parameters:")
    for param, value in decoded_params.items():
        print(f"{param}: {value[0]}")

    # Return the decoded parts if needed programmatically
    return base_url, decoded_params


# Main part of the script to take input from the user
if __name__ == "__main__":
    # Request input from the user for the SharePoint URL
    encoded_sharepoint_url = input("Please enter the encoded SharePoint URL: ")

    # Call the function to decode the provided URL
    extract_sharepoint_url(encoded_sharepoint_url)
