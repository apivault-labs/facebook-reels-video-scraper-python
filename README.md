# Facebook Reels & Video Scraper — Python SDK

Python client for the [Facebook Reels & Video Scraper Apify Actor](https://apify.com/apivault_labs/facebook-reels-video-scraper). Send public Actor inputs, wait for the hosted run, and receive clean Dataset rows without maintaining scraping infrastructure.

[![Apify Actor](https://img.shields.io/badge/Apify-Actor-blue)](https://apify.com/apivault_labs/facebook-reels-video-scraper)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## Results

- Direct URL, search and profile workflows
- MP4 links and public engagement metrics
- Captions and available transcripts
- Date and caption keyword filters

Result availability follows the public page and video visibility. Collection remains inside the hosted Actor.

## Install

```bash
pip install git+https://github.com/apivault-labs/facebook-reels-video-scraper-python.git
```

Create an Apify token at [Console → Integrations](https://console.apify.com/account/integrations), then:

```python
from facebook_reels_video_scraper import FacebookReelsVideoScraperClient

client = FacebookReelsVideoScraperClient(api_token="apify_api_xxxxxx")
rows = client.run({'profileUrls': ['https://www.facebook.com/facebook'],
 'maxReelsPerProfile': 200,
 'downloadMp4': True})
print(rows[0] if rows else "No results")
```

You can set `APIFY_API_TOKEN` instead of passing the token in code.

## Public input options

| Field | Type | Default | Description |
|---|---|---|---|
| `workflow` | `string` | `auto` | Automatically select a URL, search or profile workflow. |
| `startUrls` | `array` | `[]` | Public Reel or video URLs. |
| `searchQueries` | `array` | `[]` | Keywords or hashtags to search. |
| `profileUrls` | `array` | `[]` | Public profile or Page URLs. |
| `maxReelsPerProfile` | `integer` | `200` | Maximum videos per supplied profile. |
| `maxResults` | `integer` | `200` | Maximum total results. |
| `maxCostUsd` | `number` | `0` | Optional Actor charge cap. |
| `sinceDays` | `integer` | `0` | Keep videos from the last N days. |
| `keywordFilter` | `string` | `` | Keep captions containing this text. |
| `enrichDetailPage` | `boolean` | `True` | Request the complete public result when available. |
| `downloadMp4` | `boolean` | `True` | Include an available MP4 URL. |
| `includeTranscript` | `boolean` | `True` | Include available native captions or transcript. |
| `dedupe` | `boolean` | `True` | Return each video once. |
| `outputPreset` | `string` | `full` | Choose a public result layout. |

The complete, versioned schema is also available on the [Actor page](https://apify.com/apivault_labs/facebook-reels-video-scraper).

## Pricing

Pay per delivered result through Apify, starting around **$3/1,000 results** on paid tiers. Free-plan pricing and platform usage can differ; check the Actor page before large runs.

## Examples

- `examples/quickstart.py` — first run
- `examples/bulk_analysis.py` — expand a target list
- `examples/export_csv.py` — save flat result fields
- `examples/save_json.py` — preserve nested output
- `examples/cost_estimate.py` — estimate result-event charges
- `examples/environment_token.py` — keep credentials out of code

## Architecture and privacy

This repository is intentionally a thin API client. Collection, retries, analysis and billing run inside the hosted Apify Actor. No private implementation, credentials, scoring weights or infrastructure configuration are included.

## License

MIT. The hosted Actor is a separate paid service governed by Apify terms.
