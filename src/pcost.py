portfolio = '../Data/portfolio.dat'
portfolio3 = '../Data/portfolio3.dat'

def portfolio_cost(filename: str) -> None:
    tot_cost = 0
    with open(filename, 'r') as f:
        for line in f:
            try:
                _, qty, price = line.split()
                tot_cost += int(qty) * float(price)
            except ValueError as e:
                print(f'Unable to parse: {line}Reason: {e}\n')
    return format(tot_cost, '.2f')

print(portfolio_cost(portfolio3))
