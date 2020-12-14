class shuttle_search:
  '''Searching the best shuttle to get to the airport and save the vacation.'''
  def __init__(self, filename = 'input'):
    self.filename = filename
    self.test('p1')
    self.day_13('p1')
    #self.test('p2')
    self.day_13('p2')
    return

  def load_file(self):
    with open(self.filename) as file:
      data = [line.strip() for line in file]
      earliest_time, bus_ids = int(data[0]), data[1] 
      bus_inds = [ind for ind, bus_id in enumerate(bus_ids.split(','))
                  if bus_id != 'x']
      bus_ids = [int(bus_id) for bus_id in bus_ids.split(',') if bus_id != 'x']
      return earliest_time, bus_ids, bus_inds

  def earliest_bus(self, earliest_time, bus_ids, bus_inds, part):
    time_difference = [bus_id - (earliest_time % bus_id) for bus_id in bus_ids]
    if part == 'p1':
      min_time_ind = time_difference.index(min(time_difference))
      return bus_ids[min_time_ind] * time_difference[min_time_ind]
    elif part == 'p2':
      #from 'p1' -> bus_ids[max] - time_difference[desired] = bus_inds[ind_max]
      ind_max = bus_ids.index(max(bus_ids))
      target_modulus = bus_ids[ind_max]  - bus_inds[ind_max]
      for moduli in range(100000000000000, 100000000000000*10):
        if moduli % bus_ids[ind_max] == target_modulus:
          target_modulus = moduli
          break
      target_modulus += 2 * bus_ids[ind_max]
      counter = 0
      while True:
        target_modulus += 5*bus_ids[ind_max]
        time_difference = [bus_id - (target_modulus % bus_id)
                           if bus_id != bus_ids[0] else 0
                           for bus_id in bus_ids]
        if time_difference == bus_inds:
          print(target_modulus)
          return target_modulus
        if counter > 100000:
          print('TM ->', target_modulus)
          counter = 0
        else: counter += 1

  def test(self, part):
    sample = '''939
7,13,x,x,59,x,31,19'''
    sample = sample.split()
    earliest_time, bus_ids = int(sample[0]), sample[1] 
    bus_inds = [ind for ind, bus_id in enumerate(bus_ids.split(','))
                if bus_id!= 'x']
    bus_ids = [int(bus_id) for bus_id in bus_ids.split(',') if bus_id != 'x']
    result = self.earliest_bus(earliest_time, bus_ids, bus_inds, part)
    if result == 295 and part == 'p1':
      print('Test {} successful.'.format(part))
    elif result == 1068781 and part == 'p2':
      print('Test {} successful.'.format(part))
    return

  def day_13(self, part):
    result = self.earliest_bus(*self.load_file(), part)
    print('Answer: {}'.format(result))
    return

shuttle_search()