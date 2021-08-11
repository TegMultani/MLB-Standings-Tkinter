import requests
import json

def getStandings():
    url = "https://datacrunch.9c9media.ca/statsapi/sports/baseball/leagues/mlb/standings/divisions?brand=tsn&tournamentId=&type=json"

    payload={}
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-CA,en-US;q=0.7,en;q=0.3',
    'Origin': 'https://www.tsn.ca',
    'Connection': 'keep-alive',
    'Referer': 'https://www.tsn.ca/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'Cache-Control': 'max-age=0',
    'TE': 'trailers',
    'Cookie': 'TS01b5e851=01881d1d7e48cd285c79c414a3cdca4a7548835551f22b1c7e168ba8527bb27c3f9024c20524cdb893e630a1d1471ca602b8a9e3a4'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    return response.json()    



def getSchedule(month, teamID, year):
    url = f"https://statsapi.mlb.com/api/v1/schedule?lang=en&sportId=1&hydrate=team(venue(timezone)),venue(timezone),game(seriesStatus,seriesSummary,tickets,promotions,sponsorships,content(summary,media(epg))),seriesStatus,seriesSummary,linescore,tickets,event(tickets),radioBroadcasts,broadcasts(all)&season={year}&startDate={year}-{month}-01&endDate={year}-{month}-31&teamId={teamID}&eventTypes=primary&scheduleTypes=games,events,xref"

    payload={}
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'en-CA,en-US;q=0.7,en;q=0.3',
    'Origin': 'https://www.mlb.com',
    'Connection': 'keep-alive',
    'Referer': 'https://www.mlb.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site'
    }

    r = requests.get(url, headers=headers, data=payload)
    data = r.json()

    return data




