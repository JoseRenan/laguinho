import json
import os
import click

from pathlib import Path
from ..utils.laguinho_api import get_dataset, request_github_api, request_laguinho_api


@click.command('get', short_help="Retorna dados do repositório.")
@click.argument('name', required=True, type=str)
def get(name):
	"""Retorna os dados disponiveis de um determinado repositório do github."""
	click.echo('Recuperando dados de %s' % name)
	dataset = get_dataset(name)
	download_dataset(name, dataset)
	click.echo("\nArquivo(s) baixado(s) com sucesso!\n")

def download_dataset(name, dataset):
	"""Baixa os arquivos do github


	Baixa os arquivos através da API do Github.

	Args:
			metadata: JSON com informações acerca do dataset.
	"""
	current_path = os.getcwd()
	dir_path = "{}/{}".format(current_path, name)

	mkdir_and_cd(dir_path)
	check_dataset(name, dataset)

def check_dataset(name, dataset):
	""" Checa o dataset


	Verifica se o elemento específicado no atributo path é um diretório ou um
	arquivo. Caso seja um diretório, é chamada a função create, caso contrário,
	o arquivo é criado.

	Args:
			metadata: JSON com informações acerca do dataset.
	"""
	
	for data in dataset:
		click.echo("Criando arquivo {}{}".format(name, data))
		create_dir(data)
		content = request_github_api(dataset[data])
		with open(".{}".format(data), 'wb') as file:
			file.write(content)

def create_dir(filename):
	"""Cria um diretório

	Cria um diretório do dataset utilizando as biblioteca
	'so'. Após a criação, é chamada a função 'create' passando
	os elementos dentro do respectivo diretório criado.

	Args:
			github_url: URL  base do github usada na criação
			dos repositórios.

			content: Elemento retornado pela API do github
			referente ao diretório a ser criado.

	"""
	dir_path = os.getcwd() + '/' + '/'.join(filename.split('/')[:-1])
	path = Path(dir_path)
	path.mkdir(parents=True, exist_ok=True)

def mkdir_and_cd(dir_path):
	"""Cria e entra em um determinado diretório"""
	path = Path(dir_path)
	path.mkdir(parents=True, exist_ok=True)
	os.chdir(dir_path)
