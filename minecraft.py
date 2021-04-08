import subprocess

def start():
    return subprocess.call(['ssh', '-i' '/home/tab53/.ssh/sinkhole_to_doom/id_rsa', 'tab53@doom.srcf.net',
                            'systemctl', '--user', 'start', 'minecraft.service'])

def stop():
    return subprocess.call(['ssh', '-i' '/home/tab53/.ssh/sinkhole_to_doom/id_rsa', 'tab53@doom.srcf.net',
                            'systemctl', '--user', 'start', 'minecraft.service'])

def is_running():
    process = subprocess.run(['ssh', '-i' '/home/tab53/.ssh/sinkhole_to_doom/id_rsa', 'tab53@doom.srcf.net',
                              'systemctl', '--user', 'is-active', 'minecraft.service'], capture_output=True)
    output = process.stdout
    if output == 'active\n':
        return True
    else:
        return False

def status_text():
    if is_running():
        return "Running"
    else:
        return "Inactive"