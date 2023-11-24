corners = ((1, 1), (1, 12), (28, 1), (28, 12))
state = ((1, 1), ())
for c in corners:
    h = abs(state[0][0] - c[0]) + abs(state[0][1] - c[1])
    print(h)

    corners_list = list(corners)
    visited = []
    all_h = []

    for i in range(len(corners_list)):
        all_h.append(abs(state[0][0] - corners[i][0]) + abs(state[0][1] - corners[i][1]))
    print("all h: ", all_h)
    shortest_h = all_h.index(min(all_h))
    closest_corner = corners[shortest_h]
    real_h = abs(state[0][0] - closest_corner[0]) + abs(state[0][1] - closest_corner[1])
    if state[0] == closest_corner:
        print("State = corner")
        visited.append(closest_corner)
        corners_list.remove(closest_corner)