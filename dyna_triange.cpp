class Solution {
  public:
    int minimumTotal(vector< vector<int> > &triangle){
      if (triangle.empty()) {
        return -1;
      }

      vector<vector<int>> hashmap(triangle);

      //get the total row number of triangle
      const int N = triangle.size();
      //hashmap[0][0] = triangle[0][0];
      for (int i = 1;i !=N; ++i) {
        for (int j = 0; j <= i; ++j) {
          if (j ==0 ){
            hashmap[i][j] = hashmap[i - 1][j];
          }
          if (j > 0) && (j < i) {
            hashmap[i][j] = min(hashmap[i - 1][j],hashmap[i - 1][j - 1]);
          }
          hashmap[i][j] += triangle[i][j];
        }
      }

      int result = INT_MAX;
      for (int i; i != N; ++i) {
        result = min(result, hashmap[N - 1][i]);
      }
      return result;
    }
};
