def format_flight_itineraries(itineraries):
    result = []
    for i, (traveler_name, origin, destination) in enumerate(itineraries, start=1):
        result.append(f"Itinerary {i}: {traveler_name} - From {origin} to {destination}")
    return "\n".join(result)

# Example usage
itineraries = [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]
formatted_itineraries = format_flight_itineraries(itineraries)
print(formatted_itineraries)
