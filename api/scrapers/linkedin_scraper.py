from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from settings import *
import time

class LinkedInScraper:

    def __init__(self, site_url : str):
        self.site_url = site_url

    def scrape_candidates(self, job_title : str, skills : list, location : str):
        options = Options()
        options.headless = True

        # Very secret credentials:
        email = "softlinksoftsquad@gmail.com"
        password = "hackitall2021"

        # Login
        driver = webdriver.Chrome(options=options, executable_path=CHROME_DRIVER_PATH)
        driver.get('https://www.linkedin.com/login')
        time.sleep(3)
        driver.find_element_by_id('username').send_keys(email)
        driver.find_element_by_id('password').send_keys(password)
        driver.find_element_by_id('password').send_keys(Keys.RETURN)

        # Create URL
        search_url = self.site_url + '/?keywords='

        # Add job title
        if job_title:
            words = job_title.split(' ')
            for idx, w in enumerate(words):
                search_url += str(w)
                if idx != len(words) - 1:
                    search_url += '%20'
            if skills or location:
                search_url += '%20'

        # Add skills
        for idx, skill in enumerate(skills):
            search_url += str(skill)
            if idx != len(skills) - 1:
                search_url += '%20'
            if location:
                search_url += '%20'

        # Add location
        if location:
            search_url += str(location)

        candidates = {}
        for i in range(MAX_LINKED_IN_PAGES):
            if len(candidates) == MAX_CANDIDATES:
                break
            driver.get(search_url + f"&page={i + 1}")
            results = driver.find_elements(By.CLASS_NAME, "entity-result__title-line")
            for r in results:
                profile = r.find_element(By.CLASS_NAME, "app-aware-link")
                profile_url = profile.get_attribute('href')
                if profile_url.startswith(VALID_LINKEDIN_PROFILE_URL):
                    name = r.find_elements(By.CLASS_NAME, "visually-hidden")[0].text[5:-10]
                    candidates[name] = profile_url
        driver.quit()
        return candidates

    def scrape_jobs(self, job_title : str, skills : list, location : str):
        return {}
