class rambunctious_recitation:
  '''Yay!! This must be elves play... is it?'''
  def __init__(self):
    self.test('p1')
    self.day_15('p1')
    #self.test('p2')
    self.day_15('p2')

  def memory_game(self, spoken_start, challenge_num):
    spoken = {}
    for ind, last_spoken in enumerate(spoken_start, start=1):
      spoken[last_spoken] = ind
    while ind < challenge_num:
      ind += 1
      if last_spoken not in spoken:
        next_number = 0
      else:
        next_number = (ind - 1) - spoken[last_spoken]
      spoken[last_spoken] = ind - 1
      last_spoken = next_number
      if ind % 100000 == 0:
        print('>>> ind:', ind)
    return last_spoken

  def test(self, part):
    if part == 'p1':
      challenge = 2020
    elif part == 'p2':
      challenge = 30000000
    #samples = ['036', '132', '213', '123', '231', '321', '312']
    samples = ['036']
    answers = {}
    #answers['p1'] = [436, 1, 10, 27, 78, 438, 1836]
    #answers['p2'] = [175594, 2578, 3544142, 261214, 6895259, 18, 362]
    answers['p1'] = [436]
    answers['p2'] = [175594]
    results = 0
    for sample, answer in zip(samples, answers[part]):
      sample = [int(char) for char in sample]
      result = self.memory_game(sample, challenge)
      if result == answer:
        results += 1
    if results == len(samples):
      print('Test {} successful.'.format(part))
    return results

  def day_15(self, part):
    if part == 'p1':
      challenge = 2020
    elif part == 'p2':
      challenge = 30000000
    spoken = '2,0,1,9,5,19'
    spoken = [int(number) for number in spoken.split(',')]
    result = self.memory_game(spoken, challenge)
    print('Answer {}: {}'.format(part, result))

rambunctious_recitation()