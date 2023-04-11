import pyprowl
import Variables

p = pyprowl.Prowl(Variables.pyprowl_api_key)

try:
    p.verify_key()
except Exception as e:
    print(f"Error verifying Prowl API key: {Variables.pyprowl_api_key}")
    exit()

def notify(event_name, description, priority, url, app_name):
    try:
        p.notify(event=event_name, description=description, 
			 priority=priority, url=url, 
			 #apiKey='uncomment and add API KEY here if different', 
			 appName=app_name)
        print("Notification sent")
    except Exception as e:
        print(f"Error sending notification to Prowl: {e}")