class Solution {
public:
    vector<int> luckyNumbers(vector<vector<int>>& matrix) {

        int m = matrix.size();        // Number of rows
        int n = matrix[0].size();     // Number of columns

        // Stores the maximum among all row minimums
        int rowminmax = INT_MIN;

        // Find minimum element of each row
        // Then find the maximum among those minimums
        for (int row = 0; row < m; row++) {

            int rowmin = INT_MAX;

            for (int col = 0; col < n; col++) {
                rowmin = min(rowmin, matrix[row][col]);
            }

            rowminmax = max(rowminmax, rowmin);
        }

        // Stores the minimum among all column maximums
        int colmaxmin = INT_MAX;

        // Find maximum element of each column
        // Then find the minimum among those maximums
        for (int col = 0; col < n; col++) {

            int colmax = INT_MIN;

            for (int row = 0; row < m; row++) {
                colmax = max(colmax, matrix[row][col]);
            }

            colmaxmin = min(colmaxmin, colmax);
        }

        // If both values are equal,
        // that value is the lucky number
        if (rowminmax == colmaxmin) {
            return {rowminmax};
        }

        // No lucky number found
        return {};
    }
};