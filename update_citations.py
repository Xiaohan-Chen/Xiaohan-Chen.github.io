from scholarly import scholarly
import json
from datetime import datetime
import os

# Your Google Scholar ID
GOOGLE_SCHOLAR_ID = '0TOReDoAAAAJ'

# Fetch author data
author = scholarly.search_author_id(GOOGLE_SCHOLAR_ID)
scholarly.fill(author, sections=['basics', 'indices', 'counts', 'publications'])

# Update timestamp
author['updated'] = str(datetime.now())
author['publications'] = {v['author_pub_id']:v for v in author['publications']}

print(f"Author: {author['name']}")
print(f"Citations: {author['citedby']}")

# Create results directory
os.makedirs('results', exist_ok=True)

# Save full data
with open('results/gs_data.json', 'w', encoding='utf-8') as outfile:
    json.dump(author, outfile, ensure_ascii=False, indent=2)

# Save shields.io compatible data
shieldio_data = {
    "schemaVersion": 1,
    "label": "citations",
    "message": f"{author['citedby']}",
}
with open('results/gs_data_shieldsio.json', 'w', encoding='utf-8') as outfile:
    json.dump(shieldio_data, outfile, ensure_ascii=False, indent=2)

print("✓ Citation data updated successfully!")
