#!/bin/bash

# Clone the Git repository
git clone $GITHUB_REPO_LINK /code

# Install dependencies
pip install -r /code/requirements.txt

# Start the Django development server
cd /code

python manage.py runserver 0.0.0.0:4500
