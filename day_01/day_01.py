class ExpenseReport:
  """Learning class used on Advent of Code - Day 01"""
  def __init__(self, filename='input'):
    self.__filename__ = filename
    self.test(part='p1')
    self.test(part='p2')
    self.day_01()
    return 

  def find_sum(self, alist, part):
    if part == 'p1':
      list_1 = alist
      list_2 = list_1.copy()
      while list_2:
        entry_2 = list_2.pop()
        for entry_1 in list_1:
          if entry_1 + entry_2 == 2020:
            return entry_1 * entry_2
      else:
        return 'ERRO -- {}'.format(part)
    elif part == 'p2':
      list_1 = alist
      list_2 = list_1.copy()
      list_3 = list_1.copy()
      while list_2:
        entry_2 = list_2.pop()
        for entry_1 in list_1:
          for entry_3 in list_3:
            if entry_1 + entry_2 + entry_3 == 2020:
              return entry_1 * entry_2 * entry_3
      else:
        return 'ERRO -- {}'.format(part)

  def load_report(self):
    entries = []
    with open('./' + self.__filename__) as file:
      for line in file:
        entries.append(int(line.strip()))
    return entries

  def test(self, part):
    test_list = [1721, 979, 366, 299, 675, 1456]
    if part == 'p1':
      answer = 514579
    elif part == 'p2':
      answer = 241861950
    if self.find_sum(test_list, part) == answer:
      print("Test {} succesful".format(part))


  def day_01(self):
    self.puzzle_inputs = []
    for part in ('p1', 'p2'):
      puzzle_input = self.find_sum(self.load_report(), part)
      self.puzzle_inputs.append(puzzle_input)
      print('Puzzle input {} = {}'.format(part, puzzle_input))
    return self.puzzle_inputs

