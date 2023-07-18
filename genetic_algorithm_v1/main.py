from genetic_algorithm_v1.dataset_input_0 import place_name, matrix_distances, time_matrix
from genetic_algorithm_v1.truck_specification import ask_truck_specification, ask_number_of_routes, ask_route_plan_sequence
from genetic_algorithm_v1.genetic_algorithm_1 import genetic_algorithm, calculate_distances_times
from calculating_least_late_value_2 import fitness_function, calculate_late_point

truck_specification = ask_truck_specification() #Asking the truck specifications

# Prompt for route plan sequences:
route_sequence, distances = ask_route_plan_sequence() 

# Calculate distances based on the specification matrix (time matrix)
distances = calculate_distances_times([route_sequence], time_matrix())

# Calculate the late value for the route
late_value = calculate_late_point(distances, truck_specification["speed"], truck_specification["desired_delivery_time"])

# Display the results
print(f"Route Sequence: {' -> '.join(route_sequence)}")
print(f"Distances: {distances}")
print(f"Late Value: {late_value}")

