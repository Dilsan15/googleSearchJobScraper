from jobProcessing import jobProcessor as jp
from jobScraper import jobScraper as js

# Number of jobs needed to be scraped.
num_of_jobs_needed = 100000

# If we run out of coutries_states to scrape, then the program will stop, regardless of the number_of_jobs.
countries_or_states = ["Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua & Deps", "Argentina",
                       "Armenia", "Australia", "Austria", "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Barbados",
                       "Belarus", "Belgium", "Belize", "Benin", "Bhutan", "Bolivia", "Bosnia Herzegovina", "Botswana",
                       "Brazil", "Brunei", "Bulgaria", "Burkina", "Burundi", "Cambodia", "Cameroon", "Canada",
                       "Cape Verde", "Central African Rep", "Chad", "Chile", "China", "Colombia", "Comoros", "Congo",
                       "Congo {Democratic Rep}", "Costa Rica", "Croatia", "Cuba", "Cyprus", "Czech Republic", "Denmark",
                       "Djibouti", "Dominica", "Dominican Republic", "East Timor", "Ecuador", "Egypt", "El Salvador",
                       "Equatorial Guinea", "Eritrea", "Estonia", "Ethiopia", "Fiji", "Finland", "France", "Gabon",
                       "Gambia", "Georgia", "Germany", "Ghana", "Greece", "Grenada", "Guatemala", "Guinea",
                       "Guinea-Bissau", "Guyana", "Haiti", "Honduras", "Hungary", "Iceland", "India", "Indonesia",
                       "Iran", "Iraq", "Ireland", "Israel", "Italy", "Ivory Coast", "Jamaica", "Japan",
                       "Jordan", "Kazakhstan", "Kenya", "Kiribati", "Korea North", "Korea South", "Kosovo", "Kuwait",
                       "Kyrgyzstan", "Laos", "Latvia", "Lebanon", "Lesotho", "Liberia", "Libya", "Liechtenstein",
                       "Lithuania", "Luxembourg", "Macedonia", "Madagascar", "Malawi", "Malaysia", "Maldives", "Mali",
                       "Malta", "Marshall Islands", "Mauritania", "Mauritius", "Mexico", "Micronesia", "Moldova",
                       "Monaco", "Mongolia", "Montenegro", "Morocco", "Mozambique", "Myanmar, {Burma}", "Namibia",
                       "Nauru", "Nepal", "Netherlands", "New Zealand", "Nicaragua", "Niger", "Nigeria", "Norway",
                       "Oman", "Pakistan", "Palau", "Panama", "Papua New Guinea", "Paraguay", "Peru", "Philippines",
                       "Poland", "Portugal", "Qatar", "Romania", "Russian Federation", "Rwanda", "St Kitts & Nevis",
                       "St Lucia", "Saint Vincent & the Grenadines", "Samoa", "San Marino", "Sao Tome & Principe",
                       "Saudi Arabia", "Senegal", "Serbia", "Seychelles", "Sierra Leone", "Singapore", "Slovakia",
                       "Slovenia", "Solomon Islands", "Somalia", "South Africa", "South Sudan", "Spain", "Sri Lanka",
                       "Sudan", "Suriname", "Swaziland", "Sweden", "Switzerland", "Syria", "Taiwan", "Tajikistan",
                       "Tanzania", "Thailand", "Togo", "Tonga", "Trinidad & Tobago", "Tunisia", "Turkey",
                       "Turkmenistan", "Tuvalu", "Uganda", "Ukraine", "United Arab Emirates", "United Kingdom",
                       "United States", "Uruguay", "Uzbekistan", "Vanuatu", "Vatican City", "Venezuela", "Vietnam",
                       "Yemen", "Zambia", "Zimbabwe"]

# Timezone
scraping_timezone = "Canada/Mountain"

# The topic which we are searching for. This will go into the url
topic = "Machine Learning".replace(" ", "+")

# Path to the webdriver, saved as env variable
driver_path = r"C:\Users\dilsh\Downloads\chromedriver_win32\chromedriver.exe"  # Todo("CHANGE THIS TO UR PATH! so it looks like driver_path = 'YOUR STRING' ")

# time out needed between events, based on Wi-Fi and PC performance
time_out = 0.3

# Boolean which controls if the browser activities will be shown on screen on or not.
browser_visible = False

# Scrape/Process? or only process
type = "scrapeprocess"

if __name__ == "__main__" and type == "scrapeprocess":
    JobScraper = js(topic, countries_or_states, driver_path, num_of_jobs_needed, time_out, browser_visible,
                    scraping_timezone)
    jp()

else:
    jp()
