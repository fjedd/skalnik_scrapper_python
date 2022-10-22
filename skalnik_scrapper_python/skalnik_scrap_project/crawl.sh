#!/bin/bash
# go to project location
cd /home/fjed/Documents/vscode/SCRAP_1/skalnik_scrapper_python/skalnik_scrap_project

NAME='ekspresy_'`date +\%d_\%m_\%Y`'.json'

# run spider
pipenv run scrapy crawl skalnik_ekspresy -O /home/fjed/Documents/vscode/SCRAP_1/skalnik_scrapper_python/skalnik_scrap_project/json_store/$NAME

printf "\nFILE SAVED AS $NAME \n"
