# Lab 3 Melissa De Jesus
# Input: Get the user's preferences
content_type = input("Enter your preferred type of content (e.g., movies, TV shows, sports, documentaries): ").lower()
budget = float(input("Enter your budget for a monthly subscription (e.g., 15): $"))
streams = int(input("Enter the number of simultaneous streams you need: "))

# Decision making to recommend a streaming service ( im not sure what the streams calculate for...)
if content_type == "movies" and budget >= 15:
    recommendation = "Netflix or Amazon Prime"
elif content_type == "tv shows" and 10 <= budget < 15:
    recommendation = "Hulu or Disney+"
elif content_type == "sports" and budget >= 10:
    recommendation = "ESPN+ or DAZN"
elif content_type == "documentaries" and budget < 10:
    recommendation = "CuriosityStream"
else:
    recommendation = "(you input incorrectly or..) no service as you cannot afford any "

# Output the recommendation
print(f"\nBased on your preferences, we recommend {recommendation} for your {content_type} streaming needs.")
print("Enjoy your streaming!")
