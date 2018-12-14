import requests
import pandas as pd
import numpy as np

def get_individual_player_data(player_id):
    """ Retrieve the player-specific detailed data
    Args:
        player_id (int): ID of the player whose data is to be retrieved
    """
    base_url = "https://fantasy.premierleague.com/drf/element-summary/"
    full_url = base_url + str(player_id)
    response = ''
    while response == '':
        try:
            response = requests.get(full_url)
        except:
            time.sleep(5)
    if response.status_code != 200:
        raise Exception("Response was code " + str(response.status_code))
    data = [[player_id,x['total_points'],x['round'],x['opponent_team'],x['was_home']] for x in response.json()['history']]
    return data

r = requests.get('https://fantasy.premierleague.com/drf/bootstrap-static')
player_list = list((play['id'],play['team'],play['value_season'],play['element_type'], play['first_name']+' '+ play['second_name']) for play in r.json()['elements'])
team_list = list((t['id'],t['name'],t['short_name']) for t in r.json()['teams'])

df = pd.DataFrame(player_list, columns=['id','team','value','position', 'name'])
team_list = pd.DataFrame(team_list, columns=['id','longname','shortname'])
player_list = df['id']

def return_data(df = df):
    li = np.concatenate(list(x for x in list((get_individual_player_data(i)) for i in df['id'])),axis=0)
    pdf = pd.DataFrame(li, columns=['player','points','round','opponent','home'])
    pdf['team'] = [int(df['team'][df['id']==i]) for i in pdf['player']]
    pdf['team'] = [team_list[team_list['id']==i]['longname'].values[0] for i in pdf['team']]
    pdf['pos'] = [int(df['position'][df['id']==i]) for i in pdf['player']]
    pdf['opponent'] = [team_list[team_list['id']==i]['longname'].values[0] for i in pdf['opponent']]              
    home_pdf = pdf[pdf['home']==1]
    away_pdf = pdf[pdf['home']==0]

    piv_home = pd.DataFrame(home_pdf.groupby('team').round.nunique())
    piv_home['GKPP'] = pd.DataFrame(home_pdf[home_pdf['pos']==1]).groupby('team').points.sum()
    piv_home['DEFP'] = pd.DataFrame(home_pdf[home_pdf['pos']==2]).groupby('team').points.sum()
    piv_home['MIDP'] = pd.DataFrame(home_pdf[home_pdf['pos']==3]).groupby('team').points.sum()
    piv_home['ATTP'] = pd.DataFrame(home_pdf[home_pdf['pos']==4]).groupby('team').points.sum()
    piv_home['GKPP'] = round(piv_home['GKPP']/piv_home['round'],2)
    piv_home['DEFP'] = round(piv_home['DEFP']/piv_home['round'],2)
    piv_home['MIDP'] = round(piv_home['MIDP']/piv_home['round'],2)
    piv_home['ATTP'] = round(piv_home['ATTP']/piv_home['round'],2)
    piv_home.reset_index(level=0, inplace=True)

    piv_away = pd.DataFrame(away_pdf.groupby('team').round.nunique())
    piv_away['GKPP'] = pd.DataFrame(away_pdf[away_pdf['pos']==1]).groupby('team').points.sum()
    piv_away['DEFP'] = pd.DataFrame(away_pdf[away_pdf['pos']==2]).groupby('team').points.sum()
    piv_away['MIDP'] = pd.DataFrame(away_pdf[away_pdf['pos']==3]).groupby('team').points.sum()
    piv_away['ATTP'] = pd.DataFrame(away_pdf[away_pdf['pos']==4]).groupby('team').points.sum()
    piv_away['GKPP'] = round(piv_away['GKPP']/piv_away['round'],2)
    piv_away['DEFP'] = round(piv_away['DEFP']/piv_away['round'],2)
    piv_away['MIDP'] = round(piv_away['MIDP']/piv_away['round'],2)
    piv_away['ATTP'] = round(piv_away['ATTP']/piv_away['round'],2)
    piv_away.reset_index(level=0, inplace=True)

    con_away = pd.DataFrame(home_pdf.groupby('opponent').round.nunique())
    con_away['GKPP'] = pd.DataFrame(home_pdf[home_pdf['pos']==1]).groupby('opponent').points.sum()
    con_away['DEFP'] = pd.DataFrame(home_pdf[home_pdf['pos']==2]).groupby('opponent').points.sum()
    con_away['MIDP'] = pd.DataFrame(home_pdf[home_pdf['pos']==3]).groupby('opponent').points.sum()
    con_away['ATTP'] = pd.DataFrame(home_pdf[home_pdf['pos']==4]).groupby('opponent').points.sum()
    con_away['GKPP'] = round(con_away['GKPP']/con_away['round'],2)
    con_away['DEFP'] = round(con_away['DEFP']/con_away['round'],2)
    con_away['MIDP'] = round(con_away['MIDP']/con_away['round'],2)
    con_away['ATTP'] = round(con_away['ATTP']/con_away['round'],2)
    con_away.reset_index(level=0, inplace=True)

    con_home = pd.DataFrame(away_pdf.groupby('opponent').round.nunique())
    con_home['GKPP'] = pd.DataFrame(away_pdf[away_pdf['pos']==1]).groupby('opponent').points.sum()
    con_home['DEFP'] = pd.DataFrame(away_pdf[away_pdf['pos']==2]).groupby('opponent').points.sum()
    con_home['MIDP'] = pd.DataFrame(away_pdf[away_pdf['pos']==3]).groupby('opponent').points.sum()
    con_home['ATTP'] = pd.DataFrame(away_pdf[away_pdf['pos']==4]).groupby('opponent').points.sum()
    con_home['GKPP'] = round(con_home['GKPP']/con_home['round'],2)
    con_home['DEFP'] = round(con_home['DEFP']/con_home['round'],2)
    con_home['MIDP'] = round(con_home['MIDP']/con_home['round'],2)
    con_home['ATTP'] = round(con_home['ATTP']/con_home['round'],2)
    con_home.reset_index(level=0, inplace=True)

    print(piv_home)#,piv_away,con_home,con_away

