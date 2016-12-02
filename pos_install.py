# -*- coding:utf-8 -*-

import subprocess

programs_dev = ['python3', 'git', 'openjdk-9-jdk', 'python-software-properties',
                'php7.0', 'php7.0-fpm', 'php7.0-mysql', 'libapache2-mod-php7.0', 'composer', 'gcc', 'g++']

programs_dev_research = ['python3-scipy', 'octave', 'r-base', 'python-matplotlib', 'text_live',
                         'texlive-latex-extra', 'texlive-lang-portuguese', 'texlive-math-extra']

programs_media = ['vlc', 'amarok' ]
programs_utils = ['wine']

def install_media(**kwargs):

    output = ''
    for program in programs_media:
        try:
            print('Instalando: '+program)
            install_process = subprocess.Popen(['apt-get', 'install', '-y', program],
                                               stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            out, _ = install_process.communicate()
            output += out.decode('utf-8')
            print('Instalado: '+program)

        except Exception:
            print('Erro ao installar o programa')
            output, _ = install_process.communicate()

    print(output)



def __main__(**kwargs):
    from PackageManager import PackageManager

    package_install = PackageManager(verbose=True)
    # p = package_install.search('vlc')
    # print(p)
    # package_install.update_repository()
    package_install.install(['vlc', 'amarok'])

if __name__ == '__main__':
    __main__()