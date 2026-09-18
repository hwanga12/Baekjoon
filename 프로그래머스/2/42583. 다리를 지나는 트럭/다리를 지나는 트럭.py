from collections import deque


def solution(bridge_length, weight, truck_weights):
    bridge = deque([0] * bridge_length)
    bridge_weight = 0
    next_index = 0
    time = 0

    while next_index < len(truck_weights) or bridge_weight > 0:
        time += 1

        leaving = bridge.popleft()
        bridge_weight -= leaving

        if (
            next_index < len(truck_weights)
            and bridge_weight + truck_weights[next_index] <= weight
        ):
            truck = truck_weights[next_index]
            bridge.append(truck)
            bridge_weight += truck
            next_index += 1
        else:
            bridge.append(0)

    return time