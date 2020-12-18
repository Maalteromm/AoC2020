import time
class ticket_to_ride:
  '''Class for parsing and validating ticket fields.'''
  def __init__(self, filename = 'input'):
    self.filename = filename
    self.test('p1')
    self.day_16('p1')
    self.test('p2')
    self.day_16('p2')
    return

  def load_file(self):
    rules = {}
    with open(self.filename) as file:
      for line in file:
        if line == '\n': continue
        if line.startswith('your'):
          my_ticket = file.readline()
        elif line.startswith('nearby'):
          nearby_tickets = file.readlines()
        else:
          rule = line.split(':')[0].strip()
          values = line.split(':')[1].strip()
          rules[rule] = ((int(values.split('or')[0].split('-')[0]),
                         int(values.split('or')[0].split('-')[1])),
                        (int(values.split('or')[1].split('-')[0]),
                         int(values.split('or')[1].split('-')[1])))
    return rules, my_ticket, nearby_tickets

  def validate_tickets(self, rules, tickets, part):
    invalid_fields = []
    valid_tickets = []
    for ticket in tickets:
      ticket = [int(num) for num in ticket.split(',')]
      invalid_flag = 0
      for value in ticket:
        flag = 0
        for rule in rules:
          if (rules[rule][0][0] <= value <= rules[rule][0][1]) or (
              rules[rule][1][0] <= value <= rules[rule][1][1]):
            continue
          else:
            flag += 1
        if flag == len(rules):
          invalid_fields.append(value)
          invalid_flag = 1
      if invalid_flag == 0:
        valid_tickets.append(ticket)
    if part == 'p1':
      return sum(invalid_fields)
    elif part == 'p2':
      return valid_tickets

  def ordenate_fields(self, rules, tickets):
    fields = {rule:[] for rule in rules}
    fields_order = [[rule for rule in rules] for ind in range(len(rules))]
    for rule in rules:
      for ticket in tickets:
        for ind, value in enumerate(ticket):
           if (rules[rule][0][0] <= value <= rules[rule][0][1]) or (
              rules[rule][1][0] <= value <= rules[rule][1][1]):
            fields[rule].append(ind)
      for ind in range(len(rules)):
        if fields[rule].count(ind) != len(tickets):
          fields_order[ind].remove(rule)
    while True:
      for ind in range(len(fields_order)):
        if len(fields_order[ind]) == 1:
          rule = fields_order[ind][0]
          for field_list in fields_order[:ind]+fields_order[ind+1:]:
            if rule in field_list:
              field_list.remove(rule)
      if sum([1 if len(flist) == 1 else 0
              for flist in fields_order]) == len(fields_order):
        return [field[0] for field in fields_order]

  def departure(self, fields_order, ticket):
    ticket = [int(num) for num in ticket.split(',')]
    departure_val = 1
    for ind, field in enumerate(fields_order):
      if field.startswith('departure'):
        departure_val *= ticket[ind]
    return departure_val

  def test(self, part):
    if part == 'p1':
      rules = {'class': ((1, 3), (5, 7)), 'row': ((6, 11), (33, 44)),
               'seat': ((13, 40), (45, 50))}
      my_ticket = '7,1,14'
      nearby_tickets = ['7,3,47', '40,4,50', '55,2,20', '38,6,12']
      result = self.validate_tickets(rules, nearby_tickets, part)
      if result == 71:
        print('Test {} successful.'.format(part))
    elif part == 'p2':
      rules = {'class': ((0, 1), (4, 19)), 'row': ((0, 5), (8, 19)),
               'seat': ((0, 13), (16, 19))}
      my_ticket = '11,12,13'
      nearby_tickets = ['3,9,18', '15,1,5', '5,14,9', '55,2,20', '38,6,12']     
      valid_tickets = self.validate_tickets(rules, nearby_tickets, part)
      fields_order = self.ordenate_fields(rules, valid_tickets)
      if fields_order == ['row', 'class', 'seat']:
        print('Test {} successful.'.format(part))
      return 
    return

  def day_16(self, part):
    rules, my_ticket, nearby_tickets = self.load_file()
    result = self.validate_tickets(rules, nearby_tickets, part)
    if part == 'p2':
      fields_order = self.ordenate_fields(rules, result)
      result = self.departure(fields_order, my_ticket)
    print('Answer {}: {}:'.format(part, result))
    return

ticket_to_ride()

