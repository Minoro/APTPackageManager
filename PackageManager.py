# -*- coding:utf-8 -*-
import subprocess


class PackageInstall:
    """
        Classe para instalar os pacotes por meio do terminal
    """

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

        if 'verbose' not in kwargs:
            self.verbose = False

        if 'package_manager' not in kwargs:
            self.package_manager = "apt-get"

    def update_repository(self, command="update"):
        """
        Atualiza o repositório

        Args:
            comando: comando utilizado pelo gerenciador de pacotes para atualizações
        """
        print('Atualizando')

        try:

            update_process = subprocess.Popen([self.package_manager, command, '-y'],
                                              stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            if self.verbose:
                print('Verbose')
                for stdout_line in update_process.stdout:
                    print(stdout_line.decode('utf-8'), end='', flush=True)

            print('\n'+'-'*20+'Repositório Atualizado'+'-'*20)
        except subprocess.TimeoutExpired as e:
            update_process.kill()
            print('\n-'*20+'Erro ao atualizar Repositório'+'-'*20)

            if self.verbose:
                print(e.output)
            raise e
