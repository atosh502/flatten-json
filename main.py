import json
from collections import deque

def joinKeys(keys):
  return '.'.join([str(k) for k in keys])

def flatten(obj):
  queue = deque()
  queue.append([])

  result = {}
  while queue:
    keys = queue.popleft()
    prefix = joinKeys(keys)

    currObj = obj
    for key in keys:
      currObj = currObj[key]

    if isinstance(currObj, dict):
      for k, v in currObj.items():
        if isinstance(v, dict):
          queue.append([*keys, k])
        elif isinstance(v, list):
          for idx in range(len(v)):
            queue.append([*keys, k, idx])
        else:
          if prefix:
            result[joinKeys([prefix, k])] = v
          else:
            result[k] = v
    elif isinstance(currObj, list):
      for idx in range(len(currObj)):
        queue.append([*keys, k, idx])
    else:
      result[prefix] = currObj
  return result

def main():
  with open('sample.json') as f:
    data = json.load(f)
    result = flatten(data)
    print(result)

if __name__ == "__main__":
  main()