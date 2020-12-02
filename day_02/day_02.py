class otcp_passw:
  """Class for checking whether passwords were in accordance to the
  Official Toboggan Corporate Policy."""
  def __init__(self, filename="input"):
    self.filename = filename
    self.test('p1')
    self.test('p2')
    self.day_02('p1')
    self.day_02('p2')
    return

  def load_passw_list(self):
    """reads the file"""
    with open(self.filename) as file:
      data = file.readlines()
    return data

  def parse_passw_list(self, data):
    """parses the data"""
    passwords = []
    policies = {}
    policies['min'] = []
    policies['max'] = []
    policies['letter'] = []
    for line in data:
      passwords.append(line.split()[2])
      policies['min'].append(int(line.split()[0].split('-')[0]))
      policies['max'].append(int(line.split()[0].split('-')[1]))
      policies['letter'].append(line.split()[1].replace(':', ''))
    return passwords, policies

  def check_passw(self, passwords, policies, part):
    """checks if password is in line with its policy and returns the number
    of valid passwords"""
    count = 0
    if part == 'p1':
      for ind, passw in enumerate(passwords):
        ind_min, ind_max = policies['min'][ind], policies['max'][ind] 
        occurrences = passw.count(policies['letter'][ind])
        if occurrences >= ind_min and occurrences <= ind_max:
          count += 1
    elif part == 'p2':
      for ind, passw in enumerate(passwords):
        ind_1, ind_2 = policies['min'][ind] - 1, policies['max'][ind] - 1
        letter = policies['letter'][ind]
        if int(passw[ind_1] == letter) + int(passw[ind_2] == letter) == 1:
          count += 1
    return count

  def test(self, part):
    """tests the example"""
    sample = '''1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc'''

    passw, pol = self.parse_passw_list(sample.split('\n'))
    if part == 'p1':
      if self.check_passw(passw, pol, part) == 2:
        print('Test {} successful'.format(part))
    elif part == 'p2':
      if self.check_passw(passw, pol, part) == 1:
        print('Test {} successful'.format(part))
    return

  def day_02(self, part):
    """checks the passwords in the input file"""
    answer = self.check_passw(
                  *self.parse_passw_list(self.load_passw_list()), part
                             )
    print('Answer {}: {}'.format(part, answer))
    return answer