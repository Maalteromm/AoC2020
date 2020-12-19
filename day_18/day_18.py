class solve_homework:
  '''Help the kid solve his math homework.'''
  def __init__(self, filename = 'input'):
    self.filename=filename
    self.test('p1')
    self.day_18('p1')
    self.test('p2')
    self.day_18('p2')
    return

  def load_file(self):
    with open(self.filename) as file:
      data = [line.strip() for line in file]
    return data

  def evaluate(self, line, part):
    if '(' in line:
      line = self.eval_parenthesis(line, part)
    return self.eval_expression(line, part)

  def eval_parenthesis(self, line, part):
    ind = 0
    while True:
      if not '(' in line:
        break
      if line[ind] == '(':
        iopen = ind
      if line[ind] == ')':
        iclose = ind
        line = self.eval_parenthesis(
               line[:iopen] + 
               self.eval_expression(line[iopen+1:iclose], part) +
               line[iclose+1:], part
                                    )
      ind += 1
    return line

  def eval_expression(self, line, part):
    if part == 'p1':
      operator_inds = [char for char in line if char in '+*']
      line = line.replace('*', '+')
      nums = [int(num.strip()) for num in line.split('+')]
      num = None
      for ind in range(1, len(nums)):
        if num == None:
          num = self.eval_operator(nums[ind], nums[ind-1], operator_inds[ind-1])
        else:
          num = self.eval_operator(nums[ind], num, operator_inds[ind-1])
    elif part == 'p2':
      line_tmp = line.split('*')
      nums_tmp = []
      for section in line_tmp:
        if '+' in section:
          num = 0
          for val in section.split('+'):
            num += int(val.strip())
          nums_tmp.append(num)
        else:
          nums_tmp.append(int(section.strip()))
      num = 1
      for val in nums_tmp:
        num *= val
    return str(num)

  def eval_operator(self, num1, num2, operator):
    if operator == '*':
      return num1 * num2
    elif operator == '+':
      return num1 + num2

  def test(self, part):
    samples = ['2 * 3 + (4 * 5)', '5 + (8 * 3 + 9 + 3 * 4 * 3)',
               '5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))',
               '((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2']
    results_p1 = [26, 437, 12240, 13632]
    results_p2 = [46, 1445, 669060, 23340]
    if part == 'p1': results = results_p1
    else: results = results_p2
    for sample, result in zip(samples, results):
      if int(self.evaluate(sample, part)) == result:
        print('part:', part, '--', sample, '-> successful.')
    return

  def day_18(self, part):
    results = [int(self.evaluate(line, part)) for line in self.load_file()]
    answer = sum(results)
    print('Answer {}: {}'.format(part, answer))
    return

solve_homework()