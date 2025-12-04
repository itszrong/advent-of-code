print(reports)

reports_lists = []
for line in reports.split("\n"):
    report = []
    for number in line.split(" "):
      report.append(number)
    reports_lists.append(report)
print(reports_lists)

def bigger_or_smaller(i, j):
  if i > j:
    return 1
  elif i < j:
    return -1
  else:
    return 0

def distance_check(i, j):
  return abs(i-j)

def check_report(reports_lists):
  safe_counter = 0
  for report in reports_lists:
    check1 = False
    check2 = False
    check1_array = []
    check2_array = []
    for i in range(len(report)-1):
      check1_array.append(bigger_or_smaller(int(report[i]), int(report[i+1])))
    if abs(sum(check1_array)) == len(check1_array):
      check1 = True
    else:
      pass
    if check1 == True:
      for i in range(len(report)-1):
        check2_array.append(distance_check(int(report[i]), int(report[i+1])))
    check2_array_bool = []
    for i in check2_array:
      if i > 0 and i < 4:
        check2_array_bool.append(True)
      else:
        check2_array_bool.append(False)
    check2 = all(check2_array_bool)
    if check1 == True and check2 == True:
      safe_counter += 1
  return safe_counter

safe_counter = check_report(reports_lists)
print(safe_counter)


from copy import deepcopy
safe_counter = 0
for report in reports_lists:
  report_check_array = []
  report_int_list = []

  #convert to int
  for i in report:
    report_int_list.append(int(i))

  for i in range(len(report_int_list)):
    # print(report_int_list)
    report_to_check = deepcopy(report_int_list)
    report_to_check.pop(i)
    report_check_array.append(check_report([report_to_check]))
  if 1 in report_check_array:
    safe_counter += 1
print(safe_counter)
