# python-assignment
maze and list program 

# python-assignment
#maze and list program 
#find the average of a list of integers using recurrsion approach



def print_solution(solution):
    for row in solution:
        print(row)

def is_safe(maze, x, y, visited):
    n = len(maze)

    return (0 <= x < n and 0 <= y < n and 
            maze[x][y] == 1 and not visited[x][y])

def solve_maze_util(maze, x, y, solution, visited):
    n = len(maze)

    
    if x == n - 1 and y == n - 1 and maze[x][y] == 1:
        solution[x][y] = 1
        return True

    if is_safe(maze, x, y, visited):

        solution[x][y] = 1
        visited[x][y] = True

   
        if solve_maze_util(maze, x + 1, y, solution, visited):
            return True


        if solve_maze_util(maze, x, y + 1, solution, visited):
            return True


        if solve_maze_util(maze, x - 1, y, solution, visited):
            return True

     
        if solve_maze_util(maze, x, y - 1, solution, visited):
            return True


        solution[x][y] = 0
        return False

    return False


def solve_maze(maze):
    n = len(maze)
    solution = [[0] * n for _ in range(n)]
    visited = [[False] * n for _ in range(n)]

    if not solve_maze_util(maze, 0, 0, solution, visited):
        print("No path found.")
    else:
        print("Path found:")
        print_solution(solution)


maze = [
[1,1,1,1,0,1,1,1,1,0,1,1,1,1,1,1],
[0,1,0,1,1,1,0,0,1,1,1,0,1,0,1,1],
[1,1,0,0,1,1,1,1,0,1,0,1,1,1,0,1],
[1,0,1,1,0,1,1,0,1,1,1,0,1,1,1,1],
[1,1,1,0,1,1,0,1,1,0,1,1,0,1,1,1],
[0,1,1,1,1,0,1,1,0,1,1,1,1,0,1,0],
[1,1,0,1,1,1,0,1,1,1,0,1,1,1,1,1],
[1,0,1,1,1,1,1,0,1,1,1,1,0,1,0,1],
[1,1,1,0,1,1,1,1,0,1,1,0,1,1,1,1],
[1,0,1,1,1,1,0,1,1,1,1,1,0,1,0,1],
[1,1,1,1,0,1,1,1,1,0,1,1,1,1,1,1],
[0,1,0,1,1,1,0,0,1,1,1,0,1,0,1,1],
[1,1,0,0,1,1,1,1,0,1,0,1,1,1,0,1],
[1,0,1,1,0,1,1,0,1,1,1,0,1,1,1,1],
[1,1,1,1,1,0,1,1,0,1,1,1,1,1,0,1],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]
solve_maze(maze)








#solve a maize using a recurssion approach


 



def sum_list(lst, n):
    if n == 0:
        return 0
    return lst[n-1] + sum_list(lst, n-1)

def avg_list(lst):
    if len(lst) == 0:
        return 0
    total = sum_list(lst, len(lst))
    return total / len(lst)

print(avg_list([1, 2, 3, 4]))
