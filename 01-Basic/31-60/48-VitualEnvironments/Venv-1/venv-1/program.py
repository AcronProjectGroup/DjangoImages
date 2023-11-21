# 💠 Virtual Environments commit=1


# in Terminal any where Operation System:
    # pip install virtualenv

# Output:
    # Defaulting to user installation because normal site-packages is not writeable
    # Collecting virtualenv
    #   Downloading virtualenv-20.24.6-py3-none-any.whl.metadata (4.5 kB)
    # Collecting distlib<1,>=0.3.7 (from virtualenv)
    #   Downloading distlib-0.3.7-py2.py3-none-any.whl.metadata (5.1 kB)
    # Collecting filelock<4,>=3.12.2 (from virtualenv)
    #   Downloading filelock-3.13.1-py3-none-any.whl.metadata (2.8 kB)
    # Collecting platformdirs<4,>=3.9.1 (from virtualenv)
    #   Downloading platformdirs-3.11.0-py3-none-any.whl.metadata (11 kB)
    # Downloading virtualenv-20.24.6-py3-none-any.whl (3.8 MB)
    #    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.8/3.8 MB 959.3 kB/s eta 0:00:00
    # Downloading distlib-0.3.7-py2.py3-none-any.whl (468 kB)
    #    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 468.9/468.9 kB 1.4 MB/s eta 0:00:00
    # Downloading filelock-3.13.1-py3-none-any.whl (11 kB)
    # Downloading platformdirs-3.11.0-py3-none-any.whl (17 kB)
    # Installing collected packages: distlib, platformdirs, filelock, virtualenv
    #   WARNING: The script virtualenv is installed in '/home/sina/.local/bin' which is not on PATH.
    #   Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
    # Successfully installed distlib-0.3.7 filelock-3.13.1 platformdirs-3.11.0 virtualenv-20.24.6

# And in Terminal again:
    # sudo apt install python3-virtualenv

# Output:
    # Reading package lists... Done
    # Building dependency tree... Done
    # Reading state information... Done
    # The following additional packages will be installed:
    #   python3-distlib python3-filelock python3-pip-whl python3-platformdirs python3-setuptools-whl python3-wheel-whl
    # Suggested packages:
    #   python2-pip-whl python2-setuptools-whl
    # The following NEW packages will be installed:
    #   python3-distlib python3-filelock python3-pip-whl python3-platformdirs python3-setuptools-whl python3-virtualenv python3-wheel-whl
    # 0 upgraded, 7 newly installed, 0 to remove and 20 not upgraded.
    # Need to get 2,878 kB of archives.
    # After this operation, 4,646 kB of additional disk space will be used.
    # Do you want to continue? [Y/n] y
    # Get:1 http://ae.archive.ubuntu.com/ubuntu jammy/universe amd64 python3-distlib all 0.3.4-1 [269 kB]
    # Get:2 http://ae.archive.ubuntu.com/ubuntu jammy/universe amd64 python3-filelock all 3.6.0-1 [8,788 B]
    # Get:3 http://ae.archive.ubuntu.com/ubuntu jammy-updates/universe amd64 python3-pip-whl all 22.0.2+dfsg-1ubuntu0.4 [1,680 kB]
    # Get:4 http://ae.archive.ubuntu.com/ubuntu jammy/universe amd64 python3-platformdirs all 2.5.1-1 [14.2 kB]                               
    # Get:5 http://ae.archive.ubuntu.com/ubuntu jammy-updates/universe amd64 python3-setuptools-whl all 59.6.0-1.2ubuntu0.22.04.1 [788 kB]    
    # Get:6 http://ae.archive.ubuntu.com/ubuntu jammy-updates/universe amd64 python3-wheel-whl all 0.37.1-2ubuntu0.22.04.1 [38.0 kB]          
    # Get:7 http://ae.archive.ubuntu.com/ubuntu jammy/universe amd64 python3-virtualenv all 20.13.0+ds-2 [80.3 kB]                            
    # Fetched 2,878 kB in 8s (351 kB/s)                                                                                                       
    # Selecting previously unselected package python3-distlib.
    # (Reading database ... 229140 files and directories currently installed.)
    # Preparing to unpack .../0-python3-distlib_0.3.4-1_all.deb ...
    # Unpacking python3-distlib (0.3.4-1) ...
    # Selecting previously unselected package python3-filelock.
    # Preparing to unpack .../1-python3-filelock_3.6.0-1_all.deb ...
    # Unpacking python3-filelock (3.6.0-1) ...
    # Selecting previously unselected package python3-pip-whl.
    # Preparing to unpack .../2-python3-pip-whl_22.0.2+dfsg-1ubuntu0.4_all.deb ...
    # Unpacking python3-pip-whl (22.0.2+dfsg-1ubuntu0.4) ...
    # Selecting previously unselected package python3-platformdirs.
    # Preparing to unpack .../3-python3-platformdirs_2.5.1-1_all.deb ...
    # Unpacking python3-platformdirs (2.5.1-1) ...
    # Selecting previously unselected package python3-setuptools-whl.
    # Preparing to unpack .../4-python3-setuptools-whl_59.6.0-1.2ubuntu0.22.04.1_all.deb ...
    # Unpacking python3-setuptools-whl (59.6.0-1.2ubuntu0.22.04.1) ...
    # Selecting previously unselected package python3-wheel-whl.
    # Preparing to unpack .../5-python3-wheel-whl_0.37.1-2ubuntu0.22.04.1_all.deb ...
    # Unpacking python3-wheel-whl (0.37.1-2ubuntu0.22.04.1) ...
    # Selecting previously unselected package python3-virtualenv.
    # Preparing to unpack .../6-python3-virtualenv_20.13.0+ds-2_all.deb ...
    # Unpacking python3-virtualenv (20.13.0+ds-2) ...
    # Setting up python3-setuptools-whl (59.6.0-1.2ubuntu0.22.04.1) ...
    # Setting up python3-filelock (3.6.0-1) ...
    # Setting up python3-pip-whl (22.0.2+dfsg-1ubuntu0.4) ...
    # Setting up python3-distlib (0.3.4-1) ...
    # Setting up python3-platformdirs (2.5.1-1) ...
    # Setting up python3-wheel-whl (0.37.1-2ubuntu0.22.04.1) ...
    # Setting up python3-virtualenv (20.13.0+ds-2) ...
    # Processing triggers for man-db (2.10.2-1) ...


# Create Virtual Environment:
# Command:
    # virtualenv venv 
    # source ./venv/bin/activate

# Output:
    # will add (venv) to first command Terminal:
        # (venv) sina@linux:~/01-Repo/6 DjangoWA/01-Basic/31-60/48-VitualEnvironments/Venv-1/venv-1$


# command:
#     pip list > VENVrequirements.txt
    
# Output:
#     Package    Version
#     ---------- -------
#     pip        23.3.1
#     setuptools 68.2.2
#     wheel      0.41.2



