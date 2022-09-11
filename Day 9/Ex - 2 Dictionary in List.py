travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
def add_new_country(name,visits,list1):
  new_entry = {
    "country": name,
    "visits": visits,
    "cities": list1,
  }
  travel_log.append(new_entry)



add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)