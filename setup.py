from setuptools import setup

setup(
    name='cli_bot',
    version='0.01',
    description='CLI Bot',
    url='https://github.com/Yurii-Kovalenko/GOIT_Module9_HW',
    author='Yurii Kovalenko',
    author_email='yuriy.kovalenko.in@gmail.com',
    license='MIT',
    packages=['cli_bot'],
    entry_points={'console_scripts': ['cli-bot=cli_bot.cli_bot:main']}
)