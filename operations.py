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
        - id:           The identification tag. consists of an int number for task position.
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
    """
    Lists the tasks in agenda as a table format.
    ---------------------------------------------------
    Parameters:
        - agenda:       The agenda dictionary. contains the information of all taks linked until present.
    ---------------------------------------------------
    Return: Void. List the data information of all tasks in agenda until present.
    """
    print(ID.ljust(3), DESCRIPTION.ljust(50), STATUS.ljust(25))
    print("------------------------------------------------------------------")
    for key in agenda:
        print(f"{agenda[key]['id']:<3} {agenda[key]['description']:<50} {agenda[key]['status']:<25}")
        
def update_description(agenda, tag, new_description):
    """
    Updates the description of an especific task, witch its position is informed as an parameter 'tag'.
    ------------------------------------------------------------------------------------
    Parameters:
        - agenda:       The agenda dictionary. contains the information of all taks linked until present.
        - tag:          The identification tag. consists of an int number for task position.
        - description:  The task description. consists of a string that detail the task.
    ------------------------------------------------------------------------------------
    Return: Void. Updates the task description positional informed by 'tag' parameter.

    """
    agenda[tag]["description"] = new_description
    agenda[tag]["UpdatedAt"] = datetime.now()

def mark_done(agenda, tag):
    """
    Updates the status of an task epecified by 'tag" input marking as 'done'.
    ------------------------------------------------------------------------------------
    Parameters:
        - agenda:       The agenda dictionary. contains the information of all taks linked until present.
        - tag:          The identification tag. consists of an int number for task position.
    ------------------------------------------------------------------------------------
    Return: Void. Updates the task status.
    """
    agenda[tag]["status"] = "done"

def mark_in_progress(agenda, tag):
    """
    Updates the status of an task epecified by 'tag" input marking as 'din progress'.
    ------------------------------------------------------------------------------------
    Parameters:
        - agenda:       The agenda dictionary. contains the information of all taks linked until present.
        - tag:          The identification tag. consists of an int number for task position.
    ------------------------------------------------------------------------------------
    Return: Void. Updates the task status.
    """
    agenda[tag]["status"] = "in progress"

def list_status(agenda, status):
    """
    Print each task information in the agenda by each status.
    ------------------------------------------------------------------------------------
    Parameters:
        - agenda:       The agenda dictionary. contains the information of all taks linked until present.
        - status:       The task status informed.
    ------------------------------------------------------------------------------------
    Retrun: Void.
    """
    print(ID.ljust(3), DESCRIPTION.ljust(50), STATUS.ljust(25))
    print("------------------------------------------------------------------")
    if status.lower() == "done":
        for key in agenda:
            if agenda[key]["status"] == "done":
                print(f"{agenda[key]['id']:<3} {agenda[key]['description']:<50} {agenda[key]['status']:<25}")
    if status.lower() == "todo":
        for key in agenda:
            if agenda[key]['status'] == "todo":
                print(f"{agenda[key]['id']:<3} {agenda[key]['description']:<50} {agenda[key]['status']:<25}")
    if status.lower() == "in-progress":
        for key in agenda:
            if agenda[key]["status"] == "in progress":
                print(f"{agenda[key]['id']:<3} {agenda[key]['description']:<50} {agenda[key]['status']:<25}")


