set PYTHON_HOME=c:\usr\Python31_2

set PATH=%PYTHON_HOME%;%PYTHON_HOME%\Lib\site-packages\PyQt4;%PYTHON_HOME%\Lib\site-packages\PyQt4\bin;c:\WINDOWS\system32;c:\WINDOWS;c:\WINDOWS\system32\wbem;

mkdir .\bin
python .\setup.py build > .\bin\build.out 2>&1

