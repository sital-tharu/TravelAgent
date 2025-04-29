from langchain_ollama import OllamaLLM

class TravelPlannerAgent:
    def __init__(self):
        
        self.llm = OllamaLLM(model="llama3")  

    def generate_travel_itinerary(self, prompt):
        try:
          
            result = self.llm(prompt)
            return result 
        except Exception as e:
            print(f"Error generating travel itinerary: {str(e)}")
            return None
