import math

class evasive_actions:
  '''Class for evaluating the movement of the ferry while avoiding a
  most terrible storm.'''
  def __init__(self, filename='input'):
    self.filename = filename
    self.test('p1')
    self.day_12('p1')
    self.test('p2')
    self.day_12('p2')
    return

  def load_file(self):
    with open(self.filename) as file:
      data = [line.strip() for line in file]
      return data

  def manhatan_distance(self, data, part):
    if part == 'p1':
      movement = self.instruction_navigation(data)       
    elif part == 'p2':
      movement = self.waypoint_navigation(data)
    manh_dist = round(abs(movement[0]) + abs(movement[1]))
    return manh_dist

  def instruction_navigation(self, data):
    vert_mov, hori_mov, facing = 0, 0, 0
    for instruction in data:
      command = instruction[0]
      val = int(instruction[1:])
      if command == 'N':
        vert_mov += val
      elif command == 'E':
        hori_mov += val
      elif command == 'S':
        vert_mov -= val
      elif command == 'W':
        hori_mov -= val
      elif command == 'L':
        facing += val
      elif command == 'R':
        facing -= val
      elif command == 'F':
        vm, hm = self.forward_movement(val, facing)
        vert_mov += vm
        hori_mov += hm
    return vert_mov, hori_mov

  def waypoint_navigation(self, data):
    vert_mov, hori_mov = 0, 0
    wp_vpos, wp_hpos = 1, 10
    for instruction in data:
      command = instruction[0]
      val = int(instruction[1:])
      #print('--------------------------\ninstruction: {}, val: {}.'.format(
      #                                                        command, val))
      #print('vert_mov: {}, hori_mov: {}, wp_vpos: {}, wp_hpos: {}.'.format(
      #     vert_mov, hori_mov, wp_vpos, wp_hpos))
      if command == 'N':
        wp_vpos += val
      elif command == 'E':
        wp_hpos += val
      elif command == 'S':
        wp_vpos -= val
      elif command == 'W':
        wp_hpos -= val
      elif command in 'LR':
        wp_vpos, wp_hpos = self.rotate_waypoint(wp_vpos, wp_hpos, val, command)
        #print('Rotated - wp_vpos {}, wp_hpos {}.'.format(wp_vpos, wp_hpos))
      elif command == 'F':
        # All engines ahead Full!!
        vmov = wp_vpos * val
        hmov = wp_hpos * val
        vert_mov += vmov
        hori_mov += hmov
        #print('Forward, vert: {}, hori: {}.'.format(vert_mov, hori_mov))
    #print('V: {}, H:{}'.format(vert_mov, hori_mov))
    return vert_mov, hori_mov


  def rotate_waypoint(self, vert_pos, hori_pos, angle, direction):
    if direction == 'R':
      angle *= -1
    angle = math.radians(angle)
    rot_matrix = [[math.cos(angle), math.sin(angle)], 
                  [math.sin(angle), math.cos(angle)]]
    hori_pos_new = [(rot_matrix[0][0] * hori_pos) - (rot_matrix[0][1] * vert_pos)]
    vert_pos_new = [(rot_matrix[1][0] * hori_pos) + (rot_matrix[1][1] * vert_pos)]
    return round(vert_pos_new[0]), round(hori_pos_new[0])
  
  def forward_movement(self, distance, direction):
    angle = math.radians(direction)
    vertical_movement = math.sin(angle) * distance
    horizonal_movement = math.cos(angle) * distance
    return vertical_movement, horizonal_movement

  def test(self, part):
    testflag = 0
    sample = '''F10
N3
F7
R90
F11'''
    sample = [line.strip() for line in sample.split()]
    manh_dist = self.manhatan_distance(sample, part)
    if manh_dist == 25 and part =='p1':
      testflag = 1
    elif manh_dist == 286 and part == 'p2':
      testflag = 1
    if testflag == 1:
      print('Test {} successful.'.format(part))
    return manh_dist

  def day_12(self, part):
    manh_dist = self.manhatan_distance(self.load_file(), part)
    print('Answer {}: {}'.format(part, manh_dist))
    return

evasive_actions()