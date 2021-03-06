#!/usr/bin/python
# -*- coding:utf-8 -*-

# ---------------------------
# Author: deangao
# Copyright: 2016 deangao
# Email: gaowenhui2012@gmail.com
# Version: v1.0.0
# Created: 2016/3/10
# ---------------------------


import os
import sys
import py2exe
from distutils.core import setup


sys.path.append(os.getcwd() + '\\src')

# py2exe 选项
py2exe_options = {
	"includes": ['wxbiopyutils'],
	"dll_excludes": ["w9xpopen.exe", "numpy-atlas.dll"],
	"compressed": 1,
	"optimize": 2,
	"ascii": 0,
	"bundle_files": 1,
}

# 安装生产exe选项
setup(
	name='Bioinformatics python tools on windows platform',
	description='Bioinformatics python tools on windows platform',
	version='1.0.0',
	console=[{'script': './src/extract_seq.py', 'icon_resources': [(0, 'images/icon.ico')]},
			 {'script': './src/download_from_genbank.py', 'icon_resources': [(0, 'images/icon.ico')]},
			 {'script': './src/download_from_swissprot.py', 'icon_resources': [(0, 'images/icon.ico')]},
			 {'script': './src/draw_chromosome.py', 'icon_resources': [(0, 'image/icon.ico')]}],
	zipfile=None,
	options={'py2exe': py2exe_options},
	author='deangao-wwww.iwhgao.com',
	author_email='gaowenhui2012@gmail.com'
)
