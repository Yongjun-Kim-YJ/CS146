package HW8;

import java.util.HashMap;
import java.util.Map;

public class LongestPalindrome {
    public int longestPalindrome(String s) {
        Map<Character, Integer> count = new HashMap<>();
        
        for (char c : s.toCharArray()) {
            count.put(c, count.getOrDefault(c, 0) + 1);
        }
        
        int length = 0;
        boolean oddFound = false;

        for (int freq : count.values()) {
            if (freq % 2 == 0) {
                length += freq;
            } else {
                length += freq - 1;
                oddFound = true;
            }
        }
        
        if (oddFound) {
            length += 1;
        }
        
        return length;
    }
    
    public static void main(String[] args) {
        LongestPalindrome lp = new LongestPalindrome();
        
        System.out.println(lp.longestPalindrome("abccccdd"));
        System.out.println(lp.longestPalindrome("speediskey"));
        // System.out.println(lp.longestPalindrome("a"));
        // System.out.println(lp.longestPalindrome("aa"));
        // System.out.println(lp.longestPalindrome("abc"));
        // System.out.println(lp.longestPalindrome("abbbb"));
        // System.out.println(lp.longestPalindrome("aabbcc"));
        // System.out.println(lp.longestPalindrome("AaBbCc"));
    }
}
