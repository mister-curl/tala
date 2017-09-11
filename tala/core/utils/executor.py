import subprocess

import django
from core.utils.my_cerely import get_app

django.setup()

SCRIPT_ROOT_DIR_PATH = '/'

app = get_app()


@app.task
def add(x, y):
    return x + y


@app.task
def get_bare_metal_info(host_id):
    """
    物理サーバに対して情報の取得を行います
    BM 情報取得
    """

    command = [SCRIPT_ROOT_DIR_PATH, 'bmgetinfo.sh', '-H', str(host_id), ]
    process = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout = process.stdout.decode('utf-8')
    stderr = process.stderr.decode('utf-8')


@app.task
def create_bare_metal(host_id, distribution, username):
    """
    物理サーバに対してOSのインストールを行います
    ベアメタル作成
    """

    command = [SCRIPT_ROOT_DIR_PATH, 'bmcreate.sh', '-H', str(host_id), '-d', distribution, '-U', username]
    process = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout = process.stdout.decode('utf-8')
    stderr = process.stderr.decode('utf-8')


@app.task
def create_kvm_hyper_visor(host_id):
    """
    ベアメタルサーバからKVMホストを作成します
    BM→KVMホスト化
    """

    command = [SCRIPT_ROOT_DIR_PATH, 'kvmcreate.sh', '-H', str(host_id)]
    process = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout = process.stdout.decode('utf-8')
    stderr = process.stderr.decode('utf-8')


@app.task
def create_virtual_machine(host_id, node_name):
    """
    KVMホスト上にVMを作成します。
    VM作成
    """
    allocate_cpu = 2
    allocate_memory_size = 1024
    allocate_disk_size = 10
    vm_os = 'ubuntu1604_x86-64'
    vm_password = 'test'

    command = [SCRIPT_ROOT_DIR_PATH, 'vmcreate.sh', '-H', str(host_id), '-n', node_name, '-c', str(allocate_cpu),
               '-m', str(allocate_memory_size), '-d', str(allocate_disk_size), '-o', vm_os, '-p', vm_password]

    process = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout = process.stdout.decode('utf-8')
    stderr = process.stderr.decode('utf-8')
