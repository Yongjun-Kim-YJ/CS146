package CS146.HW1;

public class Q2 {
    public static int findIndexOfZero(int[] A, int[] B) {
        int left = 0;
        int right = B.length-1;

        while (left <= right) {
            // Set mid as average of left and right
            int mid = left+(right-left+1)/2;

            if (B[mid] == 0) {
                return mid + 1; // Return index of zero counting from 1
            } else if (mid > 0 && B[mid-1] < A[mid-1]) {
                // 0 is to the left of mid
                right = mid-1;
            } else {
                // 0 is to the right of mid
                left = mid+1;
            }
        }

        // 0 is not found
        return -1;
    }

    public static void main(String[] args) {
        int[] A = {1, 3, 4, 5, 7, 9, 11, 20};
        int[] B = {1, 3, 4, 5, 0, 7, 9, 11, 20};
        
        int zeroIndex = findIndexOfZero(A, B);
        System.out.println("Index of zero in B: " + zeroIndex);
    }
}