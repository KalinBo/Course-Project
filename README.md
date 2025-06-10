# Selenium WebDriver 4 with Python

## Test Case Overview
This project automates the following scenario:
- Enter the website & Login
- Find a specific course
- Select and enroll in the course
- Enter fake bank card information
- Detect the final error
- Report a successful test

## Resources
The project uses the framework and knowledge gained during the course.

## Main Directorys/Files
- page/course_page.py
- tests/course_test.py
- conftest.py
- base/basepage.py
- base/selenium_webdriver.py
- utilities/util.py
- utilities/custom_logger.py
- utilities/teststatus.py
  
## Base URL
- 'https://www.letskodeit.com/practice'

## How to use
pytest tests/course_test.py
you can add --browser to test with all 3 supported: edge, firefox, chrom(dafault)
