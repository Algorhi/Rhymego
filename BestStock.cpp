class Solution {
public:
int maxProfit(vector<int> &prices) {
  if (prices.size() <= 1) return 0;

  int profit = 0;
  int cur_price_min = INT_MAX;
  for (int i = 0; i < prices.size(); ++i) {
    profit = max(profit, prices[i] - cur_price_min);
    cur_price_min = min(cur_price_min, prices[i]);
  }
return profit;
}
};

