package HW7;

import java.util.Arrays;

public class MinMeetingRooms {
    public int minMeetingRooms(int[][] intervals) {
        if (intervals.length == 0) {
            return 0;
        }

        int[] startTimes = new int[intervals.length];
        int[] endTimes = new int[intervals.length];

        for (int i = 0; i < intervals.length; i++) {
            startTimes[i] = intervals[i][0];
            endTimes[i] = intervals[i][1];
        }

        Arrays.sort(startTimes);
        Arrays.sort(endTimes);

        int startPointer = 0;
        int endPointer = 0;
        int roomsNeeded = 0;

        while (startPointer < intervals.length) {
            if (startTimes[startPointer] >= endTimes[endPointer]) {
                roomsNeeded -= 1;
                endPointer += 1;
            }
            roomsNeeded += 1;
            startPointer += 1;
        }

        return roomsNeeded;
    }

    public static void main(String[] args) {
        MinMeetingRooms mmr = new MinMeetingRooms();

        int[][] intervals1 = {{0, 30}, {5, 10}, {15, 20}};
        System.out.println(mmr.minMeetingRooms(intervals1));

        // int[][] intervals2 = {{0, 1}, {1, 2}, {2, 3}};
        // System.out.println(mmr.minMeetingRooms(intervals2));
    }
}
