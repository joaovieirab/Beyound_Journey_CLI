from datetime import datetime

ID = "ID"
DESCRIPTION = "DESCRIPTION"
STATUS = "STATUS"

def create_task (agenda, description, id=1):
    """
    Creates a new task and write in the agenda data base.
    -------------------------------------------------------------------------------------------------------
    Parameters:
        - agenda:       The agenda dictionary. contains the information of all taks linked until present.
        - description:  The task description. consists of a string that detail the task.
        - id:           The identification tag. consists of an int number for position of task.
    -------------------------------------------------------------------------------------------------------
    Retrun: Void. Update the agenda by insertining the new task in the agenda.

"""
    agenda_len = len(agenda)
    if agenda_len == 0:
        new_task = {
            'id': id,
            'description': description,
            'status':'todo',
            'CreatedAt':datetime.now(),
            'UpdatedAt':datetime.now()
        }
    else:
        new_task = {
            'id': agenda_len + 1,
            'description': description,
            'status':'todo',
            'CreatedAt':datetime.now(),
            'UpdatedAt':datetime.now()
        }
    agenda[new_task["id"]] = new_task

def list_tasks(agenda):
    print(ID.ljust(3), DESCRIPTION.ljust(20), STATUS.ljust(15))
    print("---------------------------------------------")
    for key in agenda:
        print(f"{agenda[key]['id']:<3} {agenda[key]['description']:<20} {agenda[key]['status']:<15}")
        