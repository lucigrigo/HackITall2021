from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from settings import *

class BestJobsScraper:
    def __init__(self, site_url : str):
        self.site_url = site_url
    
    def scrape_jobs(self, job_title : str, skills : list, location : str):
        options = Options()
        options.headless = True

        driver = webdriver.Chrome(options=options, executable_path=CHROME_DRIVER_PATH)
        
        search_url = self.site_url
        if job_title:
            search_url += '?keyword='
            words = job_title.split(' ')
            for idx, word in enumerate(words):
                search_url += word
                if idx != len(words) - 1:
                    search_url += '+'
        
        if skills:
            for idx, skill in enumerate(skills):
                search_url += str(skill)
                if idx != len(skills) - 1:
                    search_url += '+'
        
        if location:
            search_url += '&location=' + location
        search_url += '&sort=relevant'

        jobs = {}
        driver.get(search_url)
        job_cards = driver.find_elements(By.XPATH, "//*[@id=\"app-main-content\"]/div/div/div")
        for idx, job_card in enumerate(job_cards):
            if idx == MAX_JOBS:
                break
            crt_company = job_card.get_attribute('data-employer-name')
            if not crt_company:
                break
            crt_job_title = job_card.get_attribute('data-title')
            if not crt_job_title:
                break
            crt_job_link = job_card.find_element(By.TAG_NAME, 'a').get_attribute('href')
            if not crt_job_link:
                break
            jobs[(crt_job_title, crt_company)] = crt_job_link

        return jobs

    def scrape_candidates(self, job_title : str, skills : list, location : str):
        return {}
