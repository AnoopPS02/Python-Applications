import requests
from bs4 import BeautifulSoup
import gspread
from oauth2client.service_account import ServiceAccountCredentials


scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('vturesults_secret.json',scope)
client = gspread.authorize(creds)

sheet = client.open('vturesults1').sheet1

show_timings = requests.get("https://in.bookmyshow.com/buytickets/2-0-bengaluru/movie-bang-ET00042213-MT/20181201")

soup = BeautifulSoup(show_timings.text,'html.parser')
show = soup.find_all('div',attrs={'class':'listing-info'})

for eachtheatre in show:
    name_list=eachtheatre.find('strong')
    print(name_list.contents[0])
    sheet.append_row([name_list.contents[0]])