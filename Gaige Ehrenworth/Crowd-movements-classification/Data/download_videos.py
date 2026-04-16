import csv
import os
from pytubefix import YouTube
import requests

def download_video(source_name, url, output_name, ts_multiplier=None):
    if url == "NOT_FOUND":
        print(f"URL Not Found, skipping...")
        return
    elif os.path.exists(f"./VOI/{source_name}/{output_name}"):
        print(f"{source_name}/{output_name} already exists, skipping...")
        return

    # [ehrengt] dropout switch
    if source_name != "youtube":
        # Send an HTTP GET request to the URL
        response = requests.get(url, stream=True)

        # Check if the request was successful
        if response.status_code == 200:
            # Open a file in binary write mode
            with open(f"./VOI/{source_name}/{output_name}", 'wb') as file:
                # Write the content of the response to the file in chunks
                for chunk in response.iter_content(chunk_size=1024):
                    if chunk:
                        file.write(chunk)
            print("Video downloaded successfully.")
            return
        else:
            print(f"Failed to download video. Status code: {response.status_code}")
            return

    try:
        # Create a YouTube object with additional configuration
        yt = YouTube(
            url,
            use_oauth=True,
            allow_oauth_cache=True
        )
        
        # Get the lowest resolution stream
        video_stream = yt.streams.get_lowest_resolution()
        
        # Download the video
        print(f"Downloading: {yt.title}")
        video_stream.download(output_path="./VOI/" + source_name, filename=output_name)
        print("Download complete!")
    except Exception as e:
        print(f"An error occurred: {e}")

def set_custom_timescale(yt, multiplier):
    # This function is a placeholder for custom timescale handling.
    # PyTube itself does not support direct timescale manipulation,
    # so you would need to handle this at the level of video processing (e.g., using ffmpeg).
    print(f"Custom timescale multiplier set to {multiplier}")

def main():
    try:
        with open('web_urls.csv', mode='r') as file:
            reader = csv.reader(file, delimiter=';')
            
            for row in reader:
                source_name = row[0]
                url = row[1]
                output_name = row[2]
                ts_multiplier = float(row[3].replace(',', '.')) if len(row) > 3 and row[3] else None

                download_video(source_name, url, output_name, ts_multiplier)

    except FileNotFoundError:
        print("File web_urls.csv not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
