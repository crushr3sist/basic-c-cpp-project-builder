very simple build system

aggregates source files in src

and looks for a lib folder on the same or nested level of the src folder

supports both cpp and c file compilation. 

creates a build folder and saves the executable. 

```
Directory structure:
/
├── build.py
├── src/
│   ├── file1.cpp
│   ├── file2.cpp
│   ├── file1.c
│   ├── file2.c
│   ├── file1.h
│   └── file2.h
└── build/
    └── (generated files will be placed here)
```