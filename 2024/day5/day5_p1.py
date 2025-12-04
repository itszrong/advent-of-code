pages_array = []
rules_array = []
for page in pages_str.split('\n'):
    page = page.split(',')
    pages_array.append(page)
for rules in rules_str.split('\n'):
    rules_array.append(rules)

import regex

def extract_rules(rules_str):
    pattern = r"(\d+)\|(\d+)"
    return regex.findall(pattern, rules_str)

rules_tuple_list = extract_rules(rules_str)

page0 = pages_array[0]
correct_pages = []
incorrect_pages = []
for page in pages_array:
  correct_page_bool = True
  for rule in rules_tuple_list:
      if rule[0] in page and rule[1] in page:
          if page.index(rule[0]) < page.index(rule[1]):
              pass
          else:
            correct_page_bool = False
            break
  if correct_page_bool == True:
    correct_pages.append(page)
  elif correct_page_bool == False:
    incorrect_pages.append(page)

sum = 0
for page in correct_pages:
    sum += int(page[int(len(page)/2)])
sum

graph = {}
for rule in rules_tuple_list:
    antecedent, consequent = rule
    if antecedent not in graph:
        graph[antecedent] = []
    graph[antecedent].append(consequent)


graph = {}
for rule in rules_tuple_list:
    antecedent, consequent = rule
    if antecedent not in graph:
        graph[antecedent] = []
    graph[antecedent].append(consequent)

print(graph)

values = set()
for value in graph.values():
    for number in value:
        values.add(number)
print(values)

import copy

def get_ordered_list(graph, page):
      graph_deepcopy = copy.deepcopy(graph)
      ordered_list = []
      key_to_pop = []
      page_set = set(page)

      graph_filtered = {}
      for key in graph_deepcopy.keys():
          if key in page_set:
              neighbours = [neighbour for neighbour in graph_deepcopy[key] if neighbour in page_set]
              if neighbours:
                  graph_filtered[key] = neighbours

      graph_copy = copy.deepcopy(graph_filtered)

      while graph_copy.keys():
          values = set()
          for value in graph_copy.values():
              for number in value:
                  values.add(number)

          for key in graph_copy.keys():
              if key not in values:
                ordered_list.append(key)
          if ordered_list:
            graph_copy.pop(ordered_list[-1])

      for i in ordered_list:
        if i in values:
          values.remove(i)
      ordered_list.extend(values)
      return ordered_list

fixed_pages = []
for page in incorrect_pages:
    ordered_list = get_ordered_list(graph, page)
    page.sort(key = lambda x: ordered_list.index(x))
    fixed_pages.append(page)
fixed_pages

fixed_pages = []
for page in incorrect_pages:
    page.sort(key = lambda x: ordered_list.index(x))
    fixed_pages.append(page)
fixed_pages

sum = 0
for page in fixed_pages:
    sum += int(page[int(len(page)/2)])
sum

import copy

def get_ordered_list(graph, page):
    # Filter the graph to only include nodes present in the page
    graph_filtered = {}
    page_set = set(page)

    for key in graph.keys():
        if key in page_set:
            # Only include neighbors that are also in the page
            neighbors = [neighbor for neighbor in graph[key] if neighbor in page_set]
            if neighbors:  # Only add if there are valid neighbors
                graph_filtered[key] = neighbors

    # Now perform topological sort on the filtered graph
    ordered_list = []
    graph_copy = copy.deepcopy(graph_filtered)

    while graph_copy:
        # Find all values (nodes that have incoming edges)
        values = set()
        for neighbors in graph_copy.values():
            for neighbor in neighbors:
                values.add(neighbor)

        # Find nodes with no incoming edges
        nodes_with_no_incoming = []
        for key in graph_copy.keys():
            if key not in values:
                nodes_with_no_incoming.append(key)

        # If no nodes with no incoming edges, we have a cycle in the subgraph
        if not nodes_with_no_incoming:
            # Just add remaining nodes in any order
            ordered_list.extend(list(graph_copy.keys()))
            break

        # Add one node with no incoming edges and remove it from graph
        node_to_remove = nodes_with_no_incoming[0]
        ordered_list.append(node_to_remove)
        graph_copy.pop(node_to_remove)

    # Add any remaining nodes from the page that weren't in the graph
    for node in page:
        if node not in ordered_list:
            ordered_list.append(node)

    return ordered_list

# Test with the incorrect pages
fixed_pages = []
for page in incorrect_pages:
    print(f"Original page: {page}")
    ordered_list = get_ordered_list(graph, page)
    print(f"Ordered list: {ordered_list}")
    page.sort(key=lambda x: ordered_list.index(x))
    print(f"Fixed page: {page}")
    print()
    fixed_pages.append(page)

print(f"Number of fixed pages: {len(fixed_pages)}")


# Calculate the sum of middle elements from fixed pages
sum_middle = 0
for page in fixed_pages:
    middle_index = len(page) // 2
    middle_value = int(page[middle_index])
    sum_middle += middle_value
    print(f"Page: {page}, Middle element: {middle_value}")

print(f"\nSum of middle elements from fixed pages: {sum_middle}")

