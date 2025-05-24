from pytube import YouTube
import re

def sanitize_filename(title):
	return re.sub(r'[\\/*?:"<>|]', "", title)

try:
	url = input("Enter the YouTube video URL: ")
	yt = YouTube(url, use_oauth=True, allow_oauth_cache=True)

	audio_stream = yt.streams.filter(only_audio=True).first()
	if audio_stream:
		safe_title = sanitize_filename(yt.title)
		audio_stream.download(filename=f"{safe_title}.mp3")
		print(f"Audio downloaded as {safe_title}.mp3")
	else:
		print("No audio stream found for this video.")
except Exception as e:
	print(f"An error occurred: {str(e)}")