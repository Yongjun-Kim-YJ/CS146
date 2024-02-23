package CS146.HW1;

public class Q2 {
    public static int findZeroIndex(int[] A, int[] B) {
        int left = 0;
        int right = B.length - 1;

        while (left <= right) {
            int mid = left + (right - left) / 2;

            if (B[mid] == 0) {
                return mid + 1; // 인덱스 1부터 시작한다고 가정
            } else if (mid > 0 && B[mid] < A[mid - 1]) {
                // 0이 mid의 왼쪽에 있어야 함
                right = mid - 1;
            } else {
                // 0이 mid의 오른쪽에 있어야 함
                left = mid + 1;
            }
        }

        // 0을 찾지 못한 경우, 이는 입력이 잘못되었음을 의미
        return -1;
    }

    public static void main(String[] args) {
        int[] A = {1, 3, 4, 6, 7, 8, 9, 20};
        int[] B = {1, 3, 0, 4, 6, 7, 8, 9, 20};
        
        int zeroIndex = findZeroIndex(A, B);
        System.out.println("The index of zero in B is: " + zeroIndex);
    }
}