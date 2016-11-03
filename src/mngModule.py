# -*- coding:utf-8 -*-
# 该命令用于typescript项目，用于模块
# 该命令目前只在python 3.4上测试
# 请将当前目录设添加到环境变量，这样才能够直接运行命令。
# 打开mngModule.bat, 修改当前mngModule.py的绝对路径
# 使用方法：
# 1. 打开cmd
# 2. 切换到typescript项目的目录
# 3. 运行mngModule -c create -m [模块名称，根据ts的习惯，建议写成aaa-bbb]
# 创建目录结构如下
# component
# model
# style
# template
# service
# [module-name].module.ts
# [module-name].routing.ts
import os
import getopt
import sys

componentName = "component"
modelName = "model"
styleName = "style"
serviceName = "service"
templateName = "template"

def main():
	options,args = getopt.getopt(sys.argv[1:], "ac:m:")
	print(options)
	cmdOpt = find(options, lambda o:o[0] == '-c')
	if cmdOpt:
		if cmdOpt[1] == 'create':
			dir = os.getcwd()
			moduleName = find(options, lambda o:o[0] == '-m')[1]
			createModule(dir, moduleName)
	else:
		print('没有设置c[ommand]参数,程序不能正常执行')

			


def find(arr, predicate):
	objs = list(filter(predicate, arr))
	if objs and len(objs) > 0:
		return objs[0]
	else:
		return None

def createModule(dir, moduleName):
	createComponentFolder(dir)
	createModelFolder(dir)
	createStyleFolder(dir)
	createTemplateFolder(dir)
	createServiceFolder(dir)
	createModuleFile(dir, moduleName)
	createRoutingFile(dir, moduleName)

def createComponentFolder(dir):
	os.makedirs(os.path.join(dir, componentName))

def createModelFolder(dir):
	os.makedirs(os.path.join(dir, modelName))

def createStyleFolder(dir):
	os.makedirs(os.path.join(dir, styleName))

def createTemplateFolder(dir):
	os.makedirs(os.path.join(dir, templateName))	

def createServiceFolder(dir):
	os.makedirs(os.path.join(dir, serviceName))	

def createModuleFile(dir, moduleName):
	with open(os.path.join(dir, ''.join([moduleName, '.module', '.ts'])), 'w') as file:
		pass

def createRoutingFile(dir, moduleName):
	with open(os.path.join(dir, ''.join([moduleName, '.routing', '.ts'])), 'w') as file:
		pass


if __name__ == '__main__':
	main()

