class docking_aid:
  '''Help the ship dock by solving the docking parameters.'''
  def __init__(self, filename='input'):
    self.filename = filename
    self.test('p1')
    self.day_14('p1')
    self.test('p2')
    self.day_14('p2')
    return

  def load_file(self):
    with open(self.filename) as file:
      data = [line.strip() for line in file]
    return data

  def docking_program(self, data, part):
    mask = ''
    mem = {}
    for line in data:
      fst_half, scd_half = [half.strip() for half in line.split('=')]
      if fst_half.startswith('mask'):
        mask = scd_half
      elif fst_half.startswith('mem'):
        start, stop = fst_half.find('[') + 1, fst_half.find(']')
        if part == 'p1':
          mem[fst_half[start:stop]] = self.apply_bitmask(scd_half, mask)
        elif part == 'p2':
          address = fst_half[start:stop]
          addresses = self.apply_bitmask_v2(address, mask)
          for address in addresses: mem[address] = int(scd_half)
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

  def apply_bitmask_v2(self, value, mask):
    value = bin(int(value))[2:]
    for zero in range(len(mask) - len(value)):
      value = '0' + value
    value = ''.join(['X' if m_val == 'X' else '1' if m_val == '1' else val
                     for val, m_val in zip(value, mask)])
    addresses = self.address_combinations(value)
    return [int(address, base=2) for address in addresses]

  def address_combinations(self, value, addresses=[]):
    addresses = []
    addresses.append(value)
    while True:
      tmp_addrss = []
      addresses_len = 0
      for address in addresses:
        if 'X' in address:
          tmp_addrss.append(address.replace('X', '0', 1))
          tmp_addrss.append(address.replace('X', '1', 1))
        else:
          addresses_len += 1
      if addresses_len == len(addresses):
        break
      addresses = tmp_addrss.copy()
    return addresses
        


  def test(self, part):
    if part == 'p1':
      sample = '''mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0'''
    elif part == 'p2':
      sample = '''mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1'''
    sample = sample.split('\n')
    test = self.docking_program(sample, part)
    if test == 165 and part == 'p1':
      print('Test {} successful.'.format(part))
    elif test == 208 and part == 'p2':
      print('Test {} successful.'.format(part))
    return

  def day_14(self, part):
    answer = self.docking_program(self.load_file(), part)
    print('Answer {}: {}'.format(part, answer))
    return

docking_aid()