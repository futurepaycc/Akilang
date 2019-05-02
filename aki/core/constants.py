PRODUCT = "Aki"
VERSION = "0.1.2019.05.01"
COPYRIGHT = "2019"

WELCOME = f"{PRODUCT} v.{VERSION}"

ABOUT = f"""{WELCOME}
© {COPYRIGHT} Serdar Yegulalp

Based on code created by:
- Frédéric Guérin (https://github.com/frederickjeanguerin/pykaleidoscope)
- Eli Bendersky (https://github.com/eliben/pykaleidoscope)"""


def defaults():
    return {
        "paths": {
            "source_dir": "examples",
            "output_dir": "output",
            "dump_dir": ".",
            "nt_compiler": "C:\\Program Files (x86)\\Microsoft Visual Studio\\2017\\Community\\VC\\Auxiliary\\Build\\vcvarsall.bat",
        },
        "settings": {
            "write_main_to_file": {
                'Dumps loaded module LLVM IR to "{settings.paths.output_dir}" on load.',
                True,
            },
            "write_repl_to_file": {
                'Dumps REPL LLVM IR to "{setting.paths.output_dir}" on load.',
                True,
            },
            "compile_on-load": {"Compile immediately when a file is loaded.", True},
        },
    }
