import re
class luggage_processing:
  '''Class for properly sorting and processing colorful bags.'''
  def __init__(self, filename='input'):
    self.filename = filename
    self.test('p1')
    self.day_07('p1')
    self.test('p2')
    self.day_07('p2')
    return

  def load_file(self):
    with open(self.filename) as file:
      data = file.readlines()
      return data

  def bags_inna_bag(self, data):
    bags_contained_in={} # bags in which it is contained
    bags_contains_into={} # bags contained within it
    #pattern = re.compile(' [0-9]+ [a-z ]+ bag[s.]*')
    pat_num = re.compile('[0-9]+')
    pat_letters = re.compile('[a-z]+')
    for line in data:
      main_bag = line.split('contain')[0].replace('bags', '').strip().lower()
      contained_bags = line.split('contain')[1].split(',')
      bags_contains_into[main_bag] = {}
      MainBag = bags_contains_into[main_bag]
      for bag in contained_bags:
        bag = bag.strip().lower()
        if bag == 'no other bags.':
          continue
        else:
          bagname = ' '.join([x for x in pat_letters.findall(bag)
                              if x not in ('bag', 'bags')])
          bag_qte = int(pat_num.findall(bag)[0])
          MainBag[bagname] = bag_qte
          if bagname not in bags_contained_in:
            bags_contained_in[bagname] = [main_bag]
          else:
            bags_contained_in[bagname].append(main_bag)
    return bags_contained_in, bags_contains_into

  def summon_count_bag_colors(self, bags_contained_in, bagname):
    self.bag_list = []
    self.bag_list = self.count_bag_colors(bags_contained_in, bagname)
    return self.bag_list

  def count_bag_colors(self, bags_contained_in, bagname):
    for bag in bags_contained_in[bagname]:
      #print('Bag_ini =', bag)
      if bag not in self.bag_list:
        #print('Bag not in selfbaglist =', bag)
        self.bag_list.append(bag)
        #print(bag)
        if bag in bags_contained_in:
          #print('Bag in bagscontainedin =', bag)
          self.count_bag_colors(bags_contained_in, bag)
        #else:
          #print(bag)
          #self.bag_list.append(bag)
    #print('Return -- ', self.bag_list)
    return self.bag_list

  def summon_count_bags_contained(self, bags_contains_into, bagname):
    self.bags_contained = -1
    self.bags_contained = self.count_bags_contained(bags_contains_into,
                                                    bagname, 1)
    return self.bags_contained

  def count_bags_contained(self, bags_contains_into, bagname, qte):
    self.bags_contained += qte
    for bag, qte_in in bags_contains_into[bagname].items():
      qte_in *= qte
      self.count_bags_contained(bags_contains_into, bag, qte_in)
    return self.bags_contained
  
  def test(self, part):
    sample = '''light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.'''
    sample = sample.split('\n')
    sample_into, sample_contain = self.bags_inna_bag(sample)
    if part == 'p1':
      sg_contained = self.summon_count_bag_colors(sample_into, 'shiny gold')
      #print(sg_contained)
      if len(sg_contained) == 4:
        print('Test {} successful.'.format(part))
        return
    if part == 'p2':
      sg_contains = self.summon_count_bags_contained(sample_contain,
                                                     'shiny gold')
      if self.bags_contained == 32:
        print('Test {} successful.'.format(part))

  def day_07(self, part):
    bags_into, bags_contain = self.bags_inna_bag(self.load_file())
    if part == 'p1':
      sg_contained = self.summon_count_bag_colors(bags_into, 'shiny gold')
      print('Answer {}: {}'.format(part, len(sg_contained)))
      return sg_contained
    if part == 'p2':
      sg_contains = self.summon_count_bags_contained(bags_contain, 'shiny gold')
      print('Answer {}: {}'.format(part, sg_contains))
      return sg_contains
    