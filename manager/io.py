import sys

def write_list_to_file(input_list,output_file):
  with open(output_file,"w") as f:
    for line in input_list:
      f.write(line)
      