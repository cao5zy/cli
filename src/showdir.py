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

outputFileName = "showdir.output.txt"
excludes = ['_ReSharper.ExstreamExtraction', 'Web References', 'Service References', 'bin', 'Release', 'Debug', 'TodoCache', 'BuildScriptCache', 'NamedArguments', 'WordIndex',
'.svn', 'packages', 'obj', 'TestResults', 'bootstrap']
newNameList = []
def main():
	path = os.path.join(os.getcwd(), outputFileName);
	with open(path, 'w') as outfile:
		for root, dirs, files in os.walk(os.getcwd()):
			for d in dirs:
				if (getRootName(root) in excludes) or (d in excludes) or hasExcludeNames(root, excludes):
					continue
				outfile.write('%s -> %s\n' % (generateNode(getRootName(root)), generateNode(d)))
		



def getRootName(root):
	return root[root.rfind('\\') + 1:]

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
