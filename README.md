# 🎬 Cinema Locations Map

香港電影院位置地圖 — 每週自動從 CCIEDA HK 更新。

## 數據源
- [CCIEDA HK Cinemas CSV](https://www.ccidahk.gov.hk/data/hkcinemas.csv)
- 含名稱（中英）、地址、屏幕數、座位數、GPS坐標

## 自動更新
GitHub Actions 每週日 00:00 UTC 執行

## 輸出格式
GeoJSON FeatureCollection，含每間電影院名稱、地址、屏幕數、GPS。
