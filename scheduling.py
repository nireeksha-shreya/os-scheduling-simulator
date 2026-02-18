def fcfs(processes):
    processes.sort(key=lambda x: x[1])  # sort by arrival
    time = 0
    result = []

    for pid, arrival, burst in processes:
        if time < arrival:
            time = arrival
        waiting = time - arrival
        time += burst
        turnaround = waiting + burst
        result.append((pid, waiting, turnaround))

    return result


def sjf(processes):
    processes.sort(key=lambda x: x[2])  # sort by burst
    time = 0
    result = []

    for pid, arrival, burst in processes:
        waiting = time
        time += burst
        turnaround = waiting + burst
        result.append((pid, waiting, turnaround))

    return result


def round_robin(processes, quantum):
    queue = processes[:]
    time = 0
    remaining = {pid: burst for pid, _, burst in processes}
    result = []

    while queue:
        pid, arrival, burst = queue.pop(0)

        if remaining[pid] > quantum:
            time += quantum
            remaining[pid] -= quantum
            queue.append((pid, arrival, burst))
        else:
            time += remaining[pid]
            waiting = time - burst
            turnaround = time
            result.append((pid, waiting, turnaround))
            remaining[pid] = 0

    return result
