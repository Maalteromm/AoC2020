class elves_messages:
  '''Elves reported the sighting of a sea monster.
  Better assure the messages are up to date.'''
  def __init__(self, filename='input'):
    self.filename = filename
    self.test()
    self.day_19()
    return

  def load_file(self):
    rules = {}
    data = []
    with open(self.filename) as file:
      for line in file:
        if ':' in line:
          rules[line.strip().split(':')[0]] = line.strip().split(':')[1]
        elif line.strip() != '':
          data.append(line.strip())
    return rules, data

  def rules_ab(self, rules):
    self.results = {}
    for rule in rules:
      if 'a' in rules[rule]:
        self.results[rule] = 'a'
      if 'b' in rules[rule]:
        self.results[rule] = 'b'
    return

  def rules_matching(self, rules):
    rules_ini = rules['0'].split()
    strings = ['']
    for rule in rules_ini:
      strings_temp = []
      if rule not in self.results:
        self.results[rule] = self.update_results(rules, rule)
      for string in strings:
        for result in self.results[rule]:
          strings_temp.append(string + result)
      strings = strings_temp
    return strings

  def update_results(self, rules, rule):
    results_end = []
    results_ini = rules[rule]
    if '|' not in results_ini:
      strings = ['']
      results_ini = results_ini.split()
      for rule in results_ini:
        strings_temp = []
        if rule not in self.results:
          self.results[rule] = self.update_results(rules, rule)
        for string in strings:
          for result in self.results[rule]:
            strings_temp.append(string + result)
        strings = strings_temp
      results_end += strings
    else:
      results_halves = results_ini.split('|')
      for half in results_halves:
        half = half.split()
        half_temp = ['']
        for rule in half:
          strings_temp = []
          if rule not in self.results:
            self.results[rule] = self.update_results(rules, rule)
          for string in half_temp:
            for result in self.results[rule]:
              strings_temp.append(string + result)
            half_temp = strings_temp
        results_end += half_temp
    return results_end



  def remove_corrupted(self, rules, data):
    valid_strings = self.rules_matching(rules)
    valid = []
    for datum in data:
      if datum in valid_strings:
        valid.append(datum)
    return valid

  def test(self):
    sample='''0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"

ababbb
bababa
abbbab
aaabbb
aaaabbb'''
    results = ['aaaabb', 'aaabab', 'abbabb', 'abbbab', 'aabaab',
               'aabbbb', 'abaaab', 'ababbb']
#     sample = '''0: 1 2
# 1: "a"
# 2: 1 3 | 3 1
# 3: "b"'''
#     results = ['aab', 'aba']
    sample = sample.split('\n')
    rules = {}
    data = []
    for line in sample:
      if ':' in line:
        rules[line.strip().split(':')[0]] = line.strip().split(':')[1]
      elif line.strip() != '':
        data.append(line.strip())
    self.rules_ab(rules)
    valid = self.remove_corrupted(rules, data)
    if len(valid) == 2:
      print('Test successful.')
    # if self.validate_lines(rules, data, '0') == 2:
    return

  def day_19(self):
    rules, data = self.load_file()
    self.rules_ab(rules)
    valid = self.remove_corrupted(rules, data)
    print('Answer:', len(valid))
    return

elves_messages()
