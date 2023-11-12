# Engeto akademie: třetí projekt 

## Popis projektu:

Tento projekt slouží k extrahování výsledků z parlamentních voleb v roce 2017.
Odkaz k prohlédnutí najdete zde.

## Instalace knihoven:

Knihovny, které jsou použity v kódu jsou uloženy v souboru requirements.txt.
Pro instalaci doporučuji použít nové virtuální prostředí a s nainstalovaným manažerem spustit následovně:
pip3 --version
pip3 --install -r requirements.txt
Spuštění projektu:
Spuštění souboru elections_scraper.py v rámci příkazového řádku požaduje dva povinné argumenty.

> python elections_scraper url vystupni_soubor

## Ukázka projektu:
Výsledky hlasování pro okres Praha-východ
> 1. argument: https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2109
> 2. argument: output.csv

## Spuštění programu:

> python elections_scraper.py ´https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2109

## Průběh stahování:

> Stahuji data z vybraného url: https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2109
> Ukládám do souboru: output.csv
> Ukoncuji elections_scraper

## Částečný výstup:

> code	    location	registered	envelopes	valid
>
> 538043	Babice	    732	        533	        531
> 
> 538051	Bašť	    1 409	    966	        961


