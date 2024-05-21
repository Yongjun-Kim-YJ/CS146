package HW1;

public class PalindromeChecker {
    public boolean isPalindrome(String s) {
        s = s.replaceAll("[^a-zA-Z0-9]", "").toLowerCase();
        
        int left = 0, right = s.length() - 1;
        
        while (left < right) {
            if (s.charAt(left) != s.charAt(right)) {
                return false;
            }
            left++;
            right--;
        }
        
        return true;
    }

    public static void main(String[] args) {
        PalindromeChecker checker = new PalindromeChecker();

        System.out.println(checker.isPalindrome("ab:b,a"));
        System.out.println(checker.isPalindrome("race a car"));
    }
}