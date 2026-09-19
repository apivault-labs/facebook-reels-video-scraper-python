import os
from facebook_reels_video_scraper import FacebookReelsVideoScraperClient

if not os.environ.get("APIFY_API_TOKEN"):
    raise SystemExit("Set APIFY_API_TOKEN before running this example")
client = FacebookReelsVideoScraperClient()
print(client.run_one({'profileUrls': ['https://www.facebook.com/facebook'],
 'maxReelsPerProfile': 200,
 'downloadMp4': True}))
