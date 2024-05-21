package Labs.Lab2;

import java.util.Arrays;

public class AnagramChecker {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }
        char[] sArray = s.toCharArray();
        char[] tArray = t.toCharArray();
        Arrays.sort(sArray);
        Arrays.sort(tArray);
        return Arrays.equals(sArray, tArray);
    }

    public static void main(String[] args) {
        AnagramChecker checker = new AnagramChecker();

        System.out.println(checker.isAnagram("anagram", "nagaram"));
        System.out.println(checker.isAnagram("rat", "car"));
    }
}

