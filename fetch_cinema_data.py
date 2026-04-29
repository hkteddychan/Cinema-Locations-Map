#!/usr/bin/env python3
"""Fetch Hong Kong Cinema locations from CCIA HK open data."""
import urllib.request
import json
import csv
from datetime import datetime

CSV_URL = "https://www.ccidahk.gov.hk/data/hkcinemas.csv"
OUTPUT_FILE = "cinema_data.geojson"

def fetch_cinemas():
    req = urllib.request.Request(CSV_URL, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, timeout=30) as response:
        content = response.read().decode('utf-8-sig')
    
    features = []
    reader = csv.DictReader(content.strip().split('\n'))
    for row in reader:
        lon = row.get('longitude_lands', '').strip()
        lat = row.get('latitude_lands', '').strip()
        if not lon or not lat:
            continue
        try:
            lon = float(lon)
            lat = float(lat)
        except ValueError:
            continue
        
        features.append({
            "type": "Feature",
            "geometry": {"type": "Point", "coordinates": [lon, lat]},
            "properties": {
                "name_tc": row.get('Name_TC', '').strip(),
                "name_en": row.get('Name_EN', '').strip(),
                "address_tc": row.get('Address_TC', '').strip(),
                "no_screens": row.get('No_Screen', '').strip(),
                "no_seats": row.get('No_Seat', '').strip(),
                "website": row.get('Website', '').strip(),
                "contact": row.get('Contact_Information', '').strip(),
                "last_update": row.get('Last_Update', '').strip(),
            }
        })
    
    return features

def main():
    print(f"[{datetime.now().isoformat()}] Fetching HK cinema data...")
    features = fetch_cinemas()
    print(f"Found {len(features)} cinemas")
    
    geojson = {
        "type": "FeatureCollection",
        "features": features,
        "updated": datetime.utcnow().isoformat(),
        "count": len(features)
    }
    
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(geojson, f, ensure_ascii=False, indent=2)
    
    print(f"✅ Updated {len(features)} cinemas -> {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
