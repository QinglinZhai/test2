## 在pymol中repair PDB的方法：
# load C:\Users\YourName\Documents\Proteins\myprotein.pdb
# remove resn HOH
# save /path/to/save/modified_file.pdb

## 通过这个命令可以将pdb文件转换成cif文件：
# save /path/to/save/modified_file.cif, format=cif

import subprocess
def repair_PDB(pdb,pdb_dictionary,output_dir):
    complete_command = f'"{foldx5_executable}" --command=RepairPDB --pdb={pdb} --pdb-dir={pdb_dictionary}  --output-dir={output_dir}'
    result = subprocess.run(complete_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
    return result

foldx5_executable = r'D:\FoldX\foldx5Windows64\foldx5.exe'
pdb = input("please enter the pdb fullname:").strip()
pdb_dictionary = input("please enter the pdb dictionary:").strip()
output_dir = input("Please enter the output dictionary:").strip()
# pdb = 'cleaned_BM.pdb'
# pdb_dictionary = r'D:\FoldX\foldx5Windows64\test'
# output_dir = r'D:\FoldX\foldx5Windows64\test\standard'

repaired_PDB = repair_PDB(pdb,pdb_dictionary,output_dir)

print("Standard Output:")
print(repaired_PDB.stdout)

print("Standard Error:")
print(repaired_PDB.stderr)