import subprocess

def run_foldx(foldx_executable, pdb_file, pdb_dir, mutant_file, output_dir):
    # 构建 FoldX 命令及其参数
    complete_command = f'"{foldx_executable}" --command=BuildModel --pdb="{pdb_file}" --pdb-dir="{pdb_dir}" --mutant-file="{mutant_file}" --output-dir="{output_dir}"'

    # 使用 subprocess.run() 执行命令，注意设置 shell=True
    result = subprocess.run(complete_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)

    # 返回命令执行结果
    return result.stdout, result.stderr

# 设置参数
foldx5_executable = r'D:\FoldX\foldx5Windows64\foldx5.exe'
pdb_location = r'D:\FoldX\foldx5Windows64\test'
pdb_file = 'BM.pdb'
mutant_file = r'D:\FoldX\foldx5Windows64\test\individual_list_1.txt'
output_location = r'D:\FoldX\foldx5Windows64\test\standard'

# 调用函数并获取结果
stdout, stderr = run_foldx(foldx5_executable, pdb_file, pdb_location, mutant_file, output_location)

# 打印结果
print("Standard Output:")
print(stdout)

print("Standard Error:")
print(stderr)
