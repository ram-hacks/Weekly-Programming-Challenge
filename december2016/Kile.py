def challengeProblem(input):
  """ Given incomplete list of numbers 1 ... n, find the missing number """
  n = len(input) + 1
  value = (n*(n+1))/2
  for i in input:
    value -= i
  return i
