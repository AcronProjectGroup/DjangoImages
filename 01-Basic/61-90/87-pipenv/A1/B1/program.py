# before
# python -m venv venv


# now
# pipenv 

# Instalation:
    # pip install pipenv
# Or
    # sudo apt install pipenv
    

# activation:
    # pipenv shell

# Deactivate:
    # exit


# Unistall Djnago Command:
    # pipenv uninstall django

# To activate this project's virtualenv, run:
    # pipenv shell

# Alternatively, run a command inside the virtualenv with:
    # pipenv run


# Create requirements.txt file with pipenv >> command:
    # pipenv requirements > requirements.txt


# Install on the pipenv from requirements.txt file:
    # pipenv install -r requirements.txt


# Change python version for pipenv:
# Attention! ->> python should installed on the OS(Operation System)
    
    # example change to 3.6 version:
        # pipenv --python 3.6

    # example change to 3.10 version:
        # pipenv --python 3.10


# Find Data pipenv and location:
    # pipenv --venv

# Delete pipenv:
    # pipenv --rm


#  What is it is this pipenv? 
#  Like getting Logs
#  Command:
    # pipenv graph


# Is there a security problem?
# Command:
    # pipenv check


# if don't have 
# Create Pipfile.lock 
# Command:
    # pipenv lock