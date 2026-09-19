"""Python SDK for the hosted Facebook Reels & Video Scraper Apify Actor."""
from .client import FacebookReelsVideoScraperClient
from .exceptions import FacebookReelsVideoScraperError, AuthenticationError, ActorRunError, ActorTimeoutError

__version__ = "0.1.0"
__all__ = ["FacebookReelsVideoScraperClient", "FacebookReelsVideoScraperError", "AuthenticationError", "ActorRunError", "ActorTimeoutError"]
