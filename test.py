import numpy as np

def get_largest_remainder_allocation(percentages, total):
  split_values = [int(percentage * total) for percentage in percentages]
  target_values = [(percentage * total) for percentage in percentages]
  
  split_values = np.array(split_values)
  target_values = np.array(target_values)
  
  while sum(split_values) != total:
    diff = np.abs(split_values - target_values)
    largest_index = np.argmax(diff)
    if sum(split_values) < total:
      split_values[largest_index] += 1
    else:
      split_values[largest_index] -= 1
  return split_values




percentages = [0.022492625368731565, 0.018805309734513276, 0.029498525073746312, 0.032448377581120944, 0.054203539823008844, 0.029129793510324485, 0.023230088495575223, 0.012905604719764012, 0.03502949852507375, 0.03761061946902655, 0.03982300884955752, 0.03982300884955752, 0.038348082595870206, 0.025811209439528023, 0.021755162241887907, 0.034292035398230086, 0.0357669616519174, 0.03466076696165192, 0.0357669616519174, 0.0420353982300885, 0.03687315634218289, 0.02396755162241888, 0.031342182890855455, 0.0306047197640118, 0.032079646017699116, 0.0357669616519174, 0.04056047197640118, 0.028023598820058993, 0.02396755162241888, 0.04166666666666666, 0.03171091445427729]

total = 2465

allocated_values = get_largest_remainder_allocation(percentages, total)

print(allocated_values)  # Might print something like: [824, 1099, 823]
print(sum(allocated_values))  # Should be equal to 2746

