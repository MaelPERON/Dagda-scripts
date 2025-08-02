# Dagda's Scripts

A repository of user scripts and browser tools — practical, modular, and built to simplify or automate everyday tasks. 

---

![Static Badge](https://img.shields.io/badge/Made%20with-%E2%9D%A4%EF%B8%8F-red?style=for-the-badge)
<table class="no-border"><tr><td><img src="https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white"></td><td><img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=flat&logo=javascript&logoColor=black"></td><td><img src="https://img.shields.io/badge/Node.js-339933?style=flat&logo=node.js&logoColor=white"></td></tr></table>

---

## Usage

This repository aims at stocking all the script files.
You can either add them as tampermonkey scripts, or compile them as python scripts.

### Installation

1. First -- if not done -- install [git](https://git-scm.com/downloads) on your computer
2. Create a parent directory, where you'll store this one. Open it in a command window.
3. Then clone this github repository, using
```
git clone https://github.com/MaelPERON/Dagda-scripts.git
```

Now the repository is cloned. You have access to all its content.

### TamperpMonkey Scripts

TODO ...

### Python Scripts

> [!NOTE]
> In the end, you'll be able to launch any script anywhere!

1. Make sure [python 3.12.X](https://www.python.org/downloads/release/python-3132/) is installed.
2. Open the repository inside a command window
3. Compile all the available scripts using this command
```
python .\compile_all.py
```
> [!TIP]
> Use `python .\compile_all.py -h` to see the available argument.\
> *This is useful when compiling only a selection of scripts (e.g. notion)*
4. Once the scripts are compiled, you should find them inside the `compiled` folder
```
cd .\compiled
```
5. Associate .pyc files to the python .exe interpreter
	1. On windows :
		1. Find the exe (usually located at `%localappdata%\Programs\Python\Python312`)
		2. Right click any .pyc file
		3. Open with > Choose another application
		4. More Applications, then Browse for an application
		5. Select python.exe from the interprether folder path (see 5.i.a.)
		6. Check "Always use when clicking .pyc" files
6. To register those compilled python files, add the compiled folder path into %PATH% environment variable.\
*On windows, you can look at this [stackoverflow answer](https://stackoverflow.com/a/44272417).*
7. Now that it's done! Test it by opening a random command window and typing
```
print_scripts.pyc
```
*You should see a list of all the scripts you've compiled so far*

> [!TIP]
> For each script, if its available, add `-h` or `--help` to show the help message and exit said script.\
> *(e.g; `print_scripts.pyc -h`)*

8. And, voilà! Enjoy!