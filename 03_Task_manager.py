
"""
Problem:
A software engineer must complete as many tasks as possible before their deadlines.
Each task has:
- A deadline (day by which it must be completed)
- A duration (in days)

Objective:
Maximize the number of tasks completed without missing their deadlines.

Approach:
- Sort tasks by their deadlines.
- Use a greedy approach: schedule the shortest tasks first if they fit within the current time.
- Use a min-heap to manage durations, replacing longer tasks if a shorter one can optimize the schedule.

This is a classic greedy problem inspired by the "Scheduling to Minimize Lateness".
"""
# import to use heap queue algo. also known as priority queue.
import heapq

def max_tasks(tasks):
    # Sort by deadline
    tasks.sort(key=lambda x: x['deadline'])
    total_time = 0
    max_heap = []

    for task in tasks:
        total_time += task['duration']
        # Push negative to simulate max-heap
        heapq.heappush(max_heap, -task['duration'])  
        if total_time > task['deadline']:
            # Remove longest duration
            total_time += heapq.heappop(max_heap)  
    return len(max_heap)

if __name__ == "__main__":
    tasks = [
        {'name': 'Task 1', 'deadline': 4, 'duration': 2},
        {'name': 'Task 2', 'deadline': 3, 'duration': 1},
        {'name': 'Task 3', 'deadline': 2, 'duration': 1},
        {'name': 'Task 4', 'deadline': 1, 'duration': 2},
    ]
    
    result = max_tasks(tasks)
    print("Maximum tasks that can be completed:", result)
