import json
from facebook_reels_video_scraper import FacebookReelsVideoScraperClient

rows = FacebookReelsVideoScraperClient().run({'profileUrls': ['https://www.facebook.com/facebook'],
 'maxReelsPerProfile': 200,
 'downloadMp4': True})
with open("results.json", "w", encoding="utf-8") as handle:
    json.dump(rows, handle, ensure_ascii=False, indent=2)
