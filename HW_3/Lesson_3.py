import subprocess
result = subprocess.run('cat /etc/os-release', shell=True, stdout=subprocess.PIPE, encoding='utf-8')
out = result.stdout

if result.returncode == 0:
    if '22.04' in out and 'jammy' in out:
        print('SUCSESS')
    else:
        print('FAIL')