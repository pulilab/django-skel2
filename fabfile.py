#!/usr/bin/env python
# usage: fab staging deploy

from __future__ import with_statement
from fabric.api import local, settings, abort, run, cd, env, sudo
from fabric.contrib.console import confirm
import os
import logging

logging.basicConfig()
logging.getLogger('ssh.transport').setLevel(logging.INFO)
env.just_cloned = False

def staging():
    """Configure these"""
    env.user = '<user>'
    env.hosts = ['184.106.96.201']
    env.project_root = '<project_root>/{{ project_name }}'
    env.GIT_REPO = 'git@github.com:<git_user>/{{project_name}}.git'
    env.APPS = [] # put your apps here that should tests run before deploy
    env.SETTINGS_LOCAL = '{{project_name}}.settings_local' 
    env.virtualenv_root = '%(project_root)s/_env' % env
    env.activate = "source %(virtualenv_root)s/bin/activate && " % env
    env.branch = 'develop'
                                                                                
def production():
    """Update staging configuration as needed"""
    staging()
    env.branch = 'master'

def test(apps=[]):
    """Run tests for env.APPS"""
    if len(apps) == 0:
        apps = env.APPS
    #run tests
    local("DJANGO_SETTINGS_MODULE=%s python manage.py test %s" % (env.SETTINGS_LOCAL, ' '.join(env.APPS)))

def commit():
    """Git commit with all the new files"""
    with settings(warn_only=True):
        local("git add -p")
    with settings(warn_only=True):
        local("git commit")

def push():
    """Git push"""
    local("git push")

def prepare_deploy():
    """Run the test, commit and push"""
    test()    
    commit()
    push()

def clone_repo_if_needed():
    """Git clone if no repo is present"""
    with settings(warn_only=True):
        if run("test -d %(project_root)s" % env).failed:
            run("git clone %(GIT_REPO)s %(project_root)s" % env)
            env.just_cloned = True

def create_virtualenv():
    """Create the virtualenv"""
    args = '--clear --distribute'
    run('virtualenv %s %s' % (args, env.virtualenv_root))
    with cd(env.project_root):
        run(env.activate + "pip install -r requirements-production.txt")

def run_with_failure(command, question):
    """Utility script to run a command with a confirmation to exit on failure

    :param command: the command to run
    :param question: the user friendly notice what failed
    """
    with settings(warn_only=True):
        result = run(command)
    if result.failed and not confirm("%s Continue anyway?" % question):
        abort('Aborting on your request')

def deploy():
    """Updates the server and restarts it"""
    clone_repo_if_needed()

    with cd(env.project_root):
        run_with_failure('git pull --all', 'Updating all repos failed.')
        run_with_failure('git checkout %s' % env.branch, 'Updating %s branch failed.' % env.branch)
        run_with_failure('git pull', 'Git pull failed.')
        #update submodules
        run("git submodule init")
        run("git submodule update")
            
        if env.just_cloned:
            create_virtualenv()

        run_with_failure(env.activate + "pip install -r requirements.txt", 'Installing requirements failed.')
        run_with_failure(env.activate + "python manage.py syncdb --migrate --noinput", "Syncdb failed.")
        run_with_failure(env.activate + "python manage.py collectstatic --noinput", "Collectstatic failed.")
        run("touch {{project_name}}/wsgi.py")

        #sudo("apache2ctl restart")

def manage(cmd):
    """Runs a custom `manage.py` command remotely"""
    with cd(env.project_root):
        run(env.activate + "DJANGO_SETTINGS_MODULE=%s python manage.py %s" % (env.SETTINGS_LOCAL, cmd))
