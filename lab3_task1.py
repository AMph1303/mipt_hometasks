import os
import sys

def tenet(input_file_path: str, output_file_path: str):

    if os.path.isfile(input_file_path):
        if input_file_path == output_file_path:
            raise ValueError ('Files are same')
        
        with open(input_file_path) as input_file, open(output_file_path, 'w') as output_file:
            file_lines = [x.strip("\n") for x in input_file.readlines()]
            for i in range(len(file_lines)):
                line = list(file_lines[i])
                line.reverse()
                file_lines[i] = "".join(line)
            output_file.write("\n".join(file_lines))       

    else:
        raise ValueError('It is a directory')
    
        
if __name__ == '__main__':

    input_file_path = sys.argv[1]
    output_file_path = sys.argv[2]
    tenet(input_file_path, output_file_path)
