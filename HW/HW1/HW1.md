1. Preprocessing:
   - Convert the string to lowercase.
   - Remove all non-alphanumeric characters using regular expressions.
2. Two-Pointer Initialization: `left`, `right`
3. Pointer Comparison:
   - Compare the characters at the `left` and `right` pointers.
   - If they are equal, move the `left` pointer one step to the right and the `right` pointer one step to the left.
   - If they are not equal, return `false`.
4. Completion:
   - If all characters match while the `left` pointer is less than the `right` pointer, return `true`.
