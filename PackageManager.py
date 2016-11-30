# -*- coding:utf-8 -*-
import subprocess


class PackageInstall:
    """
        Classe para instalar os pacotes por meio do terminal
    """

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

        self.cache = None

        if 'verbose' not in kwargs:
            self.verbose = False

        if 'package_manager' not in kwargs:
            self.package_manager = "apt-get"

    def update_repository(self, command="update"):
        """
        Atualiza o repositório

        :param comando, comando utilizado pelo gerenciador de pacotes para atualizações
        """
        if self.verbose:
            print('Atualizando')

        try:

            update_process = subprocess.Popen([self.package_manager, command, '-y'],
                                              stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            if self.verbose:
                self.__verbose_process__(update_process)

            print('\n'+'-'*20+'Repositório Atualizado'+'-'*20)
        except subprocess.TimeoutExpired as e:
            update_process.kill()
            print('\n-'*20+'Erro ao atualizar Repositório'+'-'*20)

            if self.verbose:
                print(e.output)
            raise e

    def search(self, package):
        """
        Busca pacotes baseados no nome informado
        :param package: nome do pacote buscado
        :return: dict no formato [nome_do_pacote : descricao]
        """

        if self.cache is not None:
            return self.cache

        print('Buscando Pacote '+package)
        search_process = subprocess.Popen(['apt-cache', 'search', package],
                                              stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

        verbose_buffer = "" #armazena a saida para utilizar no verbose
        self.cache = {}
        for stdout_line in search_process.stdout:
            package = stdout_line.decode('utf-8')
            verbose_buffer += package
            p = package.split(' - ')
            if len(p) >= 2:
                self.cache[p[0]] = p[1].rstrip('\n')

        if self.verbose:
            print('Verbose')
            print(verbose_buffer)

        return self.cache

    def __verbose_process__(self, process, enconde='utf-8'):
        """
        Exibe a saida do programa
        :param process: subprocess a ter a saida exibida
        :param encode: encode utilizado para exibir as mensagens
        """
        print('Verbose')
        for stdout_line in process.stdout:
            print(stdout_line.decode(enconde), end='', flush=True)
