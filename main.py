from crew import TravelPlannerAgent

def main():
    try:
       
        prompt = input("Enter your travel itinerary request: ")
        travel_planner = TravelPlannerAgent()
        

        result = travel_planner.generate_travel_itinerary(prompt)
        
        if result:
            print("Travel Itinerary Generated:")
            print(result)
        else:
            print("Failed to generate itinerary.")
    except Exception as e:
        print(f"Error in main execution: {str(e)}")

if __name__ == "__main__":
    main()
