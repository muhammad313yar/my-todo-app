from function import read_todo, write_todo 
import time

time = time.strftime('%d-%m-%Y: %H:%M')
print(time)
while True:
    user_action = input("Enter add, show, edit, complate or exit:").lower()
    user_action = user_action.strip()

    todos = read_todo()

    if user_action.startswith("add"):
            todo = user_action[4:] +"\n"
            todo = todo.capitalize()
            todos.append(todo)
            write_todo(todos)

    elif user_action.startswith("show"):
            for index, item in enumerate(todos):
                print(f"{index + 1}.{item.strip()}")

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1
            new_edit = input("Enter new todo:") + "\n"
            new_edit = new_edit.capitalize()
            todos[number] = new_edit
            write_todo(todos)
        except ValueError:
            print("your comman is valid.")
        except IndexError:
            print("your number out of range.")
    elif user_action.startswith("complate"):
        try:
            number = int(user_action[9:])
            number = number - 1
            remove_list = todos.pop(number)
            print(f"{remove_list} removed.")
            write_todo(todos)
        except ValueError:
            print("your comman is valid.")
        except IndexError:
            print("your number out of range.")

    elif user_action.startswith("exit"):
            break
    else:
        print("Your comman is valid.")

print("Goodbye!")
    