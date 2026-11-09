FILE_PATH = "todos.txt"

def read_todo(FILE_PATH="todos.txt"):
    with open(FILE_PATH, 'r') as file_local:
        todos_local = file_local.readlines()
        return todos_local


def write_todo(todos, FILE_PATH="todos.txt"):
    with open(FILE_PATH, "w") as file:
        file.writelines(todos)   


if __name__ == "__main__":
    print("Ya Allah.")