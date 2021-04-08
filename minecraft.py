import subprocess

def start():
    return subprocess.call(['ssh', '-i' '/home/tab53/.ssh/sinkhole_to_doom/id_rsa', 'tab53@doom.srcf.net',
                            'systemctl', '--user', 'start', 'minecraft.service'])

def stop():
    return subprocess.call(['ssh', '-i' '/home/tab53/.ssh/sinkhole_to_doom/id_rsa', 'tab53@doom.srcf.net',
                            'systemctl', '--user', 'start', 'minecraft.service'])

def status():
    process = subprocess.run(['ssh', '-i' '/home/tab53/.ssh/sinkhole_to_doom/id_rsa', 'tab53@doom.srcf.net',
                              'systemctl', '--user', 'is-active', 'minecraft.service'])
    output = process.stdout
    if output == 'active':
        return 'Running'
    else:
        return 'Inactive'