class adapter_array:
  '''Class for dealing with the joltage differential between the output and
  the device built-in adapter. Use much adpters!!'''
  def __init__(self, filename='input'):
    self.filename=filename
    self.test('p1')
    self.test('p2')
    self.day_10('p1')
    self.day_10('p2')
    return

  def load_file(self):
    with open(self.filename) as file:
      data = [int(line.strip()) for line in file]
      return data

  def joltage_difference(self, data):
    joltage_ini = 0
    joltage_built_in = max(data) + 3
    data += [joltage_ini, joltage_built_in]
    data.sort()
    jolt_diff = [data[ind+1] - data[ind] for ind in range(len(data) - 1)]
    j1, j3 = jolt_diff.count(1), jolt_diff.count(3)
    return j1, j3, jolt_diff, data

  def adapter_arrangement(self, data, jolt_diff):
    #print('------------ 1 ------------')
    #print('len data: ', len(data), 'len jolt_jiff: ', len(jolt_diff))
    j3_inds = [ind+1 for ind, val in enumerate(jolt_diff) if val == 3]
    j3_inds = [0] + j3_inds
    section_arrangements = []
    for ind in range(len(j3_inds)-1):
        section = data[j3_inds[ind]:j3_inds[ind+1]]
        section_arrangements.append(len(self.section_combinations(section, [])))
    arrangements = 1
    #print('section_arrangements:\n', section_arrangements)
    for combination in section_arrangements:
      #print('combination = ', combination)
      arrangements *= combination
    #print(arrangements)
    return arrangements

  def add_section(self, section, combinations):
    if section not in combinations:
      combinations.append(section)

  def section_combinations(self, section, combinations=[], lvl=0):
    lvl += 1
    #print('------------ {} ------------'.format(lvl))
    self.add_section(section, combinations)
    for item in section[1:-1]:
      section_tmp = section.copy()
      #print('section_tmp:\n', section_tmp)
      section_tmp.remove(item)
      #print('item_removed = ', item)
      #print('section_tmp:\n', section_tmp)
      jolt_diff = [section_tmp[ind+1] - section_tmp[ind] 
                   for ind in range(len(section_tmp) - 1)]
      if max(jolt_diff) > 3:
        #print('jolt_diff > 3')
        lvl -= 1
        #print('>>> {} <<<'.format(lvl))
        return combinations
      else:
        self.add_section(section_tmp, combinations)
        #print('combinations:\n', combinations,'\n+++++++++++')
        self.section_combinations(section_tmp, combinations, lvl)
    #print('combinations returned =\n', combinations,'\n'+'=.'*10)
    return combinations

  def test(self, part):
    testflag = 0
    sample = [28, 33, 18, 42, 31, 14, 46, 20, 48, 47, 24, 23, 49, 45, 19, 38,
              39, 11, 1, 32, 25, 35, 8, 17, 7, 9, 4, 2, 34, 10, 3]
    j1, j3, jolt_diff, sample = self.joltage_difference(sample)
    if j1 == 22 and j3 == 10 and part == 'p1':
      testflag = 1
    elif j1 == 22 and j3 == 10 and part == 'p2':
      arrangements = self.adapter_arrangement(sample, jolt_diff)
      if arrangements == 19208:
        testflag = 1
    if testflag == 1:
      print('Test {} successful.'.format(part))
    return j1, j3

  def day_10(self, part):
    j1, j3, jolt_diff, data = self.joltage_difference(self.load_file())
    if part == 'p1':
      answer = j1 * j3
      print('Answer {}: {}'.format(part, answer))
    elif part == 'p2':
      answer = self.adapter_arrangement(data, jolt_diff)
      print('Answer {}: {}'.format(part, answer))
    return answer