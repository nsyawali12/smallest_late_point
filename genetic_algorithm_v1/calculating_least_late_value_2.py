from genetic_algorithm_v1.dataset_input_0 import place_name, matrix_distances, time_matrix
from genetic_algorithm_v1.genetic_algorithm_1 import genetic_algorithm

def calculate_late_point(solution, distance_matrix, truck_speed, desired_delivery_time):
    late_point = 0
    for i in range(len(solution) - 1):
        outlet1 = solution[i]
        outlet2 = solution[i + 1]
        distance = distance_matrix(outlet1, outlet2)
        estimated_time = distance / truck_speed
        late_value = estimated_time - desired_delivery_time
        late_point += late_value
    
    return late_point

def fitness_function(solution, distance_matrix, truck_speed, desired_delivery_time):
    late_point = calculate_late_point(solution, distance_matrix, truck_speed, desired_delivery_time)
    return late_point

