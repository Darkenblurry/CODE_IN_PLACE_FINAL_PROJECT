from graphics import Canvas
import random
import time


CANVAS_WIDTH = 600
CANVAS_HEIGHT = 600
CELL_SIZE = 24
ROWS = 25
COLS = 25

canvas = None
maze = None
player_row = 0
player_col = 0



def move_player(direction):
    global player_row, player_col
    if direction == "up":
        next_row = player_row - 1
        #First we check if it's a wall
        if maze[next_row][player_col] == 0:
            # We move the player by drawing white rectangle over the player
            x1 = player_col * CELL_SIZE
            y1 = player_row * CELL_SIZE
            x2 = x1 + CELL_SIZE
            y2 = y1 + CELL_SIZE
            canvas.create_rectangle(x1, y1, x2, y2, "white")

            #We move the player one square up
            x3 = player_col * CELL_SIZE 
            y3 = player_row * CELL_SIZE - CELL_SIZE
            x4 = x3 + CELL_SIZE
            y4 = y3 + CELL_SIZE
            canvas.create_oval(x3,y3,x4,y4,"blue")

            player_row = next_row
            

    elif direction == "down":
        next_row = player_row + 1

        #First we check if it's a wall, walls equals to 1
        if maze[next_row][player_col] == 0:
            # We move the player by drawing white rectangle over the player
            x1 = player_col * CELL_SIZE
            y1 = player_row * CELL_SIZE
            x2 = x1 + CELL_SIZE
            y2 = y1 + CELL_SIZE
            canvas.create_rectangle(x1, y1, x2, y2, "white")

            #We move the player one square down
            x3 = player_col * CELL_SIZE 
            y3 = player_row * CELL_SIZE + CELL_SIZE
            x4 = x3 + CELL_SIZE
            y4 = y3 + CELL_SIZE
            canvas.create_oval(x3,y3,x4,y4,"blue")

            player_row = next_row


    elif direction == "left":
        next_col = player_col - 1

        #First we check if it's a wall, walls equals to 1
        if maze[player_row][next_col] == 0:
            # We move the player by drawing white rectangle over the player
            x1 = player_col * CELL_SIZE
            y1 = player_row * CELL_SIZE
            x2 = x1 + CELL_SIZE
            y2 = y1 + CELL_SIZE
            canvas.create_rectangle(x1, y1, x2, y2, "white")

            #We move the player one square to the left
            x3 = player_col * CELL_SIZE - CELL_SIZE 
            y3 = player_row * CELL_SIZE 
            x4 = x3 + CELL_SIZE
            y4 = y3 + CELL_SIZE
            canvas.create_oval(x3,y3,x4,y4,"blue")

            player_col = next_col


    elif direction == "right":
        next_col = player_col + 1

        #First we check if it's a wall, walls equals to 1
        if maze[player_row][next_col] == 0:
            # We move the player by drawing white rectangle over the player
            x1 = player_col * CELL_SIZE
            y1 = player_row * CELL_SIZE
            x2 = x1 + CELL_SIZE
            y2 = y1 + CELL_SIZE
            canvas.create_rectangle(x1, y1, x2, y2, "white")

            #We move the player one square to the right
            x3 = player_col * CELL_SIZE + CELL_SIZE 
            y3 = player_row * CELL_SIZE 
            x4 = x3 + CELL_SIZE
            y4 = y3 + CELL_SIZE
            canvas.create_oval(x3,y3,x4,y4,"blue")

            player_col = next_col


def choose_player_position():
    #To choose the player's position always from a corner
    corners = [(1, 1), (1, 23), (23, 1), (23, 23)]
    row, col = random.choice(corners)
    x = col * CELL_SIZE
    y = row * CELL_SIZE
    x2 = x + CELL_SIZE
    y2 = y + CELL_SIZE
    canvas.create_oval(x,y,x2,y2,"blue")
    return row, col


def generate_orange_ball(canvas):
    #To generate the orange ball, she's the goal
    #First we get the coordinates
    x1 = CANVAS_WIDTH /2 - CELL_SIZE/2
    y1 = CANVAS_HEIGHT /2 - CELL_SIZE/2
    x2 = x1 + CELL_SIZE
    y2 = y1 + CELL_SIZE
    canvas.create_oval(x1,y1,x2,y2,"orange")


def generate_maze(rows, cols):
    """I ASK CLAUDE FOR HELP because i didn't know how make the maze random xd"""
    # Start with everything as walls
    maze = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(1)
        maze.append(row)

    # Pick starting cell (must be odd row/col so paths stay separated)
    start_row = 1
    start_col = 1
    maze[start_row][start_col] = 0

    # Stack keeps track of where we've been
    stack = []
    stack.append((start_row, start_col))

    while len(stack) > 0:
        current_row, current_col = stack[-1]  # peek at top of stack

        # Find neighbors 2 steps away that are still walls
        neighbors = []
        directions = [(-2, 0), (2, 0), (0, -2), (0, 2)]
        for dr, dc in directions:
            neighbor_row = current_row + dr
            neighbor_col = current_col + dc
            if 0 < neighbor_row < rows - 1 and 0 < neighbor_col < cols - 1:
                if maze[neighbor_row][neighbor_col] == 1:
                    neighbors.append((neighbor_row, neighbor_col))

        if len(neighbors) > 0:
            # Pick a random unvisited neighbor
            next_row, next_col = random.choice(neighbors)
            # Carve through the wall between current and neighbor
            maze[(current_row + next_row) // 2][(current_col + next_col) // 2] = 0
            maze[next_row][next_col] = 0
            stack.append((next_row, next_col))
        else:
            # Dead end — backtrack
            stack.pop()

    return maze


def draw_maze(canvas,maze):
    """TO DRAW THE SQUARES"""
    for i in range (len(maze)):
        #We get the index of lists inside of maze
        lists_of_maze = maze [i]
        for z in range (len(lists_of_maze)):
            #We get the index of the elements inside the list of lists_of_maze 
            number_inside_list_of_list = lists_of_maze[z]

            #Configuration of the coordinates
            x1 = CELL_SIZE * z
            y1 = i * CELL_SIZE 
            x2 = x1 + CELL_SIZE
            y2 = y1 + CELL_SIZE
            
            #To get color 
            if number_inside_list_of_list == 1:
                color = "green"
            elif number_inside_list_of_list == 0:
                color = "white"

            #We draw the rectangle
            canvas.create_rectangle(x1,y1,x2,y2,color)

            #TO MAKE IT LOOK COOLER WHEN IT GENERATES FNBUWYIGEWA
            time.sleep(0.009)


def main():
    global canvas, maze, player_row, player_col
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    maze = generate_maze(ROWS, COLS)
    # force center be white
    maze[12][12] = 0  
    #To force the corners be white   
    maze[1][1] = 0     
    maze[1][23] = 0    
    maze[23][1] = 0    
    maze[23][23] = 0   
    
    draw_maze(canvas, maze)
    #To generate the orange ball, she's the goal
    generate_orange_ball(canvas)
    player_row, player_col = choose_player_position()

    #TO STOP THE BALL TO MOVE BEFORE THE MOUSE CLICKS
    canvas.wait_for_click()
    
    while True:
        mouse_x = canvas.get_mouse_x()
        mouse_y = canvas.get_mouse_y()
        
        clicked_col = mouse_x // CELL_SIZE
        clicked_row = mouse_y // CELL_SIZE

        # This is to move the player calling the move_player() function 
        if clicked_row < player_row:
            move_player("up")

        elif clicked_row > player_row:
            move_player("down")

        elif clicked_col < player_col:
            move_player("left")

        elif clicked_col > player_col:
            move_player("right")

        if player_row == 12 and player_col == 12:
            canvas.create_text(CANVAS_WIDTH/2 - CELL_SIZE*3,CANVAS_HEIGHT/2-CELL_SIZE,"YOU DID IT!!!!", 
            color="orange", 
            font="Courier", 
            font_size=28)
            break

        #To stop the player of teleporting
        time.sleep(0.07)
        
    





if __name__ == '__main__':
    main()