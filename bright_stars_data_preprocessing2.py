from bs4  import BeautifulSoup
import request 
import pandas as pd
bright_statrs_url='https://en.wikipedia.ong/wiki/list_of_brightest_stars_and_other_record_starts'

page=request.get(bright_stars_url)

soup=bs(page.text,'html.parcer')
star_table=soup.find('table')
temp_list=[]
table_rowse=start_table.find_all('tr')
for tr in table_rowse:
    td=tr.find_all('td')