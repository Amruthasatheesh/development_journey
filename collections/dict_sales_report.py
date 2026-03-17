sales_report={
    "sun":23000,
    "mon":16000,
    "tue":18000,
    "wed":15000,
    "thu":19000,
    "fri":19000,
    "sat":20000
}
#display day_wise values
# total_sale
# display avg_value
# display day where sales<avg_sales

for key in sales_report:
    print(key,sales_report[key])
total_sale=0
for key in sales_report:
    sale_day=sales_report[key]
    total_sale+=sale_day
print(total_sale)
avg_sale=total_sale/len(sales_report)
print(avg_sale)
for key in sales_report:
    values=sales_report[key]
    if values<avg_sale:
        print(key)