symbols = 'AAPL,IBM,MSFT,YHOO,SCO'

print(symbols[1])
# symbols[0] = 'a'

symbols = symbols + ',' + 'GOOG'
print(symbols)

symbols = 'HPQ' + ',' + symbols
print(symbols)

print('IBM' in symbols)

print('AA' in symbols)

print(symbols.lower())
print(symbols.find('CO'))
print(symbols[:5])
print(symbols[24:26])

name = "   " + symbols[1:4] + "    "
print(name)
print(name.strip())
