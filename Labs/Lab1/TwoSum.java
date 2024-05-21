package Labs.Lab1;

public class TwoSum {
    public int[] twoSum(int[] nums, int target) {
        for (int i = 0; i < nums.length; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                if (nums[i] + nums[j] == target) {
                    return new int[] { i, j };
                }
            }
        }
        return new int[] {-1,-1};
    }

    public static void main(String[] args) {
        TwoSum ts = new TwoSum();

        // int[] nums1 = {2, 7, 11, 15};
        // int target1 = 8;
        // int[] result1 = ts.twoSum(nums1, target1);
        // System.out.println(result1[0] + ", " + result1[1]);

        // int[] nums2 = {3, 2, 4};
        // int target2 = 6;
        // int[] result2 = ts.twoSum(nums2, target2);
        // System.out.println(result2[0] + ", " + result2[1]);

        // int[] nums3 = {3, 3};
        // int target3 = 6;
        // int[] result3 = ts.twoSum(nums3, target3);
        // System.out.println(result3[0] + ", " + result3[1]);
    }
}
