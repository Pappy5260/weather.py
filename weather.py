import readline

def get_weather(city):
    api_key = "a55c33b018e4ce1524dde30509bc5a1f"
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q=London,uk&appid=a55c33b018e4ce1524dde30509bc5a1f"
    response = readline.get(base_url)
    data = response.json()

    if data["cod"] == 200:
        description = data["weather"][0]["description"]
        temp = data["main"]["temp"] - 273.15
        return f"The weather in {city} is {description}. The temperature is {temp:.1f}°C."
    else:
        return "City not found."

print("Bot: Hello! I will be glad to give you some weather advice right now.")
while True:
    user_input = input("User: How is today's weather? ")
    if user_input.lower() == "exit":
        print("Bot: Goodbye!")
        break
    elif "weather" in user_input.lower():
        print("Bot: Sure! Could you please tell me the place you are looking at?")
        user_input = input("User: I am curious about the weather in ")
        result = get_weather(user_input)
        print("Bot:", result)
    else:
        print("Bot: I'm sorry, I can only provide weather information. Please ask about the weather.")
