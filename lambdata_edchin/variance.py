#___ Variance:average of the squared differences from the mean____
def variance(numbers):
    #___ calculate mean________________
    me_an=sum(numbers) / len(numbers)
    #____calculate variance using a list comprehension__________
    return sum((x - me_an) ** 2 for x in numbers) / len(numbers)