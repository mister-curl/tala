import json
import subprocess

import django
from core.utils.my_cerely import get_app

django.setup()

SCRIPT_ROOT_DIR_PATH = '/opt/tala/bin/'
BASH = '/bin/bash'

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

    command = [BASH, SCRIPT_ROOT_DIR_PATH + 'bmgetinfo.sh', '-H', str(host_id), ]
    try:
        process = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if process.returncode != 0:
            raise
    except:
        stdout = process.stdout.decode('utf-8')
        stderr = process.stderr.decode('utf-8')
        print(stdout)
        print(stderr)
        return False
    return True


@app.task
def create_bare_metal(host_id, distribution, username):
    """
    物理サーバに対してOSのインストールを行います
    ベアメタル作成
    """

    command = [BASH, SCRIPT_ROOT_DIR_PATH + 'bmcreate.sh', '-H', str(host_id)]
    try:
        process = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if process.returncode != 0:
            raise
    except:
        stdout = process.stdout.decode('utf-8')
        stderr = process.stderr.decode('utf-8')
        print(stdout)
        print(stderr)
        return False
    return True


@app.task
def create_kvm_hyper_visor(host_id):
    """
    ベアメタルサーバからKVMホストを作成します
    BM→KVMホスト化
    """

    command = [BASH, SCRIPT_ROOT_DIR_PATH + 'kvmcreate.sh', '-H', str(host_id)]
    try:
        process = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if process.returncode != 0:
            raise
    except:
        stdout = process.stdout.decode('utf-8')
        stderr = process.stderr.decode('utf-8')
        print(stdout)
        print(stderr)
        return False
    return True


@app.task
def create_docker(host_id):
    """
    ベアメタルサーバからDockerホストを作成します
    BM→Dockerホスト化
    """

    command = [BASH, SCRIPT_ROOT_DIR_PATH + 'dockercreate.sh', '-H', str(host_id)]
    try:
        process = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if process.returncode != 0:
            raise
    except:
        stdout = process.stdout.decode('utf-8')
        stderr = process.stderr.decode('utf-8')
        print(stdout)
        print(stderr)
        return False
    return True


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

    command = [BASH, SCRIPT_ROOT_DIR_PATH + 'vmcreate.sh', '-H', str(host_id), '-n', node_name, '-c', str(allocate_cpu),
               '-m', str(allocate_memory_size), '-d', str(allocate_disk_size), '-o', vm_os, '-p', vm_password]
    try:
        process = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if process.returncode != 0:
            raise
    except:
        stdout = process.stdout.decode('utf-8')
        stderr = process.stderr.decode('utf-8')
        print(stdout)
        print(stderr)
        return False
    return True


@app.task
def get_power_for_node(host_id):
    """
    電源状態を取得します
    """

    command = [BASH, SCRIPT_ROOT_DIR_PATH + 'power.sh', '-H', str(host_id), '-O', 'status', '-T', 'bm']
    try:
        process = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if process.returncode != 0:
            raise
    except:
        stdout = process.stdout.decode('utf-8')
        stderr = process.stderr.decode('utf-8')
        print(stdout)
        print(stderr)
        return False
    return True


@app.task
def power_control_for_node(host_id, state):
    """
    電源状態を任意の状態に変更します
    """

    command = [BASH, SCRIPT_ROOT_DIR_PATH + 'power.sh', '-H', str(host_id), '-O', state, '-T', 'bm']
    try:
        process = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if process.returncode != 0:
            raise
    except:
        stdout = process.stdout.decode('utf-8')
        stderr = process.stderr.decode('utf-8')
        print(stdout)
        print(stderr)
        return False
    return True


@app.task
def create_container(container_id):
    """
    Dockerホスト上にContainerを作成します。
    """

    command = [BASH, SCRIPT_ROOT_DIR_PATH + 'condeploy.sh', '-H', str(container_id)]
    try:
        process = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if process.returncode != 0:
            raise
    except:
        stdout = process.stdout.decode('utf-8')
        stderr = process.stderr.decode('utf-8')
        print(stdout)
        print(stderr)
        return False
    return True