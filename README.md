Here is an OSINT program for portfolio that can perform various tasks such as social media scraping, web scraping, and image scraping using Python.

This OSINT program uses the following libraries:
- requests: for making HTTP requests to websites
- BeautifulSoup: for parsing HTML content
- selenium: for automating web browser interactions


The OSINT class takes a username as input and initializes a Chrome web driver using Selenium. It also sets up a WebDriverWait object to wait for specific elements to load.

The scrape_social_media method scrapes the latest tweets and posts from the user's Twitter and Facebook profiles using Selenium. It locates the relevant elements using CSS selectors and prints their contents.

The scrape_web method takes a url as input and scrapes the HTML content of the webpage using the requests library and BeautifulSoup. It prints the prettified HTML.

The scrape_images method scrapes images from a given url using Selenium. It locates all the <img> tags and downloads the image files to the local directory.

Finally, the close method closes the web driver to clean up resources.

You can run this program by creating an instance of the OSINT class, passing the desired username as an argument, and calling the desired methods.

Note: Make sure to have the required libraries installed (requests, beautifulsoup4, selenium) and have the appropriate web driver (e.g., ChromeDriver) set up in your system's PATH.

Also, ensure that you have proper permissions and ethical considerations when scraping websites and collecting data from social media profiles.
