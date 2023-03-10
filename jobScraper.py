# Imports for program function

import time
from datetime import datetime, timedelta

import pandas as pd
from bs4 import BeautifulSoup
from pytz import timezone
from selenium import webdriver
from selenium.common import ElementNotInteractableException, ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class jobScraper:

    def __init__(self, topic, countries, driver_path, links_needed, time_out, broswer_vis, timezone):
        """Initializes the class, sets the variables and customizes scraping"""

        self.links_collected = 0
        self.num_links_needed = links_needed
        self.driver_path = driver_path
        self.time_out = time_out
        self.timezone = timezone

        sel_service = Service(self.driver_path)
        option = webdriver.ChromeOptions()

        # Disable asking for location prompts or tracking location, as it may affect which jobs are shown
        option.add_argument('--deny-permission-prompts')
        option.add_argument('--disable-geolocation')

        # Use chrome incognito
        if not broswer_vis:
            option.add_argument("--window-size=1920,1080")
            option.add_argument("--headless")
            user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) ' \
                         'Chrome/108.0.0.0 Safari/537.36 '
            option.add_argument(f'user-agent={user_agent}')

        # Get the country/state/city from the list of countries, set the URL, Scrape, then save

        for country_state in countries:
            if self.num_links_needed > self.links_collected:
                self.driver = webdriver.Chrome(service=sel_service, options=option)
                self.driver.get(f"https://www.google.com/search?q={topic}+Jobs+{country_state.replace(' ', '+')}")
                self.saveToCsv(self.getJobData(), country_state.replace(' ', '_'))
                self.driver.delete_cookie("CONSENT")
                self.driver.close()

            else:
                break

    def getJobData(self):
        """Scrolls down, gets a job postings data, and then continues until it reaches the end"""

        time.sleep(self.time_out)

        # Click on the Jobs tab and select the list we will scroll

        try:

            self.driver.find_element(By.ID, "fMGJ3e").click()
            job_list = self.driver.find_element(By.CLASS_NAME, 'zxU94d')
            # Contain all the data saved to the csv
            all_job_data = list()

            li_count = 0

            while self.num_links_needed > self.links_collected:

                # Finds multiple lists of jobs in the scrollable div
                li_focus = self.driver.find_elements(By.CLASS_NAME, "nJXhWc")

                # Checks if we reached the end of the scrollable div
                if len(li_focus) < li_count + 1:
                    break

                # Clicks on the job postings in the li and stores the data
                for li in li_focus[li_count].find_elements(By.TAG_NAME, "li"):

                    post_data = {}
                    try:
                        li.click()

                    except (ElementNotInteractableException, ElementClickInterceptedException):
                        self.driver.execute_script(
                            f'arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', job_list
                        )

                    time.sleep(self.time_out)

                    # Get HTML of only specific job posting
                    bSoup = BeautifulSoup(self.driver.find_element(By.ID, "tl_ditsc").get_attribute("outerHTML"),
                                          'html.parser')

                    jobDetail = bSoup.findAll("div", {"class": "I2Cbhb"})

                    # Default values
                    post_data["Job-Type"] = "NA"
                    post_data["Date-Posted"] = "NA"
                    post_data["Salary"] = "NA"

                    post_data["Job-Title"] = bSoup.find("h2").text
                    post_data["Date-Scraped"] = f"{datetime.now(timezone(self.timezone)).strftime('%Y-%m-%d %H:%M:%S')}"
                    # Gets the job type, date posted, and salary
                    for element in jobDetail:

                        if element.text in ("Full-time", "Part-time", "Internship", "Contractor"):

                            post_data["Job-Type"] = element.text

                        elif "ago" in element.text:

                            if "day" in element.text:

                                post_data["Date-Posted"] = (
                                    (datetime.now() - timedelta(days=(int(element.text[0:2].strip())))).astimezone(
                                        timezone(self.timezone)).strftime("%Y-%m-%d"))

                            else:
                                post_data["Date-Posted"] = datetime.now().astimezone(timezone(self.timezone)).strftime(
                                    "%Y-%m-%d")
                                print(post_data["Date-Posted"])

                        elif "a year" in element.text:
                            post_data["Salary"] = element.text

                    post_data["Url"] = self.driver.current_url
                    post_data["Company"] = bSoup.findAll("div", {"class": "nJlQNd"})[0].text
                    post_data["Location"] = bSoup.findAll("div", {"class": "sMzDkb"})[1].text
                    post_data["Description"] = bSoup.find("span",
                                                          {"class": "HBvzbc"}).text

                    self.links_collected += 1
                    all_job_data.append(post_data)

                # Scroll down to the next list of jobs
                self.driver.execute_script(
                    f'arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', job_list
                )

                li_count += 1
                time.sleep(self.time_out)

                # Tracks progress
                print(f"{self.links_collected} / {self.num_links_needed}")

            print(all_job_data)
            return all_job_data

        except NoSuchElementException:
            return None




    def saveToCsv(self, data, country):
        """"Saves the data to a csv file and overwrites any previous data"""

        if data != None:

            df = pd.DataFrame(data,
                              columns=["Job-Title", "Date-Posted", "Date-Scraped", "Url", "Company", "Job-Type", "Salary",
                                       "Location", "Description"])
            df.to_csv(f'data/unprocessedData/machineLearningJobData{country}.csv', mode='w', index=False)
            print("Data Saved")
            print(df)

        else:
            print("No Data Saved")