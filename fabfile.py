# encoding: utf-8

from fabric.api import local, cd, run, env, prefix

env.hosts=['root@elephant']

def install_pythonbrew():
    run('yum install gcc patch zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel python-setuptools -y')
    run('yum groupinstall "Development tools" -y')
    run('easy_install pythonbrew')
    run('pythonbrew_install')
    with cd('~/.pythonbrew/etc/'):
        run('curl -O \
            https://gist.githubusercontent.com/jaron92/1692e8836f1311a5e03f/raw/c2a61f9304d70664034dec6739de3731140cd6a4/config.cfg')
    with prefix('source "$HOME/.pythonbrew/etc/bashrc"'):
        run('pythonbrew uninstall 2.7.7')
        run('pythonbrew install 2.7.7')


def create_venv(venv='ENV'):
    with prefix('source "$HOME/.pythonbrew/etc/bashrc"'):
        run('pythonbrew venv init')
        run('pythonbrew venv create %s -p 2.7.7' % venv)
        run('pythonbrew venv use %s' % venv)

def install_scrapy(venv='ENV'):
    run('yum install libffi-devel libxml2-dev libxslt-devel -y')
    with prefix('source "$HOME/.pythonbrew/etc/bashrc"'), prefix('pythonbrew venv use %s' % venv):
        run('pip install lxml')
        run('pip install Scrapy')
        
def init():
    print "install git"
    run('yum install git -y')
    print "install pythonbrew"
    install_pythonbrew()
    print "init venv"
    create_venv()
    print "install scrapy"
    install_scrapy()
