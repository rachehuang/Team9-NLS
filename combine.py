import os
import json
import pandas as pd
import datetime

def combine(input_files):
    print('Combining as of ',datetime.datetime.now().time())
    return pd.concat(
      [
        pd.read_json(input_file)['articles'] for input_file in input_files
        ], 
        ignore_index=True)


if __name__ == '__main__':
  import argparse

  parser = argparse.ArgumentParser()
  parser.add_argument('input', help='file directory for data files (JSON)')
  parser.add_argument('output', help='combined file (CSV)')
  args = parser.parse_args()

  input_files = [
    os.path.join(args.input, f)
    for f in sorted(os.listdir(args.input))
  ]

  combined = combine(input_files)
  combined = pd.concat([x for x in combined.apply(lambda x: pd.DataFrame.from_dict(x))], ignore_index=True)
  combined.to_csv(args.output, index=True)
