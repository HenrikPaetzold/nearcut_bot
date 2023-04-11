# Nearcut Appointment Finder

This project searches for free dates on Nearcut pages within a predefined timespan. It was created as a fun little project to help me get an appointment.

## Getting Started

To use this project, you'll need to fill the `Variables.py` file with the following variables:

- `username`: Your Nearcut username (string)
- `password`: Your Nearcut password (string)
- `pyprowl_api_key`: Your Prowl API key (string)
- `app_name`: The name of the app sending the notification (string)
- `description`: The description of the event (string)
- `priority`: The priority of the notification (int)
- `url`: The URL to include in the notification (string)
- `event_name`: The name of the event (string)

All of these variables should be strings, except for `priority`, which should be an integer.