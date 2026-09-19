"""Public exception hierarchy for the Facebook Reels & Video Scraper SDK."""

class FacebookReelsVideoScraperError(Exception):
    """Base SDK error."""

class AuthenticationError(FacebookReelsVideoScraperError):
    """The Apify token is missing or rejected."""

class ActorRunError(FacebookReelsVideoScraperError):
    """The Actor run or Dataset request failed."""

class ActorTimeoutError(FacebookReelsVideoScraperError):
    """The client stopped waiting before the Actor completed."""
