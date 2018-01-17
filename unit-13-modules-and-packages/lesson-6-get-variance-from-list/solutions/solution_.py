# Import the library here (must be python 3.4+)!
try:
  from statistics import variance
except ImportError:
  def variance(a_list):
    mean = sum(a_list) / float(len(a_list))
    return sum([(x - mean) ** 2 for x in a_list]) / float((len(a_list) - 1))

def get_variance_from_list(a_list):
    return variance(a_list)