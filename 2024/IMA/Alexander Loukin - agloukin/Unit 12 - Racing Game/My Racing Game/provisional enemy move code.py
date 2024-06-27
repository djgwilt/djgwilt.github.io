def enemyMove():

    global enemy_direction
    cell = getEnemyCell()
    cell.className = ""
    enemy_direction = [0,0]
    # enemy needs to check up down left right, this could be a list
    # then work out which which 2 ways are desired
    # then move in that direction
    possible_enemy_directions = []
    
    #check up
    enemy_direction[1] = 1
    test_location = [enemy_position[0], enemy_position[1] + enemy_direction[1]]
    test_cell = getChosenCell(test_location[0], test_location[1])
    if test_cell != None:
        if test_cell.className != "wall":
            possible_enemy_directions.append("up")

    #check down
    enemy_direction[1] = -1
    test_location = [enemy_position[0], enemy_position[1] + enemy_direction[-1]]
    test_cell = getChosenCell(test_location[0], test_location[1])
    if test_cell != None:
        if test_cell.className != "wall":
            possible_enemy_directions.append("down")

    #check right
    enemy_direction[0] = 1
    test_location = [enemy_position[0] + enemy_direction[0], enemy_position[1]]
    test_cell = getChosenCell(test_location[0], test_location[1])
    if test_cell != None:
        if test_cell.className != "wall":
            possible_enemy_directions.append("right")


    #check left
    enemy_direction[0] = -1
    test_location = [enemy_position[0] + enemy_direction[0], enemy_position[-1]]
    test_cell = getChosenCell(test_location[0], test_location[1])
    if test_cell != None:
        if test_cell.className != "wall":
            possible_enemy_directions.append("left")


    #order them by priority
    x_distance = enemy_position[0] - position[0]
    y_distance = enemy_position[1] - position[1]
    priority_list = []

    if abs(x_distance) > abs(y_distance): # if x distance is greater than y distance
        if x_distance > 0:  # if x distance is positive
            if "left" in possible_enemy_directions:
                priority_list.append("left")
        else:
            enemy_direction[0] = 1
            if "right" in possible_enemy_directions:
                priority_list.append("right")

        if y_distance > 0:
            if "up" in possible_enemy_directions:
                priority_list.append("up")
        else:
            if "down" in possible_enemy_directions:
                priority_list.append("down")
        
    else:
        if y_distance > 0:
            if "up" in possible_enemy_directions:
                priority_list.append("up")
        else:
            if "down" in possible_enemy_directions:
                priority_list.append("down")

        if x_distance > 0:  # if x distance is positive
            if "left" in possible_enemy_directions:
                priority_list.append("left")
        else:
            enemy_direction[0] = 1
            if "right" in possible_enemy_directions:
                priority_list.append("right")

    print(priority_list)

    if priority_list[0] == "up":
        enemy_direction[0] = 0
        enemy_direction[1] = 1
    elif priority_list[0] == "down":
        enemy_direction[0] = 0
        enemy_direction[1] = -1
    elif priority_list[0] == "right":
        enemy_direction[0] = 1
        enemy_direction[1] = 0
    elif priority_list[0] == "left":
        enemy_direction[0] = -1
        enemy_direction[1] = 0

    enemy_position[0] += enemy_direction[0]
    enemy_position[1] += enemy_direction[1]

    cell = getEnemyCell()
    cell.className = "enemy"