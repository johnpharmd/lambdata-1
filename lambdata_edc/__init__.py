VERSION=1.0

def varedc(results):
  #calculate the variance : the average of the squared differences from the mean.
  # calculate mean
  m = sum(results) / len(results)
  # calculate variance using a list comprehension
  return sum((xi - m) ** 2 for xi in results) / len(results)