from operations import create_task, list_tasks, update_description, mark_done, mark_in_progress, list_status, delete_task
from json import dump, load

## Open the Agenda json file at the dierctory
with open("db.json", "r", encoding="utf-8") as open_file:
    Agenda = load(open_file)

### LOOP
out = 0
while out != 1:
    command = input("task cli ")
    if command.split()[0].lower() == "add":
        create_task(Agenda, command[3:])
    if command.split()[0].lower() == 'delete': 
        delete_task(Agenda, int(command[6:]))
    if command.split()[0].lower() == "mark-done":
        mark_done(Agenda, int(command[9:]))
    if command.split()[0].lower() == "mark-in-progress":
        mark_in_progress(Agenda, int(command[16:]))
    if command.split()[0].lower() == "update":         
        update_description(Agenda, int(command[7]), command[7:])
    if command.split()[0].lower() == 'list' and command.split()[1].lower() == 'done':
        list_status(Agenda, "done")
    if command.split()[0].lower() == 'list' and command.split()[1].lower() == 'todo': 
        list_status(Agenda, "todo")
    if command.split()[0].lower() == 'list' and command.split()[1].lower() == 'in-progress':
        list_status(Agenda, "in-progress")
    if command.split()[0].lower() == 'list' and command.split()[1].lower() == '.':
        list_tasks(Agenda)
    if command == "out":
        print("END")
        out = 1

## Saves the agenda in a json file at the directory
with open("db.json", "w", encoding="utf-8") as saving_file:
    dump(Agenda, saving_file, ensure_ascii=False, indent=4)