package CS146.HW1;

import java.util.ArrayList;
import java.util.List;

public class Q3 {

    public static List<List<Integer>> findMissingRanges(int[] IDs, int lower, int upper) {
        List<List<Integer>> missingRanges = new ArrayList<>();

        // Index of next missing ID
        int next = lower;

        for (int i = 0; i < IDs.length; i++) {
            if (IDs[i] > upper) break;
            if (IDs[i] < next) continue;
            if (IDs[i] > next) {
                missingRanges.add(getRange(next, IDs[i]-1));
            }

            // Update next = current ID + 1
            next = IDs[i] + 1;
        }

        // Out of range IDs to upper
        if (next <= upper) {
            missingRanges.add(getRange(next, upper));
        }

        return missingRanges;
    }

    // Create range list
    private static List<Integer> getRange(int start, int end) {
        List<Integer> range = new ArrayList<>();
        range.add(start);
        if (end >= start) {
            range.add(end);
        }
        return range;
    }

    public static void main(String[] args) {
        int[] IDs = {0, 1, 3, 50, 75};
        int lower = -1;
        int upper = -1;
        List<List<Integer>> missingRanges = findMissingRanges(IDs, lower, upper);

        System.out.println(missingRanges);
    }
}
