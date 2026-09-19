import csv
from facebook_reels_video_scraper import FacebookReelsVideoScraperClient

rows = FacebookReelsVideoScraperClient().run({'profileUrls': ['https://www.facebook.com/facebook'],
 'maxReelsPerProfile': 200,
 'downloadMp4': True})
if rows:
    scalar_keys = [k for k, v in rows[0].items() if not isinstance(v, (dict, list))]
    with open("results.csv", "w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=scalar_keys)
        writer.writeheader()
        writer.writerows({k: row.get(k) for k in scalar_keys} for row in rows)
