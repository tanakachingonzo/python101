personnel ={'Joel':2000, 'Ana':2500,'Bob':1800, 'Chris':2100, 'Diana':1900}

bonus =input("Enter bonus here:")
for i in personnel:
    personnel[i]=personnel[i] + int(bonus)
print(personnel)