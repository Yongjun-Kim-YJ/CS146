package HW1;

public class Q1 {
    private static Result findMedianAndMode(char[] arr) {
        if(arr.length<1){ // If array has no element, return (null, null)
            return new Result('\0','\0');
        }

        int[] freq = new int[26]; // Frequency array for 26 latin characters

        // Count each character
        for (char c : arr) {
            int index = c - 'a';
            if(index<0){ // Convert uppercase to lowercase
                index+=32;
            }
            freq[index]++;
        }

        char median = '\0', mode = '\0';
        int maxFreq = 0, count = 0, n = arr.length;

        // Find median and mode
        for (int i = 0; i < 26; i++) {
            // Median
            count += freq[i];
            if (median == '\0' && count >= (n+1)/2) {
                median = (char) (i + 'a');
            }

            // Mode
            if (freq[i] > maxFreq) {
                maxFreq = freq[i];
                mode = (char) (i + 'a');
            }
        }

        return new Result(median, mode);
    }

    public static class Result {
        char median;
        char mode;

        public Result(char median, char mode) {
            this.median = median;
            this.mode = mode;
        }
    }

    public static void main(String[] args) {
        char[] arr = {'a','b','c','C'};
        Result result = findMedianAndMode(arr);
        System.out.println("Median: " + result.median);
        System.out.println("Mode: " + result.mode);
    }
}
