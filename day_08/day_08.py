class console_fixing:
  '''Class for fixing the boot code of random handheld consoles'''
  def __init__(self, filename='input'):
    self.filename = filename
    self.test('p1')
    self.day_08('p1')
    self.test('p2')
    self.day_08('p2')
    return

  def load_file(self):
    with open(self.filename) as file:
      data = file.readlines()
    data.append('end +0')
    return data

  def read_command_line(self, line):
    command, value = line.strip().split()
    value = int(value)
    return command, value

  def run_boot_sequence(self, data, part, run=0, jmp_nop_lines=[]):
    acc = 0
    end = 0
    read_lines = []
    if run == 0:
      jmp_nop_lines = []
    else:
      jmp_nop_lines = jmp_nop_lines
    current_line = 0
    while True:
      if current_line in read_lines:
        if part == 'p1':
          break
        else:
          acc, end = self.try_fixing_it(data, jmp_nop_lines)
          break
      else:
        read_lines.append(current_line)
      command, value = self.read_command_line(data[current_line])
      if command == 'acc':
        acc += value
      elif command == 'jmp':
        if run == 0:
          jmp_nop_lines.append(current_line)
        current_line += value
        continue
      elif command == 'nop':
        if run == 0:
          jmp_nop_lines.append(current_line)
      elif command == 'end':
        end = 1
        break
      current_line += 1
    return acc, end

  def try_fixing_it(self, data, jmp_nop_lines):
    while jmp_nop_lines:
      line_change = jmp_nop_lines.pop()
      command, value = self.read_command_line(data[line_change])
      if command == 'jmp':
        data[line_change] = ' '.join(['nop', str(value)])
      elif command == 'nop':
        data[line_change] = ' '.join(['jmp', str(value)])
      acc, end = self.run_boot_sequence(data, 'p2', 1, jmp_nop_lines)
      if end == 1:
        break
    return acc, end


  def test(self, part):
    sample = '''nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
end +0'''
    sample = sample.split('\n')
    acc, end = self.run_boot_sequence(sample, part)
    if part == 'p1' and acc == 5 and end == 0:
      testflag = 1
    elif part == 'p2' and acc == 8 and end == 1:
      testflag = 1
    else:
      testflag = 0
    if testflag == 1:
      print('Test {} successful.'.format(part))
    else:
      print('Test {} UNsuccessful.'.format(part))
    return acc

  def day_08(self, part):
    acc, end = self.run_boot_sequence(self.load_file(), part)
    if end == 1 and part == 'p2':
      dflag = 1
    elif part == 'p1':
      dflag = 1
    else:
      dflag = 0
    if dflag == 1:
      print('Answer {}: {}.'.format(part, acc))
    else:
      print('{} not solved.'.format(part))
    return acc, end