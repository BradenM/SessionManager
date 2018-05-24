from setuptools import setup

setup(
    name='SessionManager',
    version='1.0.0',
    packages=['gui', 'gui.ui', 'gui.ui.assets', 'gui.ui.settings', 'gui.dialogs', 'gui.threads', 'gui.widgets', 'data',
              'utils', 'manage'],
    package_dir={'': 'sessionmanager'},
    url='https://github.com/BradenM/SessionManager',
    license='GNU General Public License v3.0',
    author='Braden Mars',
    author_email='bradenmars02@gmail.com',
    description='Easy to use session manager for photographers'
)
