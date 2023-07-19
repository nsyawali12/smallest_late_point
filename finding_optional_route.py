from dataset import distances, times, place_names


def calculate_time_route(route_sequence, distances, times):
    total_time = 0
    
    speed = 40  # Default speed
    loading_unloading_time = 10.55  # Loading/unloading time in minutes # Nanti diganti

    for i in range(len(route_sequence) - 1):
        from_place = route_sequence[i]
        to_place = route_sequence[i + 1]
        distance = distances[from_place][to_place]
        time = times[from_place][to_place]
        travel_time = time + (distance / speed)  # Travel time without loading/unloading time
        total_time += travel_time + loading_unloading_time  # Add loading/unloading time
        
    return total_time

def find_optional_sequence(route_sequence, distances, times, desired_delivery_time):
    place_indices = {place: index for index, place in enumerate(place_names)}
    place_indices['PERUSAHAAN'] = 0  # Add the depot with index 0

    route_indices = [place_indices[place] for place in route_sequence]

    optional_sequence = route_indices.copy()
    num_locations = len(route_indices)
    late_points = [0] * num_locations

    for i in range(1, num_locations - 1):
        current_location = optional_sequence[i]
        min_late_point = float('inf')
        min_late_point_location = -1

        for j in range(i + 1, num_locations - 1):
            # Swap current_location with the next location and calculate the new delivery time
            optional_sequence[i], optional_sequence[j] = optional_sequence[j], optional_sequence[i]
            delivery_time = calculate_time_route(optional_sequence, distances, times)

            # Calculate the late point
            late_point = max(0, delivery_time - desired_delivery_time)

            if late_point < min_late_point:
                min_late_point = late_point
                min_late_point_location = j

            # Swap back to the original sequence
            optional_sequence[i], optional_sequence[j] = optional_sequence[j], optional_sequence[i]

        # Swap the current location with the location having the minimum late point
        optional_sequence[i], optional_sequence[min_late_point_location] = optional_sequence[min_late_point_location], optional_sequence[i]
        late_points[i] = min_late_point

    # Remove any occurrence of 'PERUSAHAAN' in the middle of the sequence
    optional_sequence = [optional_sequence[0]] + [place for place in optional_sequence[1:-1] if place != 0] + [optional_sequence[-1]]

    # Append 'PERUSAHAAN' at the end of the sequence
    optional_sequence.append(0)

    return optional_sequence
