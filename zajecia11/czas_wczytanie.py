from datetime import datetime

konkretna_data = '2001-02-03'

data = datetime.strptime(konkretna_data, '%Y-%m-%d')

print(data)
print(type(data))

# Więcej tu: https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
