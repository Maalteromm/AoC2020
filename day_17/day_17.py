from copy import deepcopy as dc
class conway_cubes:
  '''Simulates Conway Cubes in a pocket dimension.'''
  def __init__(self, filename='input'):
    self.filename = filename
    self.dimensions = None
    self.test('p1')
    self.day_17('p1')
    self.test('p2')
    self.day_17('p2')
    return

  def load_file(self, part):
    self.data = {}
    self.active = 0
    with open(self.filename) as file:
      data = [line.strip() for line in file]
    dx, dy = len(data), len(data[0])
    if part == 'p1':
      self.data = {(x, y, 0) : 0 if data[x][y] == '.' else 1
              for y in range(dy) for x in range(dx)}
      dx, dy, dz = (0, dx-1), (0, dy-1), (0, 0)
      self.dimensions = (dx, dy, dz)
    elif part == 'p2':
      self.data = {(x, y, 0, 0) : 0 if data[x][y] == '.' else 1
                for y in range(dy) for x in range(dx)}
      dx, dy, dz, dt = (0, dx-1), (0, dy-1), (0, 0), (0, 0)
      self.dimensions = (dx, dy, dz, dt)
    for state in self.data.values():
      self.active += state
    return

  def cycle_dimension(self):
    self.data_tmp = dc(self.data)
    if len(self.dimensions) == 3:
      dx, dy, dz = tuple(((dim[0]-1, dim[1]+1) for dim in self.dimensions))
    elif len(self.dimensions) == 4:
      dx, dy, dz, dt = tuple(((dim[0]-1, dim[1]+1) for dim in self.dimensions))
    for x in range(dx[0], dx[1]+1):
      for y in range(dy[0], dy[1]+1):
        for z in range(dz[0], dz[1]+1):
          if len(self.dimensions) == 4:
            for t in range(dt[0], dt[1]+1):
              if (x, y, z, t) not in self.data_tmp:
                self.data[x, y, z, t] = 0
                self.data_tmp[x, y, z, t] = 0
              self.state_change((x, y, z, t))
          else:
            if (x, y, z) not in self.data_tmp:
              self.data[x, y, z] = 0
              self.data_tmp[x, y, z] = 0
            self.state_change((x, y, z))
    if len(self.dimensions) == 3:
      self.dimensions = (dx, dy, dz)
    elif len(self.dimensions) == 4:
      self.dimensions = (dx, dy, dz, dt)
    return

  def state_change(self, coords):
    state = 0
    for x in range(coords[0]-1, coords[0]+2):
      for y in range(coords[1]-1, coords[1]+2):
        for z in range(coords[2]-1, coords[2]+2):
          if len(coords) == 4:
            for t in range(coords[3]-1, coords[3]+2):
              if (x, y, z, t) == coords:
                continue
              elif (x, y, z, t) not in self.data_tmp:
                self.data[x, y, z, t] = 0
                self.data_tmp[x, y, z, t] = 0
              else:
                state += self.data_tmp[x, y, z, t]
          else:
            if (x, y, z) == coords:
              continue
            elif (x, y, z) not in self.data_tmp:
              self.data[x, y, z] = 0
              self.data_tmp[x, y, z] = 0
            else:
              state += self.data_tmp[x, y, z]
    if self.data_tmp[coords] == 1 and state not in (2, 3):
      self.data[coords] = 0
      self.active -= 1
    elif self.data_tmp[coords] == 0 and state == 3:
      self.data[coords] = 1
      self.active += 1
    return

  def run_cycles(self, cycles):
    while cycles:
      self.cycle_dimension()
      cycles -= 1
    return

  def test(self, part):
    self.data = {}
    self.active = 0
    sample = '''.#.
..#
###'''

    sample = sample.split('\n')
    dx, dy = len(sample), len(sample[0])
    if part == 'p1':
      self.data = {(x, y, 0) : 0 if sample[x][y] == '.' else 1
                for y in range(dy) for x in range(dx)}
      dx, dy, dz = (0, dx-1), (0, dy-1), (0, 0)
      self.dimensions = (dx, dy, dz)
    elif part == 'p2':
      self.data = {(x, y, 0, 0) : 0 if sample[x][y] == '.' else 1
                for y in range(dy) for x in range(dx)}
      dx, dy, dz, dt = (0, dx-1), (0, dy-1), (0, 0), (0, 0)
      self.dimensions = (dx, dy, dz, dt)
    for state in self.data.values():
      self.active += state
    self.run_cycles(6)
    if self.active == 112 and part == 'p1':
      print('Test {} successful.'.format(part))
    if self.active == 848 and part == 'p2':
      print('Test {} successful.'.format(part))
    return

  def day_17(self, part):
    self.load_file(part)
    if part == 'p1':
      self.run_cycles(6)
      print('Answer {}: {}'.format(part, self.active))
    elif part == 'p2':
      self.run_cycles(6)
      print('Answer {}: {}'.format(part, self.active))
    return

conway_cubes()