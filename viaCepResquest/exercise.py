import requests

cep = "08471120"
url = f"http://viacep.com.br/ws/{cep}/json"
retorno = requests.get(url)
dici = retorno.json()

logradouro = dici['logradouro']
complemento = dici['complemento'] 
unidade = dici['unidade']
bairro = dici['bairro']
localidade = dici['localidade']
uf = dici['uf']
ibge = dici['ibge']
gia = dici['gia']
ddd = dici['ddd']
siafi = dici['siafi']

retorno.status_code #(deveria ser 200 se deu certo)

print(f"CEP ({cep}):\n{logradouro} - {unidade} - {bairro} - {localidade} - {uf} - {ibge} - {gia} - {ddd} - {siafi} ")