import os
import requests


def download_photos(urls, folder_path):
    # Create the directory if it doesn't exist
    os.makedirs(folder_path, exist_ok=True)

    for i, url in enumerate(urls):
        response = requests.get(url)
        if response.status_code == 200:
            file_path = f"{folder_path}/photo_{i+1}.jpg"
            with open(file_path, 'wb') as file:
                file.write(response.content)
            print(f"Photo {i+1} downloaded successfully.")
        else:
            print(f"Failed to download photo {i+1}.")


# Example usage
urls = [
    "https://scontent.fhdy2-1.fna.fbcdn.net/v/xxxxxxxxxx",
    "https://example.com/photo2.jpg",
    "https://example.com/photo3.jpg"
]

folder_path = "photos"

download_photos(urls, folder_path)
