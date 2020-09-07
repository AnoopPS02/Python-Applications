import requests
from bs4 import BeautifulSoup
import gspread
from oauth2client.service_account import ServiceAccountCredentials


scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('vturesults_secret.json',scope)
client = gspread.authorize(creds)

sheet = client.open('vturesults1').sheet1

page = requests.get("https://cbcs.fastvturesults.com/student/1ks17cs008")
soup = BeautifulSoup(page.text,'html.parser')
r_list = soup.find('div',attrs={'class':'container px-1'})
list=['1ks17cs008']
for l in r_list:
    r_list= l.find('p')

    for result in r_list:
            list.append(result.contents[0])
print(list)
    