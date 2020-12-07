class custom_declaration_forms:
  '''Class for solving custom declaration forms.'''
  def __init__(self, filename='input'):
    self.filename = filename
    self.test('p1')
    self.day_06('p1')
    self.test('p2')
    self.day_06('p2')
    return

  def load_file(self, filename):
    with open(filename) as file:
      dados = file.readlines()
      return dados

  def check_answers(self, data, part):
    '''Finds which questions where answered with "yes".'''
    questions = ''
    group_answers = []
    p2flag = 0
    for line in data:
      #print('\n' + '-'*10)
      #print(line.strip())
      if line.strip() == '':
        #print('line empty')
        #print(questions)
        group_answers.append(len(questions)) 
        questions = line.strip()
        p2flag = 0
      else:
        if part == 'p1':
          #print('else p1')
          for char in line.strip():
            if char not in questions:
              #print(char)
              questions += char
        elif part == 'p2':
          #print('else p2')
          quest_temp = ''
          if questions == '' and p2flag == 0:
            questions = line.strip()
            p2flag = 1
            #print(questions)
          else:
            for char in line.strip():
              if char in questions:
                #print(char)
                quest_temp += char
            questions = quest_temp
            #print(questions)
    #print(questions)
    group_answers.append(len(questions))
    return group_answers

  def test(self, part):
    sample = '''abc

a
b
c

ab
ac

a
a
a
a

b'''
    sample = sample.split('\n')
    answ = self.check_answers(sample, part)
    if part == 'p1':
      if answ == [3, 3, 3, 1, 1]:
        print('Test {} successful.'.format(part))
    elif part == 'p2':
      if answ == [3, 0, 1, 1, 1]:
        print('Test {} successful.'.format(part))
    return

  def day_06(self, part):
    count_sum = 0
    answers = self.check_answers(self.load_file(self.filename), part)
    for answer in answers: count_sum += answer
    print('Answer {}: {}'.format(part, count_sum))
    return count_sum