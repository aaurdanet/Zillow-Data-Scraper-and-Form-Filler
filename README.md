Zillow Data Scraper and Form Filler
Overview

This project is a Python script that scrapes property data (links, prices, and addresses) from a Zillow clone website using BeautifulSoup and then automatically fills in a Google Form with the scraped data using Selenium.
Requirements

    Python 3.x
    beautifulsoup4
    selenium
    requests
    Chrome WebDriver (compatible with your version of Chrome)

Installation

    Clone the repository or download the script file.
    Install the required Python libraries:

    sh

    pip install beautifulsoup4 selenium requests

    Download the Chrome WebDriver from here and make sure it is in your PATH or in the same directory as the script.

Usage

    Ensure you have the Chrome browser installed.
    Run the script:

    sh

    python main.py

Script Details

    Web Scraping: The script uses requests to fetch the HTML content of the Zillow clone website and BeautifulSoup to parse the HTML and extract property links, prices, and addresses.
    Data Cleaning: The extracted data is cleaned and formatted to ensure it is ready for form submission.
    Form Filling: The script uses Selenium to automate the process of filling out a Google Form with the extracted property data.

Important Notes

    Make sure the Chrome WebDriver is compatible with your installed version of Chrome.
    The Google Form URL used in the script should be updated to match your specific form URL if necessary.

