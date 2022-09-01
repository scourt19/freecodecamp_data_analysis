import numpy as np

def calculate(list):
  if (len(list) != 9):
    raise ValueError("List must contain nine numbers.")
  np_list = np.array(list)
  matrix = np_list.reshape(3,3)
  #Mean
  mean_1 = np.mean(matrix, axis=0).tolist()
  mean_2 = np.mean(matrix, axis=1).tolist()
  arr_mean = np.mean(np_list)
  #Variance
  var_1 = np.var(matrix, axis=0).tolist()
  var_2 = np.var(matrix, axis=1).tolist()
  arr_var = np.var(np_list)
  #Standard deviation
  std_1 = np.std(matrix, axis=0).tolist()
  std_2 = np.std(matrix, axis=1).tolist()
  arr_std = np.std(np_list)
  #Maximum
  max_1 = np.max(matrix, axis=0).tolist()
  max_2 = np.max(matrix, axis=1).tolist()
  arr_max = np.max(np_list)
  #Minimum
  min_1 = np.min(matrix, axis=0).tolist()
  min_2 = np.min(matrix, axis=1).tolist()
  arr_min = np.min(np_list)
  #Sumation
  sum_1 = np.sum(matrix, axis=0).tolist()
  sum_2 = np.sum(matrix, axis=1).tolist()
  arr_sum = np.sum(np_list)
  #Values given in a dictionary
  calculations = {
    'mean': [mean_1, mean_2, arr_mean],
    'variance': [var_1, var_2, arr_var],
    'standard deviation': [std_1, std_2, arr_std],
    'max': [max_1, max_2, arr_max],
    'min': [min_1, min_2, arr_min],
    'sum': [sum_1, sum_2, arr_sum]
  }
  return calculations