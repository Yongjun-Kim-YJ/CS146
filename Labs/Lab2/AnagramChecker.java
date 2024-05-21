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

        // 테스트 케이스들
        System.out.println(checker.isAnagram("anagram", "nagaram"));  // 출력: true
        System.out.println(checker.isAnagram("rat", "car"));  // 출력: false
    }
}

