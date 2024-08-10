
# Define the tasks and their durations
tasks = {
    'T_START': 0,
    'A': 4,
    'B': 3,
    'C': 2,
    'D': 5,
    'E': 6,
    'T_END': 0
}

# Define the dependencies between tasks
dependencies = {
    'T_START': ['A','B'],
    # 'T_START': ['B'],
    'A': ['C'],
    'B': ['D'],
    'C': ['E'],
    'D': ['E'],
    'E': ['T_END'],
    'T_END': []
}

    #for each task in tasks
    #    for each dependency of task
    #        est =  max of (predecessor task duration, pred dependcies duration+tasks duration)
    #return the final est i.e est of all tasks

def calculate_earliest_times(tasks, dependencies):
    earliest_times = {task: 0 for task in tasks}
    for task in tasks:
        print(f'----------------- {task} --------------')
        for dep in dependencies[task]:
            print (f'{task} --> {dep} : est_dep : {earliest_times[dep]} est_task: {earliest_times[task]} tasks_task :{tasks[task]}')
            earliest_times[dep] = max(earliest_times[dep], earliest_times[task] + tasks[task])

    return earliest_times

#reverse all dependencies to work backward from the last task to the first by ensuring that all tasks are completed by the latest possible time.
#for each reversed task
#    calculates the latest start time (LST) and the latest finish time (LFT) for each task.

def calculate_latest_times(tasks, dependencies, max_time):
    latest_times = {task: max_time for task in tasks}

    reversed_dependencies = {task: [] for task in tasks}
    for task in dependencies:
        for dep in dependencies[task]:
            reversed_dependencies[dep].append(task)

    for task in reversed(tasks):
        for dep in reversed_dependencies[task]:
            latest_times[dep] = min(latest_times[dep], latest_times[task] - tasks[dep])
    return latest_times

def main():
    # Calculate earliest finish times (EFT)
    earliest_times = calculate_earliest_times(tasks, dependencies)
    print(f'calculate_earliest_times: {earliest_times}')
    max_time = max(earliest_times[task] + tasks[task] for task in tasks)

    # Calculate latest finish times (LFT)
    latest_times = calculate_latest_times(tasks, dependencies, max_time)
    print(f'calculate_latest_times: {latest_times}')

    latest_completion_time = max(latest_times[task] + tasks[task] for task in tasks)

    print(f"\nEarliest time all tasks will be completed: {max_time}")
    print(f"\nLatest time all tasks will be completed: {latest_completion_time}")

if __name__ == "__main__":
    main()

