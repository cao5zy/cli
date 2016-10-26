# -*- coding:utf-8 -*-
# 该命令用于打印当前目录下的目录结构
# 该命令目前只在python 3.4上测试
# 请将当前目录设添加到环境变量，这样才能够直接运行命令。
# 打开showdir.bat, 修改当前showdir.py的绝对路径
# 使用方法：
# 1. 打开cmd
# 2. 切换到任意需要查看的目录
# 3. 运行showdir.bat

import sys
import os
import re

outputFileName = "showdir.output.txt"
excludes = ['_ReSharper.ExstreamExtraction', 'Web References', 'Service References', 'bin', 'Release', 'Debug', 'TodoCache', 'BuildScriptCache', 'NamedArguments', 'WordIndex',
'.svn', 'packages', 'obj', 'TestResults', 'bootstrap']
newNameList = []
def main():
	path = os.path.join(os.getcwd(), outputFileName);
	rootPath = os.getcwd()
	with open(path, 'w') as outfile:
		for root, dirs, files in os.walk(rootPath):
			if getRootName(root) in excludes:
				continue

			#输出文件夹名称
			writeline(outfile, getIndentNumber(rootPath, root), getRootName(root))

			for f in files:
				writeline(outfile, getIndentNumber(rootPath, root) + 1, f)

		
def writeline(file, levelNum, content):
	indent = (levelNum if levelNum > 0 else 1)  * (' ' * 4);
	file.write('%s%s\n'%(indent, content))

def getRootName(root):
	return root[root.rfind('\\') + 1:]

def getIndentNumber(rootPath, path):
	leftPath = path.replace(rootPath, '')

	count = len(re.compile(r'\\').findall(leftPath))
	return count if count > 0 else 1

def generateNode(name):
	conv = [' ', '-', '.']
	spl=''
	for val in [n for n in conv if n in name]:
		spl = val

	if spl == '':
		return name
	else:
		newName = name.replace(spl, '_')
		if newName in newNameList:
			return newName
		else:
			newNameList.append(newName)## tricky point. need to be refactored if there is futher needs
			print('%s[label="%s"]' % (newName, name))
			return newName


def hasExcludeNames(root, excludes):
	names = root.split('\\')
	for val in [n for n in names if n in excludes]:
		return True

	return False

if __name__ == '__main__':
	main()
