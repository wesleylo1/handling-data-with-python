cupcake_invoice = open('CupcakeInvoices.csv')
# loop through all the data and print each row

for line in cupcake_invoice:
    line = line.strip('\n')
    print(line)

# loop through the data and print the type of cupcakes purchases

for line in cupcake_invoice:
    line = line.split(',')
    print(line[2])

# loop through data and print out total for each invoice

for line in cupcake_invoice:
    line = line.split(',')
    print(float(line[3]) * float(line[4]))

# loop through data and print out total for all invoices combined

sum_of_invoices = 0
for line in cupcake_invoice:
    line = line.split(',')
    quantity = float(line[3]) 
    price = float(line[4])
    sum_of_invoices += (quantity * price)
    
print(sum_of_invoices)

# close out file

cupcake_invoice.close()