import os
from season.season import season
import json
import pandas

# importando os dados:
#dados_season = season("4fa03c5d1fb45efde700cd4e48af9971")
dados_season_test = '{"get":"seasons","parameters":[],"errors":[],"results":13,"response":[2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024]}'
json_dados = json.loads(dados_season_test )
anos = json_dados['response'] 

list_season = anos


