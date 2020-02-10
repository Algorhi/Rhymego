class Solution{
  public:

    int uniquePaths(int m, int n) {
      if (m < n || n < 1){
        return 0;
      }

      vector<vector<int>> ret(m, vector<int>(n, 1));

      for (int i = 1; i != m; ++i) {
        for (int j = 1; j != n; ++j) {
        ret[i][j] = ret[i - 1][j] + ret[i][j - 1];
        }
      }

      return ret[m - 1][n - 1];
    }
};
