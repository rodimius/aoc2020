def parse(fileName):
  f = open(fileName, "r")
  input = f.read()
  f.close()
  array = map(int, input.splitlines())
  return [int(s) for s in input.splitlines() if s.isdigit()]

