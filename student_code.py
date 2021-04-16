import math
from queue import PriorityQueue

# Used Concepts found on this link
# https://www.geeksforgeeks.org/a-search-algorithm/


def shortest_path(map_grid, start_node, goal):

    initial_distance = 0
    road_cost = {start_node: initial_distance}
    came_from = {start_node: None}

    # we use  a priority queue to work as an ordered key-value pair of intersection and cost
    # and to hold unique values of intersections

    queue = PriorityQueue()
    queue.put(start_node, initial_distance)

    while not queue.empty():

        current_node = queue.get()

        # lucky us, our goal is the current node
        if current_node == goal:
            backtrack_to_get_path(came_from, start_node, goal)

        for next_neighbor in map_grid['roads'][current_node]:

            # g() is the current actual distance from start node to target node
            g_score = road_cost[current_node]

            # h() "euclidean_heuristic" which is an estimate of the distance
            # between current and target nodes
            h_score = euclidean_heuristic(
                map_grid['intersections'][current_node], map_grid['intersections'][next_neighbor])

            # f() is the sum of g() and h()
            f_score = g_score + h_score

            # check next_neighbor's g_score and default to infinity
            next_neighbors_g_score = road_cost.get(next_neighbor, float('inf'))

            if f_score < next_neighbors_g_score:

                #  take the lower f_score and make it the g_score of the next_neighbor node
                road_cost[next_neighbor] = f_score

                # update f-score
                f_score += h_score

                # add next_neighbor node to priority queue with updated distance
                queue.put(next_neighbor, f_score)

                # update came_from dict with next neighbor node to come from the current node
                came_from[next_neighbor] = current_node

    return backtrack_to_get_path(came_from, start_node, goal)


def euclidean_heuristic(start_node, goal):
    X = start_node[0] - goal[0]
    Y = start_node[1] - goal[1]

    return math.sqrt((X ** 2) + (Y ** 2))


def backtrack_to_get_path(came_from, start_node, goal):

    node = goal

    path_list = []

    path_list.append(node)

    while node != start_node:
        node = came_from[node]
        path_list.append(node)

    return [node for node in reversed(path_list)]
