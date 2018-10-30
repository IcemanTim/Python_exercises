

some_list = { 'value': 1, 'next': { 'value': 2, 'next': { 'value': 3, 'next': { 'value': 4, 'next': None}}}}

def get_need_list(d1, d2):
  # необходимая проверка в связи с тем, что NoneType объекты не имеют метода .items()
  if d1 is not None:
    d = {}
    d[list(d1.items())[0][0]] = list(d1.items())[0][1]
    # необходимая проверка в связи с тем, что NoneType объекты не имеют метода .items()
    if d2 is None:
      d[list(d1.items())[1][0]] = None
      return get_need_list(list(d1.items())[1][1],d)
    else:
      d[list(d1.items())[1][0]] = d2
      d2 = d2.copy()
      d2.update(d)
      return get_need_list(list(d1.items())[1][1],d2)
  else:
    return d2;

def reverse_print(lst):
  need_list = get_need_list(lst, None)
  print(need_list)


reverse_print(some_list)




