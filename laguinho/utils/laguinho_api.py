import requests
import json

from laguinho.values import API_URL

def create_github_url(metadata, is_file=False):
	"""Constrói a URL da API
	Constrói a URL base da API do github a partir
	dos dados presentes no metadata.
	Args:
			metadata: JSON com informações acerca do dataset.
			is_file: FLAG usada pra sinalizar se o dataset é apenas um elemento.
	"""
	url_params = metadata['url'].split('/')
	server_idx = url_params.index('github.com')
	username = url_params[server_idx + 1]
	repo = url_params[server_idx + 2]
	data_path = metadata['path']

	return ("https://raw.githubusercontent.com/{}/{}/master{}" if is_file else "https://api.github.com/repos/{}/{}/contents{}").format(username, repo, data_path)


def request_github_api(url):
	"""Faz uma requisição a API do Github.
	Faz uma requisição a API do Github.
	Args:
			url: URL do Github a ser requisitada.
	"""
	response = requests.get(url)
	return response.content

def request_laguinho_api(endpoint):
	"""Faz uma requisição a API do Laguinho.


	Faz uma requisição a API do Laguinho.

	Args:
			endpoint: Endpoint do Laguinho a ser requisitada.
	"""
	response = requests.get(API_URL + endpoint)
	return response.content

def get_dataset(name):
	response = request_laguinho_api("/datasets/{}".format(name))
	return json.loads(response)
