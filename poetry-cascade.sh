#!/bin/bash

# A bash script to cascade package updates between packages.
# i.e. if devtools has a new package installed, all dependent project's 
# `poetry.lock` files need to be updated. this script should do all of that
# `setup.py` should not be required, but we shall see. `pyproject.toml`

function poetry_update_setup_sync () {
    echo "====================== $1"
    cd $1
    poetry lock
    poetry install
    cd ..
}

# N.B. the order below here ensures that packages which are dependencies of other packages are updated first.
poetry_update_setup_sync "csvcubed-devtools"
poetry_update_setup_sync "csvcubed-models"
poetry_update_setup_sync "csvcubed-pmd"
poetry_update_setup_sync "csvcubed"
