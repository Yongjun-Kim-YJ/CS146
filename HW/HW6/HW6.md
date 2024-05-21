1. Sort the Array
2. Iterate Through the Array: For each element, use it as a potential first element of the triplet.
3. Skip Duplicates: If the current element is the same as the previous element, skip it to avoid duplicate triplets.
4. Two-Pointer Technique:
   - One starting just after the current element (`left`), and the other starting at the end of the array (`right`).
   - Calculate the sum of the three elements (`nums[i]`, `nums[left]`, and `nums[right]`).
   - If the sum == 0, add the triplet to the result list.
   - If the sum < 0, move the `left` pointer to the right to increase the sum.
   - If the sum > 0, move the `right` pointer to the left to decrease the sum.
   - Skip duplicate elements for both `left` and `right` pointers to ensure the uniqueness of triplets.
5. Return the Result