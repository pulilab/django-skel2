# {{ project_name|title }} Django Project #
## Prerequisites ##

- python >= 2.5
- pip
- virtualenv/wrapper (optional)

## Features ##

The following apps are included by default:

* django storages
* south
* django hilbert
* raven

If you install the development packages, development requires:

* django extensions
* django nose
* django pdb

### SSL settings ###

Be default ssl is enabled, and set to be forced for the admin site.

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

## Configure project ##

We have three settings files:

We have a `{{ project_name }}/settings_common.py` file contains most of the settings. The `settings.py` and `settings_local.py` files extend `settings_common.py`

```bash
vi {{ project_name }}/settings_local.py
```

## Sync database ##

South is installed, use it!

```bash
python manage.py syncdb --migrate
```

## Running ##
```bash
python manage.py runserver
```

Open browser to http://127.0.0.1:8000

## Deployment ##

The project contains a fabfile. You might want to review it and you should definitely set it up correctly. The most important commands are the following:

staging
	loads staging environment
productions
	loads production environment
test
	runs your specified tests
prepare_deploy
	runs the tests and commits/pushes on success
deploy
	check out a remote copy, and restarts the server