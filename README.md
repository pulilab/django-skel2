# {{ project_name|title }} Django Project #
## Prerequisites ##

- python >= 2.5
- pip
- virtualenv/wrapper (optional)

## Installation ##
### Creating the environment ###
Create a virtual python enviroment for the project.
If you're not using virtualenv or virtualenvwrapper you may skip this step.

#### For virtualenvwrapper ####
```bash
mkvirtualenv {{ project_name }}-env
```

#### For virtualenv ####
```bash
virtualenv --no-site-packages {{ project_name }}-env
cd {{ project_name }}-env
source bin/activate
```

### Clone the code ###
Obtain the url to your git repository.

```bash
git clone <URL_TO_GIT_REPOSITORY> {{ project_name }}
```

### Install requirements ###
```bash
cd {{ project_name }}
pip install -r requirements.txt
```

There are two additional requirement files that you might want to install as well:

* requirements-dev
	provides the packages needed for development run
* requirements-production
	provides the packages needed for production installation

### Configure project ###

We have three settings files:

We have a `{{ project_name }}/settings_common.py` file contains most of the settings. The `settings.py` and `settings_local.py` files extend `settings_common.py`

```bash
vi {{ project_name }}/settings_local.py
```

### Sync database ###

South is installed, use it!

```bash
python manage.py syncdb --migrate
```

## Running ##
```bash
python manage.py runserver
```

Open browser to http://127.0.0.1:8000
