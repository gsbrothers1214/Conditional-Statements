actual_cost = float(input("Please Enter the Actual Product Price: "))
sales_amount = float(input("Please Enter the Sales Product Price: "))

if (sales_amount > actual_cost):
  amount = sale_amount - actual_cost
  print("Total Profit = {0}".format(amount))
else:
  print("No Profit!!!!!")
