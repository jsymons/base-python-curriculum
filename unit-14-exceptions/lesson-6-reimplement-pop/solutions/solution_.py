def pop(dictionary, key, default_value=None):
  try:
    val = d[key]
    del d[key]
    return val
  except KeyError as e:
    if default_value:
        return default_value
    raise e