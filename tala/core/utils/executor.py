import subprocess

from celery import Celery

app = Celery('tasks', broker='redis://localhost:6379/0', backend='redis://localhost:6379/0')
SCRIPT_ROOT_DIR_PATH = '/'


@app.task
def add(x, y):
    return x + y


@app.task
def bare_metal_create():
    """
    物理サーバに対してOSのインストールを行います
    """
    distribution = 'ubuntu1604_x86-64'
    hostname = 'test1'
    username = 'test'
    root_password = 'test'
    ipmi_ip_address = '192.168.125.5'
    ipmi_username = 'admin'
    ipmi_password = 'admin'

    command = [SCRIPT_ROOT_DIR_PATH, 'bmcreate.sh', '-d', distribution, '-n', hostname, '-U', username, '-P', root_password, '-i', ipmi_ip_address, '-u', ipmi_username, '-p', ipmi_password]
    process = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout = process.stdout.decode('utf-8')
    stderr = process.stderr.decode('utf-8')


@app.task
def get_bare_metal_info():
    """
    物理サーバに対して情報の取得を行います
    """

    host_id = 2
    ipmi_ip_address = '192.168.125.5'
    ipmi_username = 'admin'
    ipmi_password = 'admin'

    command = [SCRIPT_ROOT_DIR_PATH, 'bmgetinfo.sh', '-H', host_id, '-i', ipmi_ip_address, '-u', ipmi_username, '-p', ipmi_password]
    process = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout = process.stdout.decode('utf-8')
    stderr = process.stderr.decode('utf-8')
