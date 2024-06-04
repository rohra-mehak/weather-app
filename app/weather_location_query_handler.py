import spacy

# Load the medium-sized English model provided by spaCy
nlp = spacy.load("en_core_web_md")

class WeatherLocationQueryHandler:
    def __init__(self, query) -> None:
        """
        Class to initialize the WeatherLocationQueryHandler instance.

        Parameters:
        query (str): The user query to be processed.
        """
        # Define the weather-related keywords using spaCy
        self.weather_nlp = nlp("Weather conditions in a city ? sunny windy raining cloudy")
        self.query = query
    
    def get_response(self):
        """
        Validate a location and generate a response 
        based on the user query.

        Returns:
        str: Response to the user query.
        """
        statement = nlp(self.query)
        min_similarity = 0.5
        
        # Check if the user query is related to weather conditions in 
        # a location
        if self.weather_nlp.similarity(statement) >= min_similarity:
            
            # Extract any geographical entities mentioned in the query
            for ent in statement.ents:
                if ent.label_ == "GPE":
                    location = ent.text
                    if location is not None:
                        return location, f"Fetching weather for {location}"
                    else:
                        return "Something went wrong. Please try again"
                else:
                    return "Please include a location to check."
                
        else:
            return "Sorry I don't understand that. Please rephrase your statement including the desired location."


if __name__ == "__main__":
    # Example usage
    query = input("How can I help you ?\n")
    bot = WeatherLocationQueryHandler(query=query)
    response = bot.get_response()
    print(response)
