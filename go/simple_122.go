func maxProfit(prices []int) int {
	N := len(prices)
	profit, profitWithStock := 0, -prices[0]

	for i := 0; i < N; i++ {
		tmp := profitWithStock + prices[i]
		newProfit := profit
		if tmp > profit {
			newProfit = tmp
		}
		tmp = profit - prices[i]
		if tmp > profitWithStock {
			profitWithStock = tmp
		}
		profit = newProfit
	}
	return profit
}
