class docking_aid:
  '''Help the ship dock by solving the docking parameters.'''
  def __init__(self, filename='input'):
    self.filename = filename
    self.test()
    self.day_14()
    return

  def load_file(self):
    with open(self.filename) as file:
      data = [line.strip() for line in file]
    return data

  def docking_program(self, data):
    mask = ''
    mem = {}
    for line in data:
      fst_half, scd_half = [half.strip() for half in line.split('=')]
      if fst_half.startswith('mask'):
        mask = scd_half
      elif fst_half.startswith('mem'):
        start, stop = fst_half.find('[') + 1, fst_half.find(']')
        mem[fst_half[start:stop]] = self.apply_bitmask(scd_half, mask)
    result = 0
    for value in mem.values():
      result += value
    return result

  def apply_bitmask(self, value, mask):
    value = bin(int(value))[2:]
    for zero in range(len(mask) - len(value)):
      value = '0' + value
    value = ''.join([val if m_val == 'X' else m_val
                     for val, m_val in zip(value, mask)])
    return int(value, base=2)


  def test(self):
    sample = '''mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0'''
    sample = sample.split('\n')
    test = self.docking_program(sample)
    if test == 165:
      print('Test {} successful.'.format('p1'))
    return

  def day_14(self):
    answer = self.docking_program(self.load_file())
    print('Answer: {}'.format(answer))
    return

docking_aid()