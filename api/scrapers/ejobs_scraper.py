from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from settings import *

class EJobsScraper:
    def __init__(self, site_url : str):
        self.site_url = site_url
    
    def scrape_jobs(self, job_title : str, skills : list, location : str):
        options = Options()
        options.headless = True
        driver = webdriver.Chrome(options=options, executable_path=CHROME_DRIVER_PATH)
        search_url = self.site_url

        if location:
            search_url += location + '/'
        
        if job_title:
            words = job_title.split(' ')
            for idx, word in enumerate(words):
                search_url += word
                if idx != len(words) - 1:
                    search_url += '-'
            if skills:
                search_url += '-'
        
        if skills:
            for idx, skill in enumerate(skills):
                search_url += str(skill)
                if idx != len(skills) - 1:
                    search_url += '-'
        
        jobs = {}

        job_titles = driver.find_elements(By.CLASS_NAME, "JCContentMiddle__Title")
        print(job_titles)

        driver.quit()
        return jobs
    
    def scrape_candidates(self, job_title : str, skills : list, location : str):
        return {}