from finding_optional_route import find_optional_sequence, calculate_time_route
from dataset import distances, times, place_names

def calculate_delivery_time():
    # Prompt the user for truck details
    height = float(input("Enter the height of the truck: "))
    width = float(input("Enter the width of the truck: "))
    length = float(input("Enter the length of the truck: "))
    capacity = float(input("Enter the capacity of the truck: "))

    # Calculate the area of the truck
    area = height * width * length

    # Prompt the user for the desired delivery time
    desired_delivery_time = float(input("Enter the desired delivery time (in minutes): "))

    # Prompt the user for the route sequence
    route_sequence = input("Enter the route sequence for delivery: ").split()
    place_indices = {place: index for index, place in enumerate(place_names)}
    route_indices = [place_indices[place] for place in route_sequence]

    # Initialize the current location
    current_location = route_indices[0]

    # Initialize the current distance and delivery time
    current_distance = 0
    current_delivery_time = 0
    speed = 40
    loading_unloading_time = 10.55 ## Loading dan unload disini bisa diganti

    # Calculate the delivery time and distances for each step of the route
    for i in range(1, len(route_indices)):
        next_location = route_indices[i]

        # Get the distance and time for the current step
        distance = distances[current_location][next_location]
        time = times[current_location][next_location]

        # Calculate the delivery time for the current step, including loading/unloading time
        current_delivery_time += time + (distance / speed) + loading_unloading_time

        # Update the current location and distance
        current_location = next_location
        current_distance += distance

        # Print the current step information
        print(f"{place_names[route_indices[i - 1]]} -> {place_names[current_location]}")
        print(f"Current Distance: {current_distance}")
        print(f"Current Delivery Time: {current_delivery_time}")
    # Compare the final delivery time with the desired delivery time
    final_delivery_time = calculate_time_route(route_indices, distances, times, loading_unloading_time)
    if final_delivery_time <= desired_delivery_time:
        print("Delivery time is on schedule, no need to change the routes.")
    else:
        # Find the optional sequence
        optimal_sequence = find_optional_sequence(route_sequence, distances, times, desired_delivery_time)
        encoded_optional_sequence = [place_names[place] for place in optimal_sequence]

        print("----------------------------------------------")
        print("The Optional sequence routes: ", encoded_optional_sequence)

        # Calculate the delivery time for the optional sequence
        optional_route_indices = [place_indices[place] for place in encoded_optional_sequence]
        optional_distance = 0
        optional_delivery_time = 0

        for i in range(1, len(optional_route_indices)):
            next_location = optional_route_indices[i]
            distance = distances[current_location][next_location]
            time = times[current_location][next_location]
            optional_delivery_time += time + (distance / speed) + loading_unloading_time
            current_location = next_location
            optional_distance += distance

            # Print the current step information for the optional sequence
            print(f"{place_names[optional_route_indices[i - 1]]} -> {place_names[current_location]}")
            print(f"Current Distance: {optional_distance}")
            print(f"Current Delivery Time: {optional_delivery_time}")

        # Display the optional sequence and delivery time
        
        print("This are the Optional Sequence Delivery Time: ", optional_delivery_time)
        print("Delivery time from original sequences: ", final_delivery_time)

