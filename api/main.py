from scrapers.scraper_factory import ScraperFactory
from settings import SITES
from flask import Flask, jsonify, request, Response

app = Flask(__name__)

@app.route("/candidates", methods = ["GET"])
def get_candidates():
    job_title = request.args.get('job_title', '')
    skills = request.args.get('skills', [])
    location = request.args.get('location', '')
    results = []
    global scrapers
    for _, scraper in scrapers.items():
        results.append(scraper.scrape_candidates(job_title, skills, location))
    return jsonify(results), 200

@app.route("/jobs", methods = ["GET"])
def get_jobs():
    job_title = request.args.get('job_title', '')
    skills = request.args.get('skills', [])
    location = request.args.get('location', '')
    results = []
    global scrapers
    for _, scraper in scrapers.items():
        results.append(scraper.scrape_jobs(job_title, skills, location))
    return jsonify(results), 200

def init_scrapers():
    return {platform : ScraperFactory.generate(url, platform) for platform, url in SITES.items()}

def main():
    global scrapers
    scrapers = init_scrapers()
    app.run()

if __name__ == '__main__':
    main()
