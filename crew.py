from langchain_ollama import OllamaLLM

# Define a class to handle travel planning using a language model
class TravelPlannerAgent:
    def __init__(self):
        # Initialize the language model with a specific configuration
        self.llm = OllamaLLM(model="llama3")  

    def generate_travel_itinerary(self, prompt):
        try:
            # Use the language model to generate a travel itinerary based on the prompt
            result = self.llm(prompt)
            return result 
        except Exception as e:
            # Handle any errors that occur during itinerary generation
            print(f"Error generating travel itinerary: {str(e)}")
            return None
