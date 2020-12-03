class toboggan_trajectory:
  """Class for determining the toboggan trajectory"""
  def __init__(self, filename='input'):
    self.filename=filename
    self.test()
    self.day_03()

  def load_file(self):
    with open(self.filename) as file:
      data = [line.strip() for line in file]
      return data

  def solve_map(self, data):
    hrzn_len = len(data[0])
    right = 3
    down = 1
    hrz_pos = 0
    tree_count = 0
    for line in data:
      if line[hrz_pos] == '#':
        tree_count += 1
      hrz_pos += right
      if hrz_pos >= hrzn_len:
        hrz_pos -= hrzn_len
    return tree_count

  def test(self):
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
    answer = self.solve_map(sample)
    if answer == 7:
      print('Test seccessful')
    return

  def day_03(self):
    answer = self.solve_map(self.load_file())
    print('Answer: {}'.format(answer))
    return
