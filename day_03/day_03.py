class toboggan_trajectory:
  """Class for determining the toboggan trajectory"""
  def __init__(self, filename='input'):
    self.filename = filename
    self.slopes = [(1, 1),
                   (3, 1),
                   (5, 1),
                   (7, 1),
                   (1, 2)]
    self.test('p1')
    self.day_03('p1')
    self.test('p2')
    self.day_03('p2')

  def load_file(self):
    with open(self.filename) as file:
      data = [line.strip() for line in file]
      return data

  def solve_map(self, data, slope):
    hrzn_len = len(data[0])
    right = slope[0]
    down = slope[1]
    hrz_pos = 0
    tree_count = 0
    down_tmp = 1
    for line in data:
      if down_tmp == 1:
        if line[hrz_pos] == '#':
          tree_count += 1
        hrz_pos += right
        if hrz_pos >= hrzn_len:
          hrz_pos -= hrzn_len
        down_tmp -= 1
        if down_tmp == 0: 
          down_tmp = down
      else:
        down_tmp -= 1
    return tree_count

  def test(self, part):
    sample='''..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#'''
    sample = [line.strip() for line in sample.split('\n')]
    if part == 'p1':
      answer = self.solve_map(sample, self.slopes[1])
      if answer == 7:
        print('Test {} successful'.format(part))
    elif part == 'p2':
      answers = []
      for slope in self.slopes:
        answers.append(self.solve_map(sample, slope))
      #print('Test {} answers = {}'.format(part, answers))
      answer = 1
      while answers:
        answer *= answers.pop() 
      if answer == 336:
        print('Test {} successful'.format(part))
      #else: print('Test {} = {}'.format(part, answer))

    return

  def day_03(self, part):
    if part == 'p1':
      answer = self.solve_map(self.load_file(), self.slopes[1])
      print('Answer {}: {}'.format(part, answer))
    elif part == 'p2':
      answers =[]
      for slope in self.slopes:
        answers.append(self.solve_map(self.load_file(), slope))
      answer = 1
      while answers:
        answer *= answers.pop()
      print('Answer {}: {}'.format(part, answer))
    return
