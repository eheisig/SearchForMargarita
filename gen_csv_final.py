# NHTSA overall star ratings (AWD/Later Release variants)
nhtsa = {
    ("Nissan",     "Rogue",     "2018"): "4/5",
    ("Nissan",     "Rogue",     "2020"): "4/5",
    ("Nissan",     "Rogue",     "2021"): "4/5",
    ("Hyundai",    "Santa Fe",  "2019"): "5/5",
    ("Hyundai",    "Tucson",    "2019"): "5/5",
    ("Hyundai",    "Tucson",    "2020"): "5/5",
    ("Hyundai",    "Tucson",    "2022"): "4/5",
    ("Subaru",     "Outback",   "2018"): "5/5",
    ("Subaru",     "Forester",  "2020"): "5/5",
    ("Subaru",     "Ascent",    "2019"): "5/5",
    ("Subaru",     "Ascent",    "2022"): "5/5",
    ("Volkswagen", "Tiguan",    "2019"): "5/5",
    ("Volkswagen", "Tiguan",    "2021"): "5/5",
    ("Ford",       "Edge",      "2020"): "5/5",
    ("Ford",       "Edge",      "2022"): "5/5",
    ("Ford",       "Escape",    "2020"): "5/5",
    ("Ford",       "Escape",    "2021"): "5/5",
    ("Ford",       "Escape",    "2022"): "5/5",
}

# IIHS TSP award — "TSP+" / "TSP" / "None"
iihs = {
    ("Nissan",     "Rogue",     "2018"): "TSP",
    ("Nissan",     "Rogue",     "2020"): "TSP",
    ("Nissan",     "Rogue",     "2021"): "TSP+",
    ("Hyundai",    "Santa Fe",  "2019"): "TSP+",
    ("Hyundai",    "Tucson",    "2019"): "TSP+",
    ("Hyundai",    "Tucson",    "2020"): "TSP+",
    ("Hyundai",    "Tucson",    "2022"): "TSP+",
    ("Subaru",     "Outback",   "2018"): "TSP+",
    ("Subaru",     "Forester",  "2020"): "TSP+",
    ("Subaru",     "Ascent",    "2019"): "TSP+",
    ("Subaru",     "Ascent",    "2022"): "TSP+",
    ("Volkswagen", "Tiguan",    "2019"): "TSP+",
    ("Volkswagen", "Tiguan",    "2021"): "TSP",
    ("Ford",       "Edge",      "2020"): "TSP",
    ("Ford",       "Edge",      "2022"): "TSP",
    ("Ford",       "Escape",    "2020"): "TSP",
    ("Ford",       "Escape",    "2021"): "TSP",
    ("Ford",       "Escape",    "2022"): "TSP",
}

# One dict per car — all fields in one place
# Sunroof + driver assist verified via CarMax feature list (name:"..." fields)
# max_cargo = behind front row, all seats folded (cu ft)
cars = [
    {
        "id": "70010384", "year": 2019, "make": "Hyundai", "model": "Santa Fe", "trim": "SE",
        "price": 14998, "miles": 107000, "city_mpg": 22, "hwy_mpg": 28,
        "cargo": 36.4, "cargo_note": "", "drive": "FWD",
        "location": "Charlottesville, VA", "shipping": "Local",
        "owners": 3, "accidents": "1 reported",
        "sunroof": "No", "bsm": "Yes", "lda": "Yes", "acc": "Yes",
        "max_cargo": 61.9,
    },
    {
        "id": "28450487", "year": 2020, "make": "Nissan", "model": "Rogue", "trim": "SV",
        "price": 14998, "miles": 127000, "city_mpg": 25, "hwy_mpg": 32,
        "cargo": 36.5, "cargo_note": "", "drive": "FWD",
        "location": "Potomac Mills, VA", "shipping": "Free",
        "owners": 1, "accidents": "None reported",
        "sunroof": "No", "bsm": "Yes", "lda": "Yes", "acc": "Yes",
        "max_cargo": 61.1,
    },
    {
        "id": "28651739", "year": 2019, "make": "Hyundai", "model": "Tucson", "trim": "Value",
        "price": 14998, "miles": 104000, "city_mpg": 23, "hwy_mpg": 30,
        "cargo": 31.0, "cargo_note": "", "drive": "AWD",
        "location": "Potomac Mills, VA", "shipping": "Free",
        "owners": 2, "accidents": "1 reported",
        "sunroof": "No", "bsm": "Yes", "lda": "Yes", "acc": "No",
        "max_cargo": 56.2,
    },
    {
        "id": "28865931", "year": 2018, "make": "Nissan", "model": "Rogue", "trim": "SL",
        "price": 15998, "miles": 120000, "city_mpg": 25, "hwy_mpg": 32,
        "cargo": 36.5, "cargo_note": "", "drive": "AWD",
        "location": "Dulles, VA", "shipping": "Free",
        "owners": 2, "accidents": "None reported",
        "sunroof": "Yes", "bsm": "Yes", "lda": "Yes", "acc": "Yes",
        "max_cargo": 61.1,
    },
    {
        "id": "28865976", "year": 2019, "make": "Volkswagen", "model": "Tiguan", "trim": "S",
        "price": 16998, "miles": 67000, "city_mpg": 21, "hwy_mpg": 29,
        "cargo": 37.6, "cargo_note": "3rd row folded", "drive": "AWD",
        "location": "Fredericksburg, VA", "shipping": "Free",
        "owners": 1, "accidents": "None reported",
        "sunroof": "No", "bsm": "Yes", "lda": "No", "acc": "No",
        "max_cargo": 65.7,
    },
    {
        "id": "29024102", "year": 2019, "make": "Hyundai", "model": "Tucson", "trim": "Sport",
        "price": 16998, "miles": 80000, "city_mpg": 23, "hwy_mpg": 30,
        "cargo": 31.0, "cargo_note": "", "drive": "FWD",
        "location": "West Broad (Richmond), VA", "shipping": "Free",
        "owners": 2, "accidents": "None reported",
        "sunroof": "No", "bsm": "Yes", "lda": "Yes", "acc": "No",
        "max_cargo": 56.2,
    },
    {
        "id": "28373451", "year": 2018, "make": "Subaru", "model": "Outback", "trim": "2.5i Touring",
        "price": 17998, "miles": 109000, "city_mpg": 25, "hwy_mpg": 32,
        "cargo": 32.5, "cargo_note": "", "drive": "AWD",
        "location": "Charlottesville, VA", "shipping": "Local",
        "owners": 2, "accidents": "None reported",
        "sunroof": "Yes", "bsm": "Yes", "lda": "Yes", "acc": "Yes",
        "max_cargo": 73.3,
    },
    {
        "id": "28738972", "year": 2020, "make": "Ford", "model": "Escape", "trim": "SE",
        "price": 17998, "miles": 50000, "city_mpg": 26, "hwy_mpg": 33,
        "cargo": 37.5, "cargo_note": "", "drive": "AWD",
        "location": "Dulles, VA", "shipping": "Free",
        "owners": 2, "accidents": "None reported",
        "sunroof": "No", "bsm": "Yes", "lda": "Yes", "acc": "Yes",
        "max_cargo": 65.4,
    },
    {
        "id": "70037532", "year": 2019, "make": "Hyundai", "model": "Santa Fe", "trim": "SE",
        "price": 17998, "miles": 71000, "city_mpg": 22, "hwy_mpg": 28,
        "cargo": 36.4, "cargo_note": "", "drive": "FWD",
        "location": "West Broad (Richmond), VA", "shipping": "Free",
        "owners": 4, "accidents": "None reported",
        "sunroof": "No", "bsm": "Yes", "lda": "Yes", "acc": "Yes",
        "max_cargo": 61.9,
    },
    {
        "id": "28866181", "year": 2019, "make": "Hyundai", "model": "Tucson", "trim": "Limited",
        "price": 17998, "miles": 79000, "city_mpg": 23, "hwy_mpg": 30,
        "cargo": 31.0, "cargo_note": "", "drive": "AWD",
        "location": "Dulles, VA", "shipping": "Free",
        "owners": 3, "accidents": "None reported",
        "sunroof": "No", "bsm": "Yes", "lda": "Yes", "acc": "No",
        "max_cargo": 56.2,
    },
    {
        "id": "27968880", "year": 2020, "make": "Ford", "model": "Edge", "trim": "Titanium",
        "price": 18998, "miles": 78000, "city_mpg": 21, "hwy_mpg": 29,
        "cargo": 39.2, "cargo_note": "", "drive": "FWD",
        "location": "Charlottesville, VA", "shipping": "Local",
        "owners": 2, "accidents": "1 reported",
        "sunroof": "Yes", "bsm": "Yes", "lda": "Yes", "acc": "Yes",
        "max_cargo": 73.4,
    },
    {
        "id": "27969408", "year": 2021, "make": "Nissan", "model": "Rogue", "trim": "SV",
        "price": 18998, "miles": 86000, "city_mpg": 25, "hwy_mpg": 32,
        "cargo": 36.5, "cargo_note": "", "drive": "AWD",
        "location": "Charlottesville, VA", "shipping": "Local",
        "owners": 1, "accidents": "None reported",
        "sunroof": "Yes", "bsm": "Yes", "lda": "Yes", "acc": "Yes",
        "max_cargo": 74.1,
    },
    {
        "id": "28909624", "year": 2021, "make": "Ford", "model": "Escape", "trim": "SE",
        "price": 18998, "miles": 49000, "city_mpg": 26, "hwy_mpg": 33,
        "cargo": 37.5, "cargo_note": "", "drive": "AWD",
        "location": "Lynchburg, VA", "shipping": "Free",
        "owners": 2, "accidents": "None reported",
        "sunroof": "No", "bsm": "Yes", "lda": "Yes", "acc": "No",
        "max_cargo": 65.4,
    },
    {
        "id": "28909749", "year": 2022, "make": "Ford", "model": "Edge", "trim": "SEL",
        "price": 18998, "miles": 73000, "city_mpg": 21, "hwy_mpg": 29,
        "cargo": 39.2, "cargo_note": "", "drive": "AWD",
        "location": "Potomac Mills, VA", "shipping": "Free",
        "owners": 3, "accidents": "None reported",
        "sunroof": "No", "bsm": "Yes", "lda": "Yes", "acc": "No",
        "max_cargo": 73.4,
    },
    {
        "id": "28909274", "year": 2021, "make": "Ford", "model": "Escape", "trim": "SE",
        "price": 18998, "miles": 39000, "city_mpg": 26, "hwy_mpg": 33,
        "cargo": 37.5, "cargo_note": "", "drive": "AWD",
        "location": "Fredericksburg, VA", "shipping": "Free",
        "owners": 1, "accidents": "None reported",
        "sunroof": "No", "bsm": "Yes", "lda": "Yes", "acc": "No",
        "max_cargo": 65.4,
    },
    {
        "id": "28377761", "year": 2021, "make": "Volkswagen", "model": "Tiguan", "trim": "S",
        "price": 18998, "miles": 52000, "city_mpg": 22, "hwy_mpg": 29,
        "cargo": 37.6, "cargo_note": "3rd row folded", "drive": "AWD",
        "location": "Roanoke, VA", "shipping": "Free",
        "owners": 2, "accidents": "None reported",
        "sunroof": "No", "bsm": "No", "lda": "No", "acc": "No",
        "max_cargo": 65.7,
    },
    {
        "id": "28680203", "year": 2021, "make": "Nissan", "model": "Rogue", "trim": "S",
        "price": 19998, "miles": 60000, "city_mpg": 25, "hwy_mpg": 32,
        "cargo": 36.5, "cargo_note": "", "drive": "AWD",
        "location": "Charlottesville, VA", "shipping": "Local",
        "owners": 1, "accidents": "None reported",
        "sunroof": "No", "bsm": "Yes", "lda": "No", "acc": "No",
        "max_cargo": 74.1,
    },
    {
        "id": "28373710", "year": 2020, "make": "Subaru", "model": "Forester", "trim": "Premium",
        "price": 19998, "miles": 89000, "city_mpg": 26, "hwy_mpg": 33,
        "cargo": 35.4, "cargo_note": "", "drive": "AWD",
        "location": "Charlottesville, VA", "shipping": "Local",
        "owners": 2, "accidents": "None reported",
        "sunroof": "Yes", "bsm": "No", "lda": "Yes", "acc": "Yes",
        "max_cargo": 76.1,
    },
    {
        "id": "28439685", "year": 2020, "make": "Nissan", "model": "Rogue", "trim": "S",
        "price": 19998, "miles": 40000, "city_mpg": 25, "hwy_mpg": 32,
        "cargo": 36.5, "cargo_note": "", "drive": "AWD",
        "location": "Lynchburg, VA", "shipping": "Free",
        "owners": 1, "accidents": "None reported",
        "sunroof": "No", "bsm": "No", "lda": "No", "acc": "No",
        "max_cargo": 61.1,
    },
    {
        "id": "28909666", "year": 2019, "make": "Subaru", "model": "Ascent", "trim": "Touring",
        "price": 19998, "miles": 101000, "city_mpg": 20, "hwy_mpg": 26,
        "cargo": 47.5, "cargo_note": "3rd row folded", "drive": "AWD",
        "location": "Potomac Mills, VA", "shipping": "Free",
        "owners": 4, "accidents": "None reported",
        "sunroof": "Yes", "bsm": "Yes", "lda": "Yes", "acc": "Yes",
        "max_cargo": 86.5,
    },
    {
        "id": "28680174", "year": 2021, "make": "Ford", "model": "Escape", "trim": "SE",
        "price": 19998, "miles": 37000, "city_mpg": 26, "hwy_mpg": 33,
        "cargo": 37.5, "cargo_note": "", "drive": "AWD",
        "location": "West Broad (Richmond), VA", "shipping": "Free",
        "owners": 1, "accidents": "None reported",
        "sunroof": "No", "bsm": "Yes", "lda": "Yes", "acc": "No",
        "max_cargo": 65.4,
    },
    {
        "id": "27881699", "year": 2022, "make": "Hyundai", "model": "Tucson", "trim": "SEL",
        "price": 19998, "miles": 61000, "city_mpg": 26, "hwy_mpg": 33,
        "cargo": 38.0, "cargo_note": "", "drive": "AWD",
        "location": "Potomac Mills, VA", "shipping": "Free",
        "owners": 2, "accidents": "None reported",
        "sunroof": "No", "bsm": "Yes", "lda": "Yes", "acc": "Yes",
        "max_cargo": 74.8,
    },
    {
        "id": "28909302", "year": 2019, "make": "Subaru", "model": "Ascent", "trim": "Touring",
        "price": 19998, "miles": 109000, "city_mpg": 20, "hwy_mpg": 26,
        "cargo": 47.5, "cargo_note": "3rd row folded", "drive": "AWD",
        "location": "Dulles, VA", "shipping": "Free",
        "owners": 3, "accidents": "None reported",
        "sunroof": "Yes", "bsm": "Yes", "lda": "Yes", "acc": "Yes",
        "max_cargo": 86.5,
    },
    {
        "id": "28652426", "year": 2022, "make": "Subaru", "model": "Ascent", "trim": "Limited",
        "price": 19998, "miles": 127000, "city_mpg": 20, "hwy_mpg": 26,
        "cargo": 47.5, "cargo_note": "3rd row folded", "drive": "AWD",
        "location": "Potomac Mills, VA", "shipping": "Free",
        "owners": 1, "accidents": "None reported",
        "sunroof": "Yes", "bsm": "Yes", "lda": "Yes", "acc": "Yes",
        "max_cargo": 86.5,
    },
    {
        "id": "29024060", "year": 2022, "make": "Ford", "model": "Escape", "trim": "SE",
        "price": 19998, "miles": 40000, "city_mpg": 28, "hwy_mpg": 34,
        "cargo": 37.5, "cargo_note": "", "drive": "FWD",
        "location": "West Broad (Richmond), VA", "shipping": "Free",
        "owners": 1, "accidents": "None reported",
        "sunroof": "No", "bsm": "Yes", "lda": "Yes", "acc": "No",
        "max_cargo": 65.4,
    },
    {
        "id": "70014793", "year": 2020, "make": "Hyundai", "model": "Tucson", "trim": "Limited",
        "price": 19998, "miles": 47000, "city_mpg": 23, "hwy_mpg": 30,
        "cargo": 31.0, "cargo_note": "", "drive": "FWD",
        "location": "Charlottesville, VA", "shipping": "Local",
        "owners": 2, "accidents": "None reported",
        "sunroof": "No", "bsm": "Yes", "lda": "Yes", "acc": "No",
        "max_cargo": 56.2,
    },
]

# Generate CSV
header = "#,Year,Make,Model,Trim,Price,Miles,City MPG,Hwy MPG,Cargo (cu ft),Cargo Note,Drive Type,CarMax Location,Shipping,NHTSA Stars,IIHS Award,# Owners,Accident/Damage History,Sunroof,Blind Spot Monitor,Lane Departure Alert,Adaptive Cruise Control,Max Cargo Behind Front Row (cu ft),CarMax URL"
lines = [header]
for i, c in enumerate(cars, 1):
    key = (c["make"], c["model"], str(c["year"]))
    nhtsa_stars = nhtsa.get(key, "")
    iihs_award  = iihs.get(key, "")
    url = f"https://www.carmax.com/car/{c['id']}"
    lines.append(
        f'{i},{c["year"]},{c["make"]},"{c["model"]}","{c["trim"]}",'
        f'{c["price"]},{c["miles"]},{c["city_mpg"]},{c["hwy_mpg"]},'
        f'{c["cargo"]},"{c["cargo_note"]}","{c["drive"]}","{c["location"]}","{c["shipping"]}",'
        f'"{nhtsa_stars}","{iihs_award}",'
        f'{c["owners"]},"{c["accidents"]}","{c["sunroof"]}","{c["bsm"]}","{c["lda"]}","{c["acc"]}",'
        f'{c["max_cargo"]},{url}'
    )

output = '\n'.join(lines)

import os
out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'CarMax_SUV_Results.csv')
with open(out_path, 'w') as f:
    f.write(output)
print("Done — CarMax_SUV_Results.csv written.")
