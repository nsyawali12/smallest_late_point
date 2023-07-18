from genetic_algorithm_v1.dataset_input_0 import time_matrix, place_name
from genetic_algorithm_v1.genetic_algorithm_1 import calculate_distances_times

def calculate_distances(route_sequences):
    distances = []
    for sequence in route_sequences:
        route_distances = []
        for i in range(len(sequence) - 1):
            start = int(sequence[i])
            end = int(sequence[i + 1])
            distance = time_matrix()[start][end]
            route_distances.append(distance)
        distances.append(route_distances)
    return distances

def ask_truck_specification():
    print("Please provide the truck's specifications: ")
    width = float(input("Width (in meters): "))
    length = float(input("Length (in meters): "))
    height = float(input("Height (in meters): "))
    capacity = float(input("Capacity (in Kilograms): "))
    area = float(input("Area (in square meters): "))
    speed = 40 # Default speed truck9
    disired_delivery_time = int(input("Desired delivery time (in minutes): "))

    truck_specification = {
        "width": width,
        "length": length,
        "capacity": capacity,
        "area": area,
        "speed": speed,
        "desired_delivery_time": disired_delivery_time
    }

    return truck_specification

def ask_number_of_routes():
    return int(input("Please enter the number of routes the truck needs to pass: "))

def ask_route_plan_sequence():
    print("Please enter the sequence of places for the route:")
    sequence = input("Enter the place names separated by spaces: ")
    sequence = sequence.split()  # Split the input by spaces to get a list of place names
    encoded_sequence = [place_name().index(place) for place in sequence]  # Encode the place names to their indices
    distances = calculate_distances_times([encoded_sequence], time_matrix())
    return sequence, distances

