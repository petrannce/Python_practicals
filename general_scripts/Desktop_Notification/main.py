import time
from plyer import notification

def send_notification(title, message):
    """Send a desktop notification."""
    notification.notify(
        title=title,
        message=message,
        app_name="Notification App",
        timeout=10  # Notification will be visible for 10 seconds
    )

# Example usage
send_notification("Start Coding", "Clear all your projects backup and start coding!")

# Keep sending notifications every 10 seconds
while True:
    time.sleep(10)  # Wait for 10 seconds before sending the next notification
    send_notification("Reminder", "Don't forget to take breaks while coding!")
    
# pip install plyer