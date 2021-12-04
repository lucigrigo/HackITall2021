import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from settings import *

class HipoScraper:
    def __init__(self, site_url : str):
        self.site_url = site_url
    
    def scrape_jobs(self, job_title : str, skills : list, location : str):
        options = Options()
        options.headless = True
        driver = webdriver.Chrome(options=options, executable_path=CHROME_DRIVER_PATH)

        search_url = self.site_url

        # Location
        if location:
            search_url += '/' + location + '/'
        else:
            search_url += '/Toate-Orasele/'

        # Job Title
        if job_title:
            words = job_title.split(' ')
            for idx, w in enumerate(words):
                search_url += w
                if idx != len(words) - 1:
                    search_url += '-'
            if skills:
                search_url += '-'

        # Skills
        for idx, skill in enumerate(skills):
            search_url += str(skill)
            if idx != len(skills) - 1:
                search_url += '-'

        # Get last page
        driver.get(search_url)
        r = driver.find_element(By.CLASS_NAME, "page-last")
        last_page_url = r.get_attribute("href")
        last_page = int(re.findall(r'\d+', last_page_url)[-1])

        count = 0
        jobs = {}
        for i in range(last_page):
            driver.get(search_url + f"/{i + 1}")
            ret_jobs = driver.find_elements(By.CLASS_NAME, "job-title")
            companies = driver.find_elements(By.CLASS_NAME, "cell-company")
            for i, job in enumerate(ret_jobs):
                company_name = companies[i].find_element(By.TAG_NAME, "span").text
                title = job.get_attribute('title')
                link = job.get_attribute('href')
                jobs[(title, company_name)] = link
                count += 1
                if count == MAX_JOBS:
                    driver.quit()
                    return jobs
        driver.quit()
        return jobs

    def scrape_candidates(self, job_title : str, skills : list, location : str):
        return {}
