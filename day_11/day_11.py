from copy import deepcopy
class seat_modelling:
  '''Class for modelling which is the best place to sit.'''
  def __init__(self, filename='input'):
    self.filename = filename
    self.test('p1')
    self.day_11('p1')
    self.test('p2')
    self.day_11('p2')
    return

  def load_file(self):
    with open(self.filename) as file:
      data = [line.strip() for line in file]
    return data

  def round_sitting(self, data, part):
    iteration=0
    data = self.add_floors(data)
    data = [[char for char in line] for line in data]
    data_new = deepcopy(data)
    while self.check_seat_change(data, data_new, iteration):
      #print('_______________________\n{}'.format(iteration))
      data = deepcopy(data_new)
      for ind_line, line in enumerate(data):
        for ind_col, seat in enumerate(line):
          if seat == 'L' and self.check_availability(data,
                                                    (ind_line, ind_col), part):
            data_new[ind_line][ind_col] = '#'
          if seat == '#' and self.check_annoyance(data,
                                                 (ind_line, ind_col), part):
            data_new[ind_line][ind_col] = 'L'
      iteration += 1
      seat_map = ''.join([''.join(line) + '\n' for line in data])
      #print(seat_map)
      #seat_new = ''.join([''.join(line) + '\n' for line in data_new])
      #print(seat_new)
    occupied_seats = [line.count('#') for line in data]
    return sum(occupied_seats)

  def check_seat_change(self, data_old, data_new, iteration):
    #print('Checking seat change')
    if iteration == 0 or data_old != data_new:
      #print(' -- True')
      return True
    elif data_old == data_new:
      #print('Total iterations =', iteration)
      return False

  def check_availability(self, data, inds, part):
    #print('Checking check_availability: ', inds)
    ind_line, ind_col = inds
    if part == 'p1':
      seat_neighborhood = [data[ind_line-1][ind_col-1:ind_col+2],
                     [data[ind_line][ind_col-1], 'X' ,data[ind_line][ind_col+1]],
                      data[ind_line+1][ind_col-1:ind_col+2]]
      seat_neighborhood = ''.join([''.join(line) for line in seat_neighborhood])
      if '#' not in seat_neighborhood:
        #print(' -- True')
        return True
      else:
        #print(' -- False')
        return False
    elif part == 'p2':
      ind_line_min, ind_line_max = 0, len(data) - 1
      ind_col_min, ind_col_max = 0, len(data[0]) - 1
      look_N = ''
      ind_l_N = ind_line
      while not look_N:
        ind_l_N -= 1
        if ind_l_N < ind_line_min:
          break
        char = data[ind_l_N][ind_col]
        if char != '.':
          look_N = char
      look_S = ''
      ind_l_S = ind_line
      while not look_S:
        ind_l_S += 1
        if ind_l_S > ind_line_max:
          break
        char = data[ind_l_S][ind_col]
        if char != '.':
          look_S = char
      look_E = ''
      ind_c_E = ind_col
      while not look_E:
        ind_c_E += 1
        if ind_c_E > ind_col_max:
          break
        char = data[ind_line][ind_c_E]
        if char != '.':
          look_E = char
      look_W = ''
      ind_c_W = ind_col
      while not look_W:
        ind_c_W -= 1
        if ind_c_W < ind_col_min:
          break
        char = data[ind_line][ind_c_W]
        if char != '.':
          look_W = char
      look_NE = ''
      ind_l_NE, ind_c_NE = ind_line, ind_col
      while not look_NE:
        ind_l_NE -= 1
        ind_c_NE += 1
        if ind_l_NE < ind_line_min or ind_c_NE > ind_col_max:
          break
        char = data[ind_l_NE][ind_c_NE]
        if char != '.':
          look_NE = char
      look_NW = ''
      ind_l_NW, ind_c_NW = ind_line, ind_col
      while not look_NW:
        ind_l_NW -= 1
        ind_c_NW -= 1
        if ind_l_NW < ind_line_min or ind_c_NW < ind_col_min:
          break
        char = data[ind_l_NW][ind_c_NW]
        if char != '.':
          look_NW = char
      look_SW = ''
      ind_l_SW, ind_c_SW = ind_line, ind_col
      while not look_SW:
        ind_l_SW += 1
        ind_c_SW -= 1
        if ind_l_SW > ind_line_max or ind_c_SW < ind_col_min:
          break
        char = data[ind_l_SW][ind_c_SW]
        if char != '.':
          look_SW = char
      look_SE = ''
      ind_l_SE, ind_c_SE = ind_line, ind_col
      while not look_SE:
        ind_l_SE += 1
        ind_c_SE += 1
        if ind_l_SE > ind_line_max or ind_c_SE > ind_col_max:
          break
        char = data[ind_l_SE][ind_c_SE]
        if char != '.':
          look_SE = char
      seats_visible = [look_N, look_NE, look_E, look_SE, look_S, look_SW,
                       look_W, look_NW]
      if '#' not in seats_visible:
        return True
      else:
        return False

  def check_annoyance(self, data, inds, part):
    #print('Checking check_annoyance: ', inds)
    ind_line, ind_col = inds
    if part == 'p1':
      seat_neighborhood = [data[ind_line-1][ind_col-1:ind_col+2],
                     [data[ind_line][ind_col-1], 'X' ,data[ind_line][ind_col+1]],
                      data[ind_line+1][ind_col-1:ind_col+2]]
      seat_neighborhood = sum([line.count('#') for line in seat_neighborhood])
      if seat_neighborhood >= 4:
        #print(' -- True')
        return True
      else:
        #print(' -- False')
        return False
    elif part == 'p2':
      ind_line_min, ind_line_max = 0, len(data) - 1
      ind_col_min, ind_col_max = 0, len(data[0]) - 1
      look_N = ''
      ind_l_N = ind_line
      while not look_N:
        ind_l_N -= 1
        if ind_l_N < ind_line_min:
          break
        char = data[ind_l_N][ind_col]
        if char != '.':
          look_N = char
      look_S = ''
      ind_l_S = ind_line
      while not look_S:
        ind_l_S += 1
        if ind_l_S > ind_line_max:
          break
        char = data[ind_l_S][ind_col]
        if char != '.':
          look_S = char
      look_E = ''
      ind_c_E = ind_col
      while not look_E:
        ind_c_E += 1
        if ind_c_E > ind_col_max:
          break
        char = data[ind_line][ind_c_E]
        if char != '.':
          look_E = char
      look_W = ''
      ind_c_W = ind_col
      while not look_W:
        ind_c_W -= 1
        if ind_c_W < ind_col_min:
          break
        char = data[ind_line][ind_c_W]
        if char != '.':
          look_W = char
      look_NE = ''
      ind_l_NE, ind_c_NE = ind_line, ind_col
      while not look_NE:
        ind_l_NE -= 1
        ind_c_NE += 1
        if ind_l_NE < ind_line_min or ind_c_NE > ind_col_max:
          break
        char = data[ind_l_NE][ind_c_NE]
        if char != '.':
          look_NE = char
      look_NW = ''
      ind_l_NW, ind_c_NW = ind_line, ind_col
      while not look_NW:
        ind_l_NW -= 1
        ind_c_NW -= 1
        if ind_l_NW < ind_line_min or ind_c_NW < ind_col_min:
          break
        char = data[ind_l_NW][ind_c_NW]
        if char != '.':
          look_NW = char
      look_SW = ''
      ind_l_SW, ind_c_SW = ind_line, ind_col
      while not look_SW:
        ind_l_SW += 1
        ind_c_SW -= 1
        if ind_l_SW > ind_line_max or ind_c_SW < ind_col_min:
          break
        char = data[ind_l_SW][ind_c_SW]
        if char != '.':
          look_SW = char
      look_SE = ''
      ind_l_SE, ind_c_SE = ind_line, ind_col
      while not look_SE:
        ind_l_SE += 1
        ind_c_SE += 1
        if ind_l_SE > ind_line_max or ind_c_SE > ind_col_max:
          break
        char = data[ind_l_SE][ind_c_SE]
        if char != '.':
          look_SE = char
      seats_visible = [look_N, look_NE, look_E, look_SE, look_S, look_SW,
                       look_W, look_NW]
      seats_visible = seats_visible.count('#')
      if seats_visible >= 5:
        return True
      else:
        return False

  def add_floors(self, data):
    if data[0] == '.'*len(data[0]):
      return data
    data.insert(0, '.'*len(data[0]))
    data.append('.'*len(data[0]))
    data = ['.' + line + '.' for line in data]
    return data

  def test(self, part):
    sample ='''L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL'''
    sample = [line.strip() for line in sample.split()]
    answer = self.round_sitting(sample, part)
    if answer == 37 and part == 'p1':
      print('Test {} successful.'.format(part))
    elif answer == 26 and part == 'p2':
      print('Test {} successful.'.format(part))
    return

  def day_11(self, part):
    data = self.load_file()
    answer = self.round_sitting(data, part)
    print('Answer {}: {}'.format(part, answer))
    return answer

seat_modelling()
