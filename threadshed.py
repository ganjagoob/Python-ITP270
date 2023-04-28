#!/bin/python3

daily_sales = "customer1;,$21.34,white&blue;\n\
customer2;,$12.17;red;\n\
customer3;, $11.23;purple&yellow;\n\
customer4;, $10.92;green;\n"

daily_sales_replaced = daily_sales.replace(';,;', '%%')
daily_transactions = daily_sales_replaced.split(',')

daily_transactions_split = []
for transaction in daily_transactions:
    for delimiter in [';,$', ', $', ',']:
        if delimiter in transaction:
            daily_transactions_split.append(transaction.split(delimiter))
            break
    else:
        print(f'Invalid transaction: {transaction.split(";")[0]}')


transactions_clean = []
for transaction in daily_transactions_split:
    clean_transaction = [data_point.strip() for data_point in transaction]
    transactions_clean.append(clean_transaction)

customers = []
sales = []
thread_sold = []
print(f'transaction: {transaction}')
for transaction in transactions_clean:
    if len(transaction) == 3:
        customers.append(transaction[0])
        sales.append(transaction[1].replace(" ", ""))
        thread_sold.append(transaction[2])
    else:
        print(f'Invalid transaction: {transaction}')

total_sales = sum([float(sale.strip('$')) for sale in sales])

thread_sold_split = []
for sale in thread_sold:
    if '&' not in sale:
        thread_sold_split.append(sale)
    else:
        colors = sale.split('&')
        thread_sold_split += [color.strip() for color in colors]

def color_count(color):
    count = 0
    for thread_color in thread_sold_split:
        if thread_color == color:
            count += 1
    return count

colors = ['red', 'yellow', 'green', 'white', 'black', 'blue', 'purple']
for color in colors:
    count = color_count(color)
    print("Thread Shed sold {} threads of {} today.".format(count, color))


