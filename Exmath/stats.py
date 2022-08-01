from math import *
from .math_func import *
from prettytable import *
import numpy as np
import matplotlib.pyplot as plt

#steps added, working
def meanx(data, steps=False):
  if(steps != False and steps != True):
    return "error"
  sum = 0
  num = len(data)
  for x in data:
    sum += x
  mean = sum / num
  if(steps == False):
    return mean
  if(steps == True):
    steps_arr = []
    steps_arr.append("mean = sum of data / number of data")
    steps_arr.append(f"mean = {sum} / {num}")
    steps_arr.append(f"mean = {mean}")
    return (mean,steps_arr)

#steps added, working
def medianx(data, steps=False):
  if(steps != False and steps != True):
    return "error"
  sorted_data = data
  sorted_data.sort()
  num = len(sorted_data)
  value = (num + 1)/2 - 1
  if(type(value) == int):
    median = sorted_data[value]
  elif(type(value) == float):
    median = (sorted_data[floor(value)] + sorted_data[ceil(value)])/2
  if(steps == False):
    return median
  elif(steps == True):
    steps_arr = []
    steps_arr.append("target value = (number of data + 1)/2")
    steps_arr.append(f"target value = ({num} + 1)/2")
    steps_arr.append(f"target value = {value + 1}")
    if(isInteger(value) == True):
      steps_arr.append(f"Because there is an odd number of data, the median is {median}")
    elif(isInteger(value) == False):
      steps_arr.append("Because there is an even number of data, the median is the average two data closest to the target value.")
      steps_arr.append(f"median = ({sorted_data[floor(value)]} + {sorted_data[ceil(value)]}) / 2")
      steps_arr.append(f"median = {median}")
    return (median,steps_arr)

#steps added, working
def modex(data):
  freq = {}
  for x in data:
    if x in freq:
      freq[x] += 1
    else:
      freq[x] = 1
  freq_arr = []
  for x in freq:
    freq_arr.append(freq[x])
  freq_arr.sort(reverse=True)
  mode = [i for i,j in freq.items() if j == freq_arr[0]]
  return mode

def freqTableDx(data, cumulative=False, table=False):
  freq = {}
  for x in data:
    if(x in freq):
      freq[x] += 1
    else:
      freq[x] = 1
  sorted_freq = sorted(freq.items())
  if(cumulative == True):
    cumu = []
    for x in range(0,len(sorted_freq)):
      if(x == 0):
        cumu.append(sorted_freq[x])
      else:
        cumu.append((sorted_freq[x][0], cumu[x-1][1] + sorted_freq[x][1]))
    if(table != True):
      return cumu

  if(table == True):
    freqtable = PrettyTable(["Data", "Frequency"])
    for x in sorted_freq:
      freqtable.add_row(x)
    if(cumulative == True):
      cumutable = PrettyTable(["Data", "Cumulative Frequency"])
      for x in cumu:
        cumutable.add_row(x)
      return cumutable, cumu
    return freqtable, sorted_freq

  return sorted_freq

def freqGraphDx(data, cumulative=False, color="maroon", width=0.4): 
  data_freq = freqTableDx(data, cumulative=cumulative)
  
  xaxis = []
  yaxis = []
  
  for x in data_freq:
    xaxis.append(x[0])
    yaxis.append(x[1])
  plt.bar(xaxis, yaxis, color=color,
        width = width)
  plt.show()