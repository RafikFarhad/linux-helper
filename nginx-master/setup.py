from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(
    packages = [],
    excludes = [],
    includes = [],
    include_files = ["conf.txt"]
)

import sys
base = 'Win32GUI' if sys.platform=='win32' else None

executables = [
    Executable('master.py', base=base, targetName = 'nginx-master')
]

setup(name='nginx-master',
      version = '1.0',
      description = 'A simple GUI for managing nginx and create subdomain for laravel like projects for developper.',
      options = dict(build_exe = buildOptions),
      executables = executables)
