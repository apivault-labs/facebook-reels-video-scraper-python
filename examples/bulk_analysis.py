from facebook_reels_video_scraper import FacebookReelsVideoScraperClient

client = FacebookReelsVideoScraperClient()
payload = {'profileUrls': ['https://www.facebook.com/facebook'],
 'maxReelsPerProfile': 200,
 'downloadMp4': True}
# Add more targets or queries to the list fields supported by this Actor.
rows = client.run(payload)
print(f"Received {len(rows)} rows")
