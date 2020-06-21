import re
import os
def get_last_epoch(ckpt_path):
  paths = [d.split('.')[0] for d in os.listdir(ckpt_path)]
  last_epoch = max([int(re.findall("[0-9]+",p)[0])  for p in paths])
  return last_epoch