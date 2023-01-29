from jobScraper import jobScraper as js
from jobProcessing import jobProcessor as jp

# Number of jobs needed to be scraped.
num_of_jobs_needed = 1000

# If we run out of coutries_states to scrape, then the program will stop, regardless of the number_of_jobs.
countries_or_states = ["United States California", "India", "United Kingdom London", "Canada Toronto",
                       "Australia Sydney", "New Zealand", "Singapore", "Malaysia", "Hong Kong", "South Africa",
                       "Ireland", "Germany", "France", "Spain", "Italy", "Norway", "Denmark", "Finland",
                       "Netherlands", "Belgium", "Austria", "Switzerland", "Poland",
                       "Russia", "Turkey", "Brazil", "Mexico", "Argentina", "Chile", "Venezuela",
                       "Ecuador", "Uruguay", "Bolivia", "Costa Rica", "Panama", "Dominican Republic",
                       "Puerto Rico", "Pakistan", "Afghanistan"]

# Timezone
scraping_timezone = "Canada/Mountain"

# The topic which we are searching for. This will go into the url
topic = "Machine Learning".replace(" ", "+")

# Path to the webdriver, saved as env variable
driver_path = r"C:\Users\dilsh\Downloads\chromedriver_win32\chromedriver.exe"  # Todo("CHANGE THIS TO UR PATH! so it looks like driver_path = 'YOUR STRING' ")

# time out needed between events, based on Wi-Fi and PC performance
time_out = 0.5

# Boolean which controls if the browser activities will be shown on screen on or not.
browser_visible = False

# Scrape/Process? or only process
type = "process"


if __name__ == "__main__" and type == "scrapeprocess":
     JobScraper = js(topic, countries_or_states, driver_path, num_of_jobs_needed, time_out, browser_visible,
                            scraping_timezone)
     jp()

else:
    jp()