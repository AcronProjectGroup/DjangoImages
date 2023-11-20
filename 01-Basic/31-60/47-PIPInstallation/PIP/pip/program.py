# most Python packages is here 
# https://pypi.org/

# For Update pip
    #  pip install -U pip

# Output after updating:
    # Defaulting to user installation because normal site-packages is not writeable
    # Requirement already satisfied: pip in /usr/lib/python3/dist-packages (22.0.2)
    # Collecting pip
    #   Downloading pip-23.3.1-py3-none-any.whl (2.1 MB)
    #      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.1/2.1 MB 2.0 MB/s eta 0:00:00
    # Installing collected packages: pip
    #   WARNING: The scripts pip, pip3, pip3.10 and pip3.11 are installed in '/home/sina/.local/bin' which is not on PATH.
    #   Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
    # Successfully installed pip-23.3.1

from colorama import just_fix_windows_console
from termcolor import colored

# use Colorama to make Termcolor work on Windows too
just_fix_windows_console()

# then use Termcolor for all colored text output
print(colored('Hello, World!', 'green', 'on_red'))