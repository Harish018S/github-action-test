import requests
import os
import json

def fetch_and_save_data(api_url, output_filename):
    # Ensure we only write inside /data/
    output_path = os.path.join("data", output_filename)

    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an error for HTTP errors

        # Save the response content
        with open(output_path, "w", encoding="utf-8") as file:
            if response.headers.get("Content-Type") == "application/json":
                json.dump(response.json(), file, indent=4)
            else:
                file.write(response.text)

        print(f"Data saved successfully to {output_path}")
        return {"status": "success", "message": f"Data saved to {output_path}"}

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return {"status": "error", "message": str(e)}

# Example usage
if __name__ == "__main__":
    api_url = "https://jsonplaceholder.typicode.com/posts"  # Change this to your API URL
    output_filename = "api_data.json"  # Change this to your preferred filename
    fetch_and_save_data(api_url, output_filename)
