import requests

def check_website_status(url):
    """
    Checks the HTTP status code of a website.
    Returns True if the status code is 200 (OK), False otherwise.
    """
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        return True
    except requests.exceptions.RequestException as e:
        print(f"Error checking {url}: {e}")
        return False

def check_social_media_status(social_media):
    """
    Checks the status of given social media platforms.
    """
    social_media_urls = {
        "instagram": "https://www.instagram.com/",
        "facebook": "https://www.facebook.com/",
        "twitter": "https://x.com/",
        "linkedin": "https://www.linkedin.com/",
        "tiktok": "https://www.tiktok.com/",
        "snapchat": "https://www.snapchat.com/",
        "youtube": "https://www.youtube.com/",
    }

    if social_media not in social_media_urls:
      print(f"Invalid social media platform: {social_media}")
      return

    url = social_media_urls[social_media]
    status = check_website_status(url)

    if status:
        print(f"{social_media.capitalize()} is up and running.")
    else:
        print(f"{social_media.capitalize()} might be down or experiencing issues.")

if __name__ == "__main__":
    check_social_media_status("instagram")
    check_social_media_status("facebook")
    check_social_media_status("twitter")
    check_social_media_status("linkedin")
    check_social_media_status("tiktok")
    check_social_media_status("snapchat")
    check_social_media_status("youtube")