class XMAS_breaking:
  '''Class for breaking the XMAS encryption protocol.'''
  def __init__(self, filename='input'):
    self.filename = filename
    self.test('p1')
    self.day_09('p1')
    self.test('p2')
    self.day_09('p2')
    return

  def load_file(self):
    with open(self.filename) as file:
      data = [int(x) for x in file]
      return data

  def find_valid_sum(self, target, data):
    data_temp = data.copy()
    for ind in range(len(data)):
      num = data_temp.pop(ind)
      data_temp = [x + num for x in data_temp]
      if target in data_temp:
        return True
      data_temp = data.copy()
    return False

  def break_xmas(self, data, preamble):
    for ind, num in enumerate(data[preamble:]):
      ind_data = preamble + ind
      if not self.find_valid_sum(num, data[ind_data-preamble:ind_data]):
        return num

  def find_encrypt_weakness(self, target, data):
    for ind_start in range(len(data)):
      #print('-'*12+'\nIND_START =', ind_start)
      ind_end = ind_start + 2
      num = 0
      while num < target:
        num = 0
        #print('num_start =', num)
        for x in data[ind_start:ind_end]: num += x
        #print(ind_start, ind_end)
        #print(data[ind_start:ind_end])
        #print('num =', num)
        if num == target:
          #print('num == target')
          enc_weak_sequence = data[ind_start:ind_end]
          enc_weak = min(enc_weak_sequence) + max(enc_weak_sequence)
          return enc_weak
        ind_end += 1
        #print('ind_end =', ind_end)
    return

  def test(self, part):
    testflag = 0
    preamble = 5
    sample = '''35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576'''
    sample = [int(x) for x in sample.split()]
    num = self.break_xmas(sample, preamble)
    if num == 127 and part == 'p1':
      testflag = 1
    elif num == 127 and part == 'p2':
      enc_weak = self.find_encrypt_weakness(num, sample)
      if enc_weak == 62:
        testflag = 1
    if testflag == 1:
      print('Test {} successful.'.format(part))
    return

  def day_09(self, part):
    preamble = 25
    num = self.break_xmas(self.load_file(), preamble)
    if part == 'p1':
      answer = num
    elif part == 'p2':
      answer = self.find_encrypt_weakness(num, self.load_file())
    print('Answer {}: {}'.format(part, answer))
    return answer