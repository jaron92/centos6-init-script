# encoding: utf-8

from fabric.api import local, cd, run, env, prefix

env.hosts=['root@elephant']

def create_python_venv(reinstall=False, venv='ENV'):
    if reinstall:
        print "install pythonbrew"
        run('yum install gcc patch zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel python-setuptools -y')
        run('easy_install pythonbrew')
        run('pythonbrew_install')
        run('yum groupinstall "Development tools" -y')
        with cd('~/.pythonbrew/etc/'):
            run('curl -O \
                https://gist.githubusercontent.com/jaron92/1692e8836f1311a5e03f/raw/c2a61f9304d70664034dec6739de3731140cd6a4/config.cfg')
    with prefix('source "$HOME/.pythonbrew/etc/bashrc"'):
        if reinstall:
            run('pythonbrew uninstall 2.7.7')
            run('pythonbrew install 2.7.7')
        run('pythonbrew switch 2.7.7')
        run('python -V')
        run('pythonbrew venv init')
        run('pythonbrew venv create %s -p 2.7.7' % venv)
        run('pythonbrew venv use %s' % venv)
        run('pip list')
        
def init():
    print "install git"
    run('yum install git -y')
    print "init venv"
    create_python_venv(reinstall=True)
