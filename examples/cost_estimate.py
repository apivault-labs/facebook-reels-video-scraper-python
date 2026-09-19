from facebook_reels_video_scraper import FacebookReelsVideoScraperClient

for count in (10, 100, 1000):
    print(count, FacebookReelsVideoScraperClient.estimate_cost(count), "USD estimated result charges")
