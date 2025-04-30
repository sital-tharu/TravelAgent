from crew import TravelPlannerAgent

# Entry point of the program
def main():
    try:
        # Prompt the user for a travel itinerary request
        prompt = input("Enter your travel itinerary request: ")

        # Create an instance of TravelPlannerAgent
        travel_planner = TravelPlannerAgent()

        # Generate the travel itinerary based on the user's input
        result = travel_planner.generate_travel_itinerary(prompt)

        # Check if the itinerary was successfully generated and display the result
        if result:
            print("Travel Itinerary Generated:")
            print(result)
        else:
            print("Failed to generate itinerary.")
    except Exception as e:
        # Handle any exceptions that occur during execution
        print(f"Error in main execution: {str(e)}")

# Ensure the script runs only when executed directly
if __name__ == "__main__":
    main()
