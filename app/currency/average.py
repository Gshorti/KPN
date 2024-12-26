def average_calculator(sale_orders, buy_orders):
    sale_orders = sale_orders.split(",")
    buy_orders = buy_orders.split(",")
    buy_orders_list, sale_orders_list = [], []

    for buy in buy_orders:
        buy_orders_list.append(float(buy))

    for sale in sale_orders:
        sale_orders_list.append(float(sale))

    summary = 0

    for float_buy in buy_orders_list:
        summary += float_buy

    buy_average = summary/len(buy_orders_list)

    summary = 0

    for float_sale in sale_orders_list:
        summary += float_sale

    sale_average = summary/len(sale_orders_list)

    average = (sale_average + buy_average)/2

    return sale_average,buy_average,average
