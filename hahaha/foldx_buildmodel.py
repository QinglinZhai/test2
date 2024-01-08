import subprocess
import os
def create_config_file(config_dictionary,config_file_name,pdb,pdb_dir,mutant_file,output_dir):
    config_full_file = os.path.join(config_dictionary,config_file_name)
    #打开配置文件，进行写入
    with open(config_full_file,mode="w") as config_file:
        config_file.write('command=BuildModel\n')
        config_file.write(f'pdb={pdb}\n')
        config_file.write(f'pdb-dir={pdb_dir}\n')
        config_file.write(f'mutant-file={mutant_file}\n')
        config_file.write(f'output-dir={output_dir}\n')

    return config_full_file
def run_FoldX5(config_dictionary,config_file_name,foldx5_executable):
    config_full_file = os.path.join(config_dictionary, config_file_name)
    complete_command = f'"{foldx5_executable}" --config={config_full_file}'
    result = subprocess.run(complete_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
    return result

#设置参数
foldx5_executable = r'D:\FoldX\foldx5Windows64\foldx5.exe'
config_dictionary = input("Please enter the config_dictionary:").strip()
config_file_name = input("Please enter the config_file_name:").strip()
pdb = input("please enter the pdb fullname:").strip()
pdb_dir = input("Please enter the pdb dictionary:").strip()
mutant_file = input("Please enter the mutant_file dictionary:").strip()
output_dir = input("Please enter the output dictionary:").strip()

# # 设置参数
# config_dictionary = r'D:\FoldX\foldx5Windows64\test\standard'
# config_file_name = 'a.cfg'
# pdb = 'BM.pdb'
# pdb_dir = r'D:\FoldX\foldx5Windows64\test'
# mutant_file = r'D:\FoldX\foldx5Windows64\test\individual_list_1.txt'
# output_dir = r'D:\FoldX\foldx5Windows64\test\standard'
# foldx5_executable = r'D:\FoldX\foldx5Windows64\foldx5.exe'

# 调用创建配置文件函数
created_config_file=create_config_file(config_dictionary,config_file_name,pdb,pdb_dir,mutant_file,output_dir)
result = run_FoldX5(config_dictionary,config_file_name,foldx5_executable)

print("Standard Output:")
print(result.stdout)

print("Standard Error:")
print(result.stderr)