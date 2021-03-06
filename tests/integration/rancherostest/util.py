import pytest
import subprocess
import time


def run_qemu(request, run_args=[]):
    subprocess.check_call('rm -f ./state/empty-hd.img', shell=True)
    print('\nrm ./state/*')
    print('\nStarting QEMU')
    p = subprocess.Popen(['./scripts/run'] + run_args,
                         stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)

    def fin():
        print('\nTerminating QEMU')
        p.terminate()

    request.addfinalizer(fin)
    return p


@pytest.mark.timeout(10)
def wait_for_ssh(ssh_command=['./scripts/ssh']):
    while subprocess.call(ssh_command + ['/bin/true']) != 0:
        time.sleep(1)
