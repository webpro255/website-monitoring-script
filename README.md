# website-monitoring-script
A Python script to automate the monitoring of websites, sending alerts if any site is down.

This repository contains a Python script to automate the monitoring of websites. The script sends HTTP GET requests to specified websites, checks the response status codes, logs the results, and sends email notifications if any sites are down.

## Features

- **Automated Monitoring:** Periodically checks the availability of specified websites.
- **Alert System:** Sends email notifications if a website is down.
- **Logging:** Logs the status of each website check with timestamps.

## Requirements

- Python 3.x
- `requests` library
- Email server for sending notifications

## How to Use

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/website-monitoring-script.git
   cd website-monitoring-script
   ```
2. Install the required libraries:
  ```bash
  pip3 install requests
  ```
3. Update the email configuration in website_monitor.py with your email server details.

4. Run the script:
  ```bash
  python3 website_monitor.py
  ```

   Example
  ```bash
  import requests

  response = requests.get('https://example.com')
  print(response.status_code)
  ```
##  Contributing

Feel free to fork this repository and contribute by submitting a pull request.

## License

This project is licensed under the MIT License.
