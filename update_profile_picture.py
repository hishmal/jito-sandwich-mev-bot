import requests

# Your bot token
TOKEN = "7001542183:AAHO-cpFDGNTSUgAUQgaj6zbluNuAflbBCk"
# URL of the image you want to use as the bot's profile picture
IMAGE_URL = "https://pbs.twimg.com/profile_images/1687112115331665923/58-fg4B3_400x400.png"
# Path to save the downloaded image
PHOTO_PATH = "profile_picture.png"

# Download the image
response = requests.get(IMAGE_URL)
if response.status_code == 200:
    with open(PHOTO_PATH, 'wb') as file:
        file.write(response.content)
    print("Image downloaded successfully.")
else:
    print("Failed to download the image.")
    exit()

# Set the downloaded image as the bot's profile picture
url = f"https://api.telegram.org/bot{TOKEN}/setChatPhoto"

with open(PHOTO_PATH, 'rb') as photo:
    files = {'photo': photo}
    response = requests.post(url, files=files, data={'chat_id': f"@JitoSandwichMevBot"})

if response.status_code == 200:
    print("Profile photo updated successfully!")
else:
    print(f"Failed to update profile photo. Status code: {response.status_code}, Response: {response.text}")
