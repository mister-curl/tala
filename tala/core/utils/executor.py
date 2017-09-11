import subprocess

from celery import Celery

app = Celery('tasks', broker='redis://localhost:6379/0', backend='redis://localhost:6379/0')
SCRIPT_ROOT_DIR_PATH = '/'


@app.task
def add(x, y):
    return x + y


@app.task
def get_bare_metal_info():
    """
    物理サーバに対して情報の取得を行います
    BM 情報取得
    """

    host_id = 1

    command = [SCRIPT_ROOT_DIR_PATH, 'bmgetinfo.sh', '-H', host_id, ]
    process = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout = process.stdout.decode('utf-8')
    stderr = process.stderr.decode('utf-8')


@app.task
def create_bare_metal():
    """
    物理サーバに対してOSのインストールを行います
    ベアメタル作成
    """
    host_id = 1
    distribution = 'ubuntu1604_x86-64'
    username = 'test'

    command = [SCRIPT_ROOT_DIR_PATH, 'bmcreate.sh', '-H', host_id, '-d', distribution, '-U', username]
    process = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout = process.stdout.decode('utf-8')
    stderr = process.stderr.decode('utf-8')


@app.task
def create_kvm_hyper_visor():
    """
    ベアメタルサーバからKVMホストを作成します
    BM→KVMホスト化
    """
    host_id = 1

    command = [SCRIPT_ROOT_DIR_PATH, 'kvmcreate.sh', '-H', host_id]
    process = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout = process.stdout.decode('utf-8')
    stderr = process.stderr.decode('utf-8')


@app.task
def create_virtual_machine():
    """
    KVMホスト上にVMを作成します。
    VM作成
    """
    host_id = 1
    node_name = ''
    allocate_cpu = 2
    allocate_memory_size = 1024
    allocate_disk_size = 10
    vm_os = 'ubuntu1604_x86-64'
    vm_password = 'test'

    command = [SCRIPT_ROOT_DIR_PATH, 'vmcreate.sh', '-H', host_id, '-n', node_name, '-c', allocate_cpu,
               '-m', allocate_memory_size, '-d', allocate_disk_size, '-o', vm_os, '-p', vm_password]

    process = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout = process.stdout.decode('utf-8')
    stderr = process.stderr.decode('utf-8')