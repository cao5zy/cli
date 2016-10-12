# -*- coding:utf-8 -*-
# 该命令用于typescript项目，用于创建目录下的index.ts文件
# 该命令目前只在python 3.4上测试
# 请将当前目录设添加到环境变量，这样才能够直接运行命令。
# 打开createIndexTs.bat, 修改当前createIndexTs.py的绝对路径
# 使用方法：
# 1. 打开cmd
# 2. 切换到typescript项目的目录
# 3. 运行py_createindex.bat
import os

def main():
	dir = os.getcwd()

	indexTsFileName = os.path.join(dir, 'index.ts')

	with open(indexTsFileName, 'w') as indexTsFile:
		for fileName in getTsFiles(dir):
			indexTsFile.write('''import * from './%s';\r\n '''% fileName)

def getTsFiles(dir):
	return ["heeloo.ts"];

if __name__ == '__main__':
	main()