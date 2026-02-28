#E-Commerce Order Revenue Analyzer

class Solution:

    def city_revenue(self, orders):
        revenue_dict = {}
        
        for order in orders:
            city = order["city"]
            amount = order["amount"]
            
            if city in revenue_dict:
                revenue_dict[city] += amount
            else:
                revenue_dict[city] = amount
        
        max_city = None
        max_revenue = 0
        
        for city in revenue_dict:
            if revenue_dict[city] > max_revenue:
                max_revenue = revenue_dict[city]
                max_city = city
        
        return revenue_dict, max_city