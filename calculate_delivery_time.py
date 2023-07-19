from finding_optional_route import find_optional_sequence, calculate_time_route
from dataset import distances, times, place_names

def calculate_delivery_time():
    ## Prompt the user for truck details:
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

    # Calculate the delivery time for the given route sequence
    delivery_time = calculate_time_route(route_indices, distances, times)

    # Compare the delivery time with the desired delivery time
    if delivery_time <= desired_delivery_time:
        print("Delivery time is on schedule, no need to change the routes.")
    else:
        # Find the optional sequence
        optimal_sequence = find_optional_sequence(route_sequence, distances, times, desired_delivery_time)

        # Retrieve all places before the depot (PERUSAHAAN)
        # optional_places = [place for place in optimal_sequence if place != place_indices['PERUSAHAAN'] and place != 'PERUSAHAAN']

        # # Append the depot at the beginning and end of the optional places
        # optional_sequence = ['PERUSAHAAN'] + optional_places + ['PERUSAHAAN']

        # Encode the place names in the optional sequence
        encoded_optional_sequence = [place_names[place] for place in optimal_sequence]


        # Display the optional sequence and delivery time
        print("Optional sequence: ", encoded_optional_sequence)
        print("Delivery time: ", delivery_time)