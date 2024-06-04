import spacy

# Load the medium-sized English model provided by spaCy
nlp = spacy.load("en_core_web_md")

class WeatherChatbot:
    def __init__(self, query) -> None:
        """
        Class to initialize the WeatherChatbot instance.


        Parameters:
        query (str): The user query to be processed.
        """
        # Define the weather-related keywords using spaCy
        self.weather_nlp = nlp("Weather conditions in a city ? sunny windy raining cloudy")
        self.query = query
    
    def chatbot_response(self):
        """
        Validate a location and generate a response 
        based on the user query.

        Returns:
        str: Response to the user query.
        """
        # Process the user query using spaCy
        statement = nlp(self.query)
        min_similarity = 0.5
        
        # Check if the user query is related to weather conditions
        if self.weather_nlp.similarity(statement) >= min_similarity:
            
            # Extract any geographical entities mentioned in the query
            for ent in statement.ents:
                if ent.label_ == "GPE":  # GeoPolitical Entity
                    city = ent.text
                    if city is not None:
                        return city, f"Fetching weather for {city}"
                    else:
                        return "Something went wrong. Please try again"
                else:
                    return "Please include a city to check."
                
        else:
            return "Sorry I don't understand that. Please rephrase your statement including the desired city location."


if __name__ == "__main__":
    # Example usage
    query = input("How can I help you ?\n")
    bot = WeatherChatbot(query=query)
    response = bot.chatbot_response()
    print(response)
