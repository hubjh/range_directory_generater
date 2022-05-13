import os
import argparse

parser = argparse.ArgumentParser(description=
'''
--path : Enter the path to the directory.
    
--count : Enter the number of subdirectories.           
''',
    formatter_class=argparse.RawTextHelpFormatter
)

parser.add_argument('--path', required=True, help=''':  Please enter a folder path.     < --path=/foo/bar/test >''')
    
parser.add_argument('--count', required=False, type=int, default=1, help=''':  Please enter the number of folders to create.    < --count=100 >''')
args = parser.parse_args()

os.makedirs(args.path, exist_ok=True)         


for i in range(1 ,args.count+1):
    os.makedirs(f'{args.path}/{i}', exist_ok=True)


        