from facebook_reels_video_scraper import FacebookReelsVideoScraperClient

client = FacebookReelsVideoScraperClient()
rows = client.run({'profileUrls': ['https://www.facebook.com/facebook'],
 'maxReelsPerProfile': 200,
 'downloadMp4': True})
print(rows[0] if rows else "No results")
