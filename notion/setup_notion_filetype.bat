@echo off
REM Associate .xyz files with mpNotion file type
assoc .xyz=mpNotion

REM Create the mpNotion file type (no open command specified)
ftype mpNotion="<path_to_python>\python.exe" "<path_do_dagda_scripts>\notion\opening_notion.py" "--is_file" "%1"

REM Set the DefaultIcon for mpNotion using environment variable and REG_EXPAND_SZ
reg add "HKCR\mpNotion\DefaultIcon" /ve /t REG_EXPAND_SZ /d "C:\Users\jeffw\AppData\Local\Programs\Notion\Notion.exe,-1" /f

echo Done.