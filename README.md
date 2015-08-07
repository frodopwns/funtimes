#Coding Challenge

#Challenge 1 - Race Average

    python challenge_one.py

#Challenge 2 - MaxMind GeoLite API

Download the csv source data from [here](http://geolite.maxmind.com/download/geoip/database/GeoLiteCity_CSV/GeoLiteCity-latest.zip)
When starting challenge_two.py the code will load the csv's into memory before starting the web server.  This should take under 5 seconds.

Extract the files into the project directory.

    .
    ├── challenge_one.py
    ├── challenge_two.py
    ├── GeoLiteCity-Blocks.csv
    ├── GeoLiteCity-Location.csv
    └── README.md

    sudo pip install flask
    python challenge_two.py

From another terminal:

    curl http://127.0.0.1:5000/167.792.6.4
    {
      "areaCode": "",
      "city": "Guangzhou",
      "country": "CN",
      "latitude": "23.1167",
      "locId": "47667",
      "longitude": "113.2500",
      "metroCode": "",
      "postalCode": "",
      "region": "30"
    }

---
test
