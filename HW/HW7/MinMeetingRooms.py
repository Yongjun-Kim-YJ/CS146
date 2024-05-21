def minMeetingRooms(self, intervals: List[List[int]]) -> int:
    if not intervals:
        return 0
    
    start_times = sorted([i[0] for i in intervals])
    end_times = sorted([i[1] for i in intervals])

    start_pointer = 0
    end_pointer = 0
    rooms_needed = 0

    while start_pointer < len(intervals):
        if start_times[start_pointer] >= end_times[end_pointer]:
            rooms_needed -= 1
            end_pointer += 1
        rooms_needed += 1
        start_pointer += 1

    return rooms_needed
