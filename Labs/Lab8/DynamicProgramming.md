1. Initialization: Create a DP array dp of size amount+1 initialized to amount+1 to represent unreachable amounts. Set dp[0]=0 since zero coins are needed to make zero amount.

2. Filling the DP Table, iterate through each coin in the coins array:
For each coin, update the DP table for all amounts starting from the coin's value up to the total amount.
Update dp[i] as the minimum of its current value and dp[i-coin]+1. This ensures the minimum number of coins needed to make the amount i using the current coin.

3. Result: If dp[amount] remains the initialized high value, it means that the amount cannot be made up using the given coins, so return -1. Otherwise, return the value in dp[amount].