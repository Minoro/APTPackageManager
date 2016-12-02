# APTPackageManager
Wrapper para o utilizar os comandos do apt-get em python. Todos os comando são executados sem a necessidade de interação do usuário com o terminal, equivalente a executar as funções com o argumento `-y`. É necessário ser `sudo` para utilizar o script.

# Exemplos de Uso
Para utilizar os comandos do apt-get no python basta instanciar o objeto PackageManager.
```python
  pm = PackageManager()
```
O construtor aceita os seguintes argumentos:
* verbose = exibe as mensagens do apt-get no terminal (padrão `False`)
* package_manager = gerenciador de pacotes do sistema (padrão `apt-get`)
* cmd_update = comando utilizado para atualizar o repositório (padrão `update`)

## Atualização do repositório
Atualização do repositório de pacotes. Equivale a _apt-get update_
```python
  pm.update_repository()
```

## Instalação de pacotes
Instala um ou mais pacotes. Equivale a _apt-get install -y [pacote]_
```python
  pm = PackageManager()
  pm.install('vlc')
```
É possível instalar um conjunto de pacotes passando uma lista com os nomes dos pacotes.
```python
  pm.install(['vlc', 'amarok', 'gcc'])
```
