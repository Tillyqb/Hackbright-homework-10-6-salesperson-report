"""Generate sales report showing total melons each salesperson sold."""


salespeople = []
melons_sold = []

f = open('sales-report.txt')
total_sales = {}
for line in f:
    line = line.rstrip()
    entries = line.split('|')
    total_sales[entries[0]] = {'gross income': entries[1], 'total melons': entries[2]}
    

for sales_person in sorted(total_sales):
    current_record = total_sales[sales_person]
    total_melons = current_record['total melons']
    print(f"{sales_person} sold {total_melons} melons.")

    #salesperson = entries[0]
    #melons = int(entries[2])
#
    #if salesperson in salespeople:
    #    position = salespeople.index(salesperson)
#
    #    melons_sold[position] += melons
    #else:
    #    salespeople.append(salesperson)
    #    melons_sold.append(melons)


#for i in range(len(salespeople)):
#    print(f'{salespeople[i]} sold {melons_sold[i]} melons')
