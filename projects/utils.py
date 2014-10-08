
def total_work_time_project(tasks):
    time = 0
    for task in tasks:
        time += task.time
    return time
