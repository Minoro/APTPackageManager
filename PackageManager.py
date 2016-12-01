# -*- coding:utf-8 -*-
import subprocess


class PackageManager:
    """
        Classe para gerenciar os pacotes por meio de comandos do terminal
    """

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

        self.cache = None

        if 'verbose' not in kwargs:
            self.verbose = False

        if 'package_manager' not in kwargs:
            self.package_manager = 'apt-get'

        if 'cmd_update' not in kwargs:
            self.cmd_update = 'update'

    def update_repository(self):
        """
        Atualiza o repositório. Equivale a apt-get update -y
        """
        if self.verbose:
            print('Atualizando')

        update_process = subprocess.Popen([self.package_manager, self.cmd_update, '-y'],
                                          stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        output = self.__run_process__(update_process)

        if self.verbose:
            print(output)

        print('\n' + '-' * 20 + 'Repositório Atualizado' + '-' * 20)

    def search(self, package):
        """
        Busca pacotes baseados no nome informado. Equivale a apt-cache search pacote
        :param package: nome do pacote buscado
        :return: dict no formato [nome_do_pacote : descricao]
        """

        if self.cache is not None:
            return self.cache

        print('Buscando Pacote ' + package)
        search_process = subprocess.Popen(['apt-cache', 'search', package],
                                          stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

        output = self.__run_process__(search_process)

        self.cache = {}
        for line in output.split('\n'):
            package = line.split(' - ')

            if len(package) >= 2:
                self.cache[package[0]] = ''.join(package[1:])

        if self.verbose:
            print(output)

        return self.cache

    def install_package(self, package):
        """
        Instala um unico pacote informado como argumento. Equivale a apt-get install pacote -y
        :param package: pacote a ser instalado
        :return string: saida do terminal
        """
        pass

    def __run_process__(self, process, enconde='utf-8'):
        """
        Executa um processo
        :param process: subprocess a ter a saida exibida
        :param encode: encode utilizado para exibir as mensagens
        :return string: saida do terminal
        """
        verbose_buffer = ""
        for stdout_line in process.stdout:
            output = stdout_line.decode(enconde)

            verbose_buffer += output
        return verbose_buffer
