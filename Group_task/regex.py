import re

api_response = "Freedom restaurant - South sudanese cuisine"

pattern = r"(.+) - (.+)"
match = re.match(pattern, api_response)
if match:
    restaurant_name = match.group(1)
    cuisine_type = match.group(2)
    print("restaurant name:", restaurant_name)
    print("Cuisine Type:", cuisine_type)

# 2.ingredient lists from recipes

    api_response = "Onion, oil, garlic"

ingredients = re.findall(r"[\w\s]+", api_response)
print("Ingredients:", ingredients)

# 3.RGB color values:

api_response = "rgb(255, 255, 255)"

rgb_values = re.findall(r"^rgb\((\d{3}),\s(\d{3}),\s(\d{3})\)", api_response)
print("RGB Values:", rgb_values)

# 4.Social Meadia usernames:

api_response = "@abrahamkuol"

username = re.search(r"@(\w+)", api_response)
if username:
    print("Username:", username.group(1))

    # 5.Product codes:

    api_response = "ABC123"

product_code = re.search(r"([A-Z]{3}\d{3})", api_response)
if product_code:
    print("Product Code:", product_code.group(1))

# 6.Newsheadlines:

api_response = "Headline: Welcome to care for all"

headline = re.search(r"Headline: (.+)", api_response)
if headline:
    print("Headline:", headline.group(1))

# 7.Event dates and times:

api_response = "Sep 04, 2023 - 11:59 PM"

event_datetime = re.search(r"((\w{3} \d{2}, \d{4}) - (0|1)[0-9]:(0|1|2|3|4|5)[0-9] [AP]M)", api_response)
if event_datetime:
    event_date = event_datetime.group(1)
    event_time = event_datetime.group(2)
    print("Event Time:", event_date)
    print("Event Time:", event_time)

# 8.Email addresses:

api_response = "m.madol@alustudent.com"

email = re.search(r"(^([a-zA-Z0-9._%-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}))", api_response)
if email:
    print("Email:", email.group(1))
