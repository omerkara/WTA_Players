import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

logo = Image.open('wta_logo.png')
st.set_page_config( page_title='WTA', page_icon=logo)


header = st.container()
player = st.container()
h2h = st.container()

color_field = 'white'
color_info = 'white'
color_achieved = '#e6e6e6'
color_letter = 'white'
color_rank = 'white'
color_h2h = 'white'

hide_menu = """
<style>
    #MainMenu {
        visibility:hidden;}
    footer {
        visibility: hidden;}
</style>
"""

@st.cache_data
def get_data(): 
    y23 = pd.read_csv("tennis_wta/matches/wta_matches_2023.csv")
    y22 = pd.read_csv("tennis_wta/matches/wta_matches_2022.csv")
    y21 = pd.read_csv("tennis_wta/matches/wta_matches_2021.csv")
    y20 = pd.read_csv("tennis_wta/matches/wta_matches_2020.csv")
    y19 = pd.read_csv("tennis_wta/matches/wta_matches_2019.csv")
    y18 = pd.read_csv("tennis_wta/matches/wta_matches_2018.csv")
    y17 = pd.read_csv("tennis_wta/matches/wta_matches_2017.csv")
    y16 = pd.read_csv("tennis_wta/matches/wta_matches_2016.csv")
    y15 = pd.read_csv("tennis_wta/matches/wta_matches_2015.csv")
    y14 = pd.read_csv("tennis_wta/matches/wta_matches_2014.csv")
    y13 = pd.read_csv("tennis_wta/matches/wta_matches_2013.csv")
    y12 = pd.read_csv("tennis_wta/matches/wta_matches_2012.csv")
    y11 = pd.read_csv("tennis_wta/matches/wta_matches_2011.csv")
    y10 = pd.read_csv("tennis_wta/matches/wta_matches_2010.csv")
    y09 = pd.read_csv("tennis_wta/matches/wta_matches_2009.csv")
    y08 = pd.read_csv("tennis_wta/matches/wta_matches_2008.csv")
    y07 = pd.read_csv("tennis_wta/matches/wta_matches_2007.csv")
    y06 = pd.read_csv("tennis_wta/matches/wta_matches_2006.csv")
    y05 = pd.read_csv("tennis_wta/matches/wta_matches_2005.csv")
    y04 = pd.read_csv("tennis_wta/matches/wta_matches_2004.csv")
    y03 = pd.read_csv("tennis_wta/matches/wta_matches_2003.csv")
    y02 = pd.read_csv("tennis_wta/matches/wta_matches_2002.csv")
    y01 = pd.read_csv("tennis_wta/matches/wta_matches_2001.csv")
    y00 = pd.read_csv("tennis_wta/matches/wta_matches_2000.csv")
    y999 = pd.read_csv("tennis_wta/matches/wta_matches_1999.csv")
    y998 = pd.read_csv("tennis_wta/matches/wta_matches_1998.csv")
    y997 = pd.read_csv("tennis_wta/matches/wta_matches_1997.csv")
    y996 = pd.read_csv("tennis_wta/matches/wta_matches_1996.csv")
    y995 = pd.read_csv("tennis_wta/matches/wta_matches_1995.csv")
    y994 = pd.read_csv("tennis_wta/matches/wta_matches_1994.csv")
    y993 = pd.read_csv("tennis_wta/matches/wta_matches_1993.csv")
    y992 = pd.read_csv("tennis_wta/matches/wta_matches_1992.csv")
    y991 = pd.read_csv("tennis_wta/matches/wta_matches_1991.csv")
    y990 = pd.read_csv("tennis_wta/matches/wta_matches_1990.csv")
    y989 = pd.read_csv("tennis_wta/matches/wta_matches_1989.csv")
    y988 = pd.read_csv("tennis_wta/matches/wta_matches_1988.csv")
    y987 = pd.read_csv("tennis_wta/matches/wta_matches_1987.csv")
    y986 = pd.read_csv("tennis_wta/matches/wta_matches_1986.csv")
    y985 = pd.read_csv("tennis_wta/matches/wta_matches_1985.csv")
    y984 = pd.read_csv("tennis_wta/matches/wta_matches_1984.csv")
    y983 = pd.read_csv("tennis_wta/matches/wta_matches_1983.csv")
    y982 = pd.read_csv("tennis_wta/matches/wta_matches_1982.csv")
    y981 = pd.read_csv("tennis_wta/matches/wta_matches_1981.csv")
    y980 = pd.read_csv("tennis_wta/matches/wta_matches_1980.csv")
    y979 = pd.read_csv("tennis_wta/matches/wta_matches_1979.csv")
    y978 = pd.read_csv("tennis_wta/matches/wta_matches_1978.csv")
    y977 = pd.read_csv("tennis_wta/matches/wta_matches_1977.csv")
    y976 = pd.read_csv("tennis_wta/matches/wta_matches_1976.csv")
    y975 = pd.read_csv("tennis_wta/matches/wta_matches_1975.csv")
    y974 = pd.read_csv("tennis_wta/matches/wta_matches_1974.csv")
    y973 = pd.read_csv("tennis_wta/matches/wta_matches_1973.csv")
    y972 = pd.read_csv("tennis_wta/matches/wta_matches_1972.csv")
    y971 = pd.read_csv("tennis_wta/matches/wta_matches_1971.csv")
    y970 = pd.read_csv("tennis_wta/matches/wta_matches_1970.csv")
    y969 = pd.read_csv("tennis_wta/matches/wta_matches_1969.csv")
    y968 = pd.read_csv("tennis_wta/matches/wta_matches_1968.csv")
    y967 = pd.read_csv("tennis_wta/matches/wta_matches_1967.csv")
    y966 = pd.read_csv("tennis_wta/matches/wta_matches_1966.csv")
    y965 = pd.read_csv("tennis_wta/matches/wta_matches_1965.csv")
    y964 = pd.read_csv("tennis_wta/matches/wta_matches_1964.csv")
    y963 = pd.read_csv("tennis_wta/matches/wta_matches_1963.csv")
    y962 = pd.read_csv("tennis_wta/matches/wta_matches_1962.csv")
    y961 = pd.read_csv("tennis_wta/matches/wta_matches_1961.csv")
    y960 = pd.read_csv("tennis_wta/matches/wta_matches_1960.csv")
    y959 = pd.read_csv("tennis_wta/matches/wta_matches_1959.csv")
    y958 = pd.read_csv("tennis_wta/matches/wta_matches_1958.csv")
    y957 = pd.read_csv("tennis_wta/matches/wta_matches_1957.csv")
    y956 = pd.read_csv("tennis_wta/matches/wta_matches_1956.csv")
    y955 = pd.read_csv("tennis_wta/matches/wta_matches_1955.csv")
    y954 = pd.read_csv("tennis_wta/matches/wta_matches_1954.csv")
    y953 = pd.read_csv("tennis_wta/matches/wta_matches_1953.csv")
    y952 = pd.read_csv("tennis_wta/matches/wta_matches_1952.csv")
    y951 = pd.read_csv("tennis_wta/matches/wta_matches_1951.csv")
    y950 = pd.read_csv("tennis_wta/matches/wta_matches_1950.csv")
    y949 = pd.read_csv("tennis_wta/matches/wta_matches_1949.csv")
    y948 = pd.read_csv("tennis_wta/matches/wta_matches_1948.csv")
    y947 = pd.read_csv("tennis_wta/matches/wta_matches_1947.csv")
    y946 = pd.read_csv("tennis_wta/matches/wta_matches_1946.csv")
    y945 = pd.read_csv("tennis_wta/matches/wta_matches_1945.csv")
    y944 = pd.read_csv("tennis_wta/matches/wta_matches_1944.csv")
    y943 = pd.read_csv("tennis_wta/matches/wta_matches_1943.csv")
    y942 = pd.read_csv("tennis_wta/matches/wta_matches_1942.csv")
    y941 = pd.read_csv("tennis_wta/matches/wta_matches_1941.csv")
    y940 = pd.read_csv("tennis_wta/matches/wta_matches_1940.csv")
    y939 = pd.read_csv("tennis_wta/matches/wta_matches_1939.csv")
    y938 = pd.read_csv("tennis_wta/matches/wta_matches_1938.csv")
    y937 = pd.read_csv("tennis_wta/matches/wta_matches_1937.csv")
    y936 = pd.read_csv("tennis_wta/matches/wta_matches_1936.csv")
    y935 = pd.read_csv("tennis_wta/matches/wta_matches_1935.csv")
    y934 = pd.read_csv("tennis_wta/matches/wta_matches_1934.csv")
    y933 = pd.read_csv("tennis_wta/matches/wta_matches_1933.csv")
    y932 = pd.read_csv("tennis_wta/matches/wta_matches_1932.csv")
    y931 = pd.read_csv("tennis_wta/matches/wta_matches_1931.csv")
    y930 = pd.read_csv("tennis_wta/matches/wta_matches_1930.csv")
    y929 = pd.read_csv("tennis_wta/matches/wta_matches_1929.csv")
    y928 = pd.read_csv("tennis_wta/matches/wta_matches_1928.csv")
    y927 = pd.read_csv("tennis_wta/matches/wta_matches_1927.csv")
    y926 = pd.read_csv("tennis_wta/matches/wta_matches_1926.csv")
    y925 = pd.read_csv("tennis_wta/matches/wta_matches_1925.csv")
    y924 = pd.read_csv("tennis_wta/matches/wta_matches_1924.csv")
    y923 = pd.read_csv("tennis_wta/matches/wta_matches_1923.csv")
    y922 = pd.read_csv("tennis_wta/matches/wta_matches_1922.csv")
    y921 = pd.read_csv("tennis_wta/matches/wta_matches_1921.csv")
    y920 = pd.read_csv("tennis_wta/matches/wta_matches_1920.csv")
    dataset = [y920, y921, y922, y923, y924, y925, y926, y927, y928, y929,
            y930, y931, y932, y933, y934, y935, y936, y937, y938, y939,
            y940, y941, y942, y943, y944, y945, y946, y947, y948, y949,
            y950, y951, y952, y953, y954, y955, y956, y957, y958, y959,
            y960, y961, y962, y963, y964, y965, y966, y967, y968, y969,
            y970, y971, y972, y973, y974, y975, y976, y977, y978, y979,
            y980, y981, y982, y983, y984, y985, y986, y987, y988, y989,
            y990, y991, y992, y993, y994, y995, y996, y997, y998, y999,
            y00, y01, y02, y03, y04, y05, y06, y07, y08, y09,
            y10, y11, y12, y13, y14, y15, y16, y17, y18, y19,
            y20, y21, y22, y23]


    def DropColumnsYear(ynnn):
        columns = ['tourney_id', 'tourney_name', 'surface', 'tourney_date', 'winner_id', 'winner_name', 
                'loser_id', 'loser_name', 'score', 'round', 'winner_rank', 'loser_rank']
        ynnn.drop(ynnn.columns.difference(columns), 1, inplace=True)
        ynnn['tourney_date'] = pd.to_datetime(ynnn['tourney_date'], format='%Y%m%d', errors='coerce')

    def CleanDF(dataset):
        for i in dataset:
            DropColumnsYear(i)
        return dataset

    dataset = CleanDF(dataset)
    matches = pd.concat(dataset)
    matchesh2h = matches.copy()
    matchesh2h[['set_1', 'set_2', 'set_3']] = matchesh2h['score'].str.split(' ', n=2, expand=True)
    matchesh2h[['set_1_player_1', 'set_1_player_2']] = matchesh2h['set_1'].str.split('-', n=1, expand=True)
    matchesh2h[['set_1_player_2_r', 'set_1_player_2_t']] = matchesh2h['set_1_player_2'].str.split('(', expand=True)
    matchesh2h[['set_2_player_1', 'set_2_player_2']] = matchesh2h['set_2'].str.split('-', n=1, expand=True)
    matchesh2h[['set_2_player_1_r', 'set_2_player_1_t']] = matchesh2h['set_2_player_1'].str.split('(', n=1, expand=True)
    matchesh2h[['set_2_player_2_r', 'set_2_player_2_t']] = matchesh2h['set_2_player_2'].str.split('(', n=1, expand=True)
    matchesh2h[['set_3_player_1', 'set_3_player_2']] = matchesh2h['set_3'].str.split('-', n=1, expand=True)
    matchesh2h[['set_3_player_1_r', 'set_3_player_1_t']] = matchesh2h['set_3_player_1'].str.split('(', n=1, expand=True)
    matchesh2h[['set_3_player_2_r', 'set_3_player_2_t']] = matchesh2h['set_3_player_2'].str.split('(', n=1, expand=True)
    matchesh2h.fillna("-",inplace=True)


    players = pd.read_csv("tennis_wta/wta_players.csv")
    players = players.iloc[2:,:]
    players = players[players['name_first'].notna()]
    players['dob'] = pd.to_datetime(players['dob'], format='%Y%m%d', errors='coerce')
    players.drop('wikidata_id', axis=1, inplace= True)
    players["full_name"] = players['name_first'].astype(str) +" "+ players["name_last"].astype(str)
    now = pd.Timestamp('now')   # 1
    players['dob'] = players['dob'].where(players['dob'] < now, players['dob'] -  np.timedelta64(100, 'Y'))
    players['age'] = (now - players['dob']).astype('<m8[Y]') 
    players['hand'].fillna("-",inplace=True)
    all_players = players['full_name'].to_list()

    rank_current = pd.read_csv("tennis_wta/wta_rankings_current.csv")
    rank_20 = pd.read_csv("tennis_wta/wta_rankings_20s.csv")
    rank_10 = pd.read_csv("tennis_wta/wta_rankings_10s.csv")
    rank_00 = pd.read_csv("tennis_wta/wta_rankings_00s.csv")
    rank_90 = pd.read_csv("tennis_wta/wta_rankings_90s.csv")
    rank_80 = pd.read_csv("tennis_wta/wta_rankings_80s.csv")
    ranks = [rank_current, rank_20, rank_10, rank_00, rank_90, rank_80]

    def FechaRank(ranks):
        for i in ranks:
            i['ranking_date'] = pd.to_datetime(i['ranking_date'], format='%Y%m%d', errors='coerce')

    FechaRank(ranks)
    r = pd.concat(ranks)

    return matches, matchesh2h, players, rank_current, r, all_players

st.markdown(hide_menu, unsafe_allow_html=True)


with header:
    with st.columns(3)[1]:
        st.image("wta.png")
        matches, matchesh2h, players, rank_current, r, all_players = get_data() 


with player:
    col1, col2, col3 = st.columns([1.09,2,1])
    with col2:
        st.title("PLAYER STATS", anchor=False)
    st.write('')
    st.write('')
    
    img, b, info = st.columns([2,1,3])
    
    player = img.selectbox('Select player:', options=all_players, index=14542)

    playinfo = players[players['full_name'] == player]
    first_name = playinfo.iloc[0][1]
    last_name = playinfo.iloc[0][2]

    try:
        dob = playinfo.iloc[0][4].strftime('%b %d, %Y')
        age = str(int(playinfo.iloc[0][10]))
    except:
        dob = '-'
        age = '-'

    if not pd.isna(playinfo.iloc[0][5]):
        country = playinfo.iloc[0][5]
    else:
        country = ''

    try:
        height = str(int(playinfo.iloc[0][6]))
    except:
        height = '-'

    if playinfo.iloc[0][3] == 'R':
        hand = 'Right-Handed'
    if playinfo.iloc[0][3] == 'L':
        hand = 'Left-Handed'
    if playinfo.iloc[0][3] == 'U':
        hand = '-'
    if ((playinfo.iloc[0][3] != 'R') & (playinfo.iloc[0][3] != 'L') & (playinfo.iloc[0][3] != 'U')):
        hand = '-'
        
    id_ = playinfo.iloc[0][0]

    if (rank_current['player'] == id_).any():
        year_rank = rank_current.loc[rank_current['player'] == id_]
        curr_rank_row = year_rank.loc[year_rank['ranking_date'] == year_rank['ranking_date'].max()]
        curr_rank = curr_rank_row.iloc[0][1]
    else:
        curr_rank = '-'

    if ~playinfo['image'].isnull().values.any():
        image = playinfo.iloc[0][7]
    else:
        image = 'silueta.png'

    img.image(
                image,
                width=350
            )

    player1_wta_singlestitles = len(matches[(matches['winner_id'] == id_) & (matches['round'] == 'F')])
    
    if (r['player'] == id_).any():
        career_high = int(r.loc[r['player'] == id_].min()[1])
        date_achieved = r[(r['player'] == id_) & (r['rank'] == career_high)].min()[0].strftime('%b %d, %Y')
    else:
        career_high = '-'
        date_achieved = ''

    if ~playinfo['flag'].isnull().values.any():
        flag = playinfo.iloc[0][8]
    else:
        flag = 'flag.png'

    lost_player1 = len(matches[(matches['loser_id'] == id_)])
    won_player1 = len(matches[(matches['winner_id'] == id_)])


    with info:

        st.markdown(f"<h3 style='text-align: left;color: {color_letter};'>{first_name} {last_name}</h3>", unsafe_allow_html=True)

        field, data = st.columns([.8,4])
        with field:
            st.markdown(f"<h5 style='text-align: left; color: {color_field};'>Age:</h5>", unsafe_allow_html=True)
        with data:
            st.markdown(f"<h5 style='text-align: left;color: {color_info};'>{age}</h5>", unsafe_allow_html=True)

        field, data = st.columns([3,2.5])
        with field:
            st.markdown(f"<h5 style='text-align: left; color: {color_field};'>Date of Birth:</h5>", unsafe_allow_html=True)
        with data:
            st.markdown(f"<h5 style='text-align: left;color: {color_info};'>{dob}</h5>", unsafe_allow_html=True)

        col1, col2, col3, col4 = st.columns([2,1.3, 0.8, 1])
        with col1:
            st.markdown(f"<h5 style='text-align: left; color:{color_field};'>Country:</h5>", unsafe_allow_html=True)
            st.markdown(f"<h5 style='text-align: left; color: {color_info};'> {country}</h5>", unsafe_allow_html=True)
        with col2:
            st.image(flag, width=63, use_column_width="always")

        field, data = st.columns([1.1,2.5])
        with field:
            st.markdown(f"<h5 style='text-align: left;color:{color_field};'>Height:</h5>", unsafe_allow_html=True)
        with data:
            st.markdown(f"<h5 style='text-align: left;color: {color_info};'>{height} cm</h5>", unsafe_allow_html=True)

        field, data = st.columns([1.1,2.8])
        with field:   
            st.markdown(f"<h5 style='text-align: left;color:{color_field};'>Plays:</h5>", unsafe_allow_html=True)
        with data:
            st.markdown(f"<h5 style='text-align: left;color: {color_info};'>{hand}</h5>", unsafe_allow_html=True)

        field, data = st.columns([5,2.8])
        with field: 
            st.markdown(f"<h5 style='text-align: left; color:{color_field}'>Current Ranking: </h5>", unsafe_allow_html=True)
        with data:
            st.markdown(f"<h5 style='text-align: left;color: {color_info};'>{str(curr_rank)}</h5>", unsafe_allow_html=True)

        field, data, ach = st.columns([3,0.5,2.3])
        with field: 
            st.markdown(f"<h5 style='text-align: left;color:{color_field}'>Career High:</h5>", unsafe_allow_html=True)
        with data:
            st.markdown(f"<h5 style='text-align: left;color: {color_info}'>{str(career_high)}</h5>", unsafe_allow_html=True)

        field, data = st.columns([1.8,1])
        with field:
            st.markdown(f"<h5 style='text-align: left; color:{color_field};'>Singles Titles:</h5>", unsafe_allow_html=True)
        with data:
            st.markdown(f"<h5 style='text-align: left;color: {color_info};'>{str(player1_wta_singlestitles)} </h5>", unsafe_allow_html=True)

            
            
with h2h:
    st.write("")
    st.write("")
    st.write("")
    st.markdown("<h1 style='text-align: center;'>HEAD 2 HEAD</h1>", unsafe_allow_html=True)
    st.write("")
    st.write("")
    player2 = h2h.selectbox('Select another player to know H2H:', options=all_players, index=6250)

    if not player == player2:
        playinfo2 = players[players['full_name'] == player2]
        id_2 = playinfo2.iloc[0][0]
        
        play1, brk, result, play2 = st.columns([2.7,0.3, 2.3,2.7])

        with play1:
            play1.image(
                    image,
                    width=350,
                    use_column_width="always"
                )
            
            st.markdown(f"<h3 style='text-align: left;'>{first_name}</h3>", unsafe_allow_html=True)
            st.markdown(f"<h2 style='text-align: left;'>{last_name}</h2>", unsafe_allow_html=True)

            col1, col2, col3 = st.columns([3, 2,1])
            with col1:
                st.markdown(f"<h4 style='text-align: left;'>{country}</h4>", unsafe_allow_html=True)
            with col2:
                st.image(flag, width=63)

            col1, col2, col3 = st.columns([2, 2, 1])
            with col1:
                st.markdown(f"<div style='text-align: left;'>Ranking</div>", unsafe_allow_html=True)
            with col2:
                st.markdown(f"<h5 style='text-align: left; color:{color_rank};'><b>{curr_rank}</b></h5>", unsafe_allow_html=True)

        with result:
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")


            won_player1_df = (matchesh2h[(matchesh2h['winner_id'] == id_) & (matchesh2h['loser_id'] == id_2) & (matchesh2h['score'] != 'W/O')])
            matches_player1 = len(won_player1_df)

            won_player2_df = matchesh2h[(matchesh2h['winner_id'] == id_2) & (matchesh2h['loser_id'] == id_) & (matchesh2h['score'] != 'W/O')]
            matches_player2 = len(won_player2_df)


            r1, h, h2, r2 = st.columns([2,1,1, 2])
            with r1:
                st.write(f'## {matches_player1}')
            with h:
                st.write('## -')
            with r2:
                    st.write(f'## {matches_player2}')
            
            
        with play2: 

            first_name2 = playinfo2.iloc[0][1]
            last_name2 = playinfo2.iloc[0][2]

            try:
                dob2 = playinfo2.iloc[0][4].strftime('%b %d, %Y')
                age2 = str(int(playinfo2.iloc[0][10]))
            except:
                dob2 = '-'
                age2 = '-'

            if not pd.isna(playinfo2.iloc[0][5]):
                country2 = playinfo2.iloc[0][5]
            else:
                country2 = ''

            try:
                height2 = str(int(playinfo2.iloc[0][6]))
            except:
                height2 = '-'
            
            if playinfo2.iloc[0][3] == 'R':
                hand2 = 'Right-Handed'
            if playinfo2.iloc[0][3] == 'L':
                hand2 = 'Left-Handed'
            if playinfo2.iloc[0][3] == 'U':
                hand2 = '-'
            if ((playinfo2.iloc[0][3] != 'R') & (playinfo2.iloc[0][3] != 'L') & (playinfo2.iloc[0][3] != 'U')):
                hand2 = '-'

            id_2 = playinfo2.iloc[0][0]
            

            if (rank_current['player'] == id_2).any():
                year_rank2 = rank_current.loc[rank_current['player'] == id_2]
                curr_rank_row2 = year_rank2.loc[year_rank2['ranking_date'] == year_rank2['ranking_date'].max()]
                curr_rank2 = curr_rank_row2.iloc[0][1]
            else:
                curr_rank2 = '-'

            if ~playinfo2['image'].isnull().values.any():
                image2 = playinfo2.iloc[0][7]
            else:
                image2 = 'silueta.png'
            
            if (r['player'] == id_2).any():
                career_high2 = int(r.loc[r['player'] == id_2].min()[1])
                date_achieved2 = r[(r['player'] == id_2) & (r['rank'] == career_high2)].min()[0].strftime('%b %d, %Y')
            else:
                career_high2 = '-'
                date_achieved2 = ''

            if ~playinfo2['flag'].isnull().values.any():
                flag2 = playinfo2.iloc[0][8]
            else:
                flag2 = 'flag.png'

            play2.image(
                        image2,
                        width=350,
                        use_column_width="always"
                    )  
            
            player2_wta_singlestitles = len(matches[(matches['winner_id'] == id_2) & (matches['round'] == 'F')])
            lost_player2 = len(matches[(matches['loser_id'] == id_2)])
            won_player2 = len(matches[(matches['winner_id'] == id_2)])

            st.markdown(f"<h3 style='text-align: right;'>{first_name2}</h3>", unsafe_allow_html=True)
            st.markdown(f"<h2 style='text-align: right;'>{last_name2}</h2>", unsafe_allow_html=True)

            col1, col2, col3 = st.columns([1,2,3])
            with col2:
                st.image(flag2, width=63)
            with col3:
                st.markdown(f"<h4 style='text-align: right;'>{country2}</h4>", unsafe_allow_html=True)

            col1, col2, col3 = st.columns([1, 2, 2])
            with col2:
                st.markdown(f"<h5 style='text-align: right; color:{color_rank};'><b>{curr_rank2}</b></h5>", unsafe_allow_html=True)
            with col3:
                st.markdown(f"<div style='text-align: right;'>Ranking</div>", unsafe_allow_html=True)

        players_info = st.container()

        with players_info:
            st.write("")
            st.write("")
            st.write("")
            st.write("")

            pl1c, infoc, pl2c = st.columns(3)

            with pl1c:
                st.markdown("<h3 style='text-align: center;color:#7814ff;'>S</h3>", unsafe_allow_html=True)
                st.write("")
                st.markdown(f"""<div style="text-align: left;color:{color_h2h};">{player1_wta_singlestitles}</div>""", unsafe_allow_html=True)
                st.write("")
                st.markdown(f"""<div style="text-align: left;color:{color_h2h};">{won_player1}/{lost_player1}</div>""", unsafe_allow_html=True)
                st.write("")
                one, two = st.columns([0.5,3])
                with one:
                    st.markdown(f"""<div style="text-align: left;color:{color_h2h};">{career_high}</div>""", unsafe_allow_html=True)
                with two:
                    st.markdown(f"""<div style="text-align: left;color: {color_achieved}">{date_achieved}</div>""", unsafe_allow_html=True)
                st.write("")
                st.markdown(f"""<div style="text-align: left;color:{color_h2h};">{curr_rank}</div>""", unsafe_allow_html=True)


            with infoc:
                st.markdown("<h3 style='text-align: center;'>CAREER STATS</h3>", unsafe_allow_html=True)
                st.write("")
                st.markdown('<div style="text-align: center;">WTA Singles Titles</div>', unsafe_allow_html=True)
                st.write("")
                st.markdown('<div style="text-align: center;">W/L Singles</div>', unsafe_allow_html=True)
                st.write("")
                st.markdown('<div style="text-align: center;">Career Highest Ranking</div>', unsafe_allow_html=True)
                st.write("")
                st.markdown('<div style="text-align: center;">Current ranking</div>', unsafe_allow_html=True)
                st.write("")

            with pl2c:
                st.markdown("<h3 style='text-align: center;color:#7814ff;'>S</h3>", unsafe_allow_html=True)
                st.write("")
                st.markdown(f"""<div style="text-align: right;color:{color_h2h};">{player2_wta_singlestitles}</div>""", unsafe_allow_html=True)
                st.write("")
                st.markdown(f"""<div style="text-align: right;color:{color_h2h};">{won_player2}/{lost_player2}</div>""", unsafe_allow_html=True)
                st.write("")
                one, two = st.columns([3,0.5])
                with one:
                    st.markdown(f"""<div style="text-align: right;color: {color_achieved}">{date_achieved2}</div>""", unsafe_allow_html=True)
                with two:
                    st.markdown(f"""<div style="text-align: right;color:{color_h2h};;">{career_high2}</div>""", unsafe_allow_html=True)
                st.write("")
                st.markdown(f"""<div style="text-align: right;color:{color_h2h};">{curr_rank2}</div>""", unsafe_allow_html=True)


            st.markdown("<h3 style='text-align: center;color:#7814ff;'>S</h3>", unsafe_allow_html=True)
            
            pl1, info, pl2 = st.columns([2,3,2])

            with pl1:
                st.markdown("<h3 style='text-align: center;color:#7814ff;'>S</h3>", unsafe_allow_html=True)
                st.write("")
                st.markdown(f"""<div style="text-align: left;color:{color_h2h};">{age}</div>""", unsafe_allow_html=True)
                st.write("")
                st.markdown(f"""<div style="text-align: left;color:{color_h2h};">{dob}</div>""", unsafe_allow_html=True)
                st.write("")
                st.markdown(f"""<div style="text-align: left;color:{color_h2h};">{height}</div>""", unsafe_allow_html=True)
                st.write("")
                st.markdown(f"""<div style="text-align: left;color:{color_h2h};">{hand}</div>""", unsafe_allow_html=True)


            with info:
                st.markdown("<h3 style='text-align: center;'>PLAYER PROFILES</h3>", unsafe_allow_html=True)
                st.write("")
                st.markdown('<div style="text-align: center;">Age</div>', unsafe_allow_html=True)
                st.write("")
                st.markdown('<div style="text-align: center;">Date of Birth</div>', unsafe_allow_html=True)
                st.write("")
                st.markdown('<div style="text-align: center;">Height (cm)</div>', unsafe_allow_html=True)
                st.write("")
                st.markdown('<div style="text-align: center;">Plays</div>', unsafe_allow_html=True)

            with pl2:
                st.markdown("<h3 style='text-align: center;color:#7814ff;'>S</h3>", unsafe_allow_html=True)
                st.write("")
                st.markdown(f"""<div style="text-align: right;color:{color_h2h};">{age2}</div>""", unsafe_allow_html=True)
                st.write("")
                st.markdown(f"""<div style="text-align: right;color:{color_h2h};;">{dob2}</div>""", unsafe_allow_html=True)
                st.write("")
                st.markdown(f"""<div style="text-align: right;color:{color_h2h};">{height2}</div>""", unsafe_allow_html=True)
                st.write("")
                st.markdown(f"""<div style="text-align: right;color:{color_h2h};">{hand2}</div>""", unsafe_allow_html=True)

        matches = st.container()

        with matches:


            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.markdown("<h3 style='text-align: center;'>PREVIOUS MATCHES</h3>", unsafe_allow_html=True)
            st.write("")
            st.write("")

            matches_played = pd.concat([won_player1_df, won_player2_df])
            matches_played.sort_values(by='tourney_date', ascending=False, inplace=True)

            if not matches_played.empty:
                for index, row in matches_played.iterrows():
                    tournament_name = row['tourney_name']
                    surface = row['surface']
                    date = row['tourney_date'].year
                    winner_id = row['winner_id']
                    loser_id = row['loser_id']
                    if id_ == row['winner_id']:
                        s1_p1 = row['set_1_player_1']
                        s2_p1_r = row['set_2_player_1_r']
                        s2_p1_t = row['set_2_player_1_t']
                        s3_p1_r = row['set_3_player_1_r']
                        s3_p1_t = row['set_3_player_1_t']
                        s1_p2_r = row['set_1_player_2_r']
                        s1_p2_t = row['set_1_player_2_t']
                        s2_p2_r = row['set_2_player_2_r']
                        s2_p2_t = row['set_2_player_2_t']
                        s3_p2_r = row['set_3_player_2_r']
                        s3_p2_t = row['set_3_player_2_t']
                        if ((row['set_1'] == 'RET') |(row['set_2'] == 'RET')|(row['set_3'] == 'RET')):
                            ret_pl2 = 'RET'
                            ret_pl1 = ''
                        else:
                            ret_pl1 = ''
                            ret_pl2 = ''

                    if id_ == row['loser_id']:
                        s1_p2 = row['set_1_player_1']
                        s2_p2_r = row['set_2_player_1_r']
                        s2_p2_t = row['set_2_player_1_t']
                        s3_p2_r = row['set_3_player_1_r']
                        s3_p2_t = row['set_3_player_1_t']
                        s1_p1_r = row['set_1_player_2_r']
                        s1_p1_t = row['set_1_player_2_t']
                        s2_p1_r = row['set_2_player_2_r']
                        s2_p1_t = row['set_2_player_2_t']
                        s3_p1_r = row['set_3_player_2_r']
                        s3_p1_t = row['set_3_player_2_t']
                        if ((row['set_1'] == 'RET') |(row['set_2'] == 'RET')|(row['set_3'] == 'RET')):
                            ret_pl1 = 'RET'
                            ret_pl2 = ''
                        else:
                            ret_pl1 = ''
                            ret_pl2 = ''


                    tournament, players, result = st.columns([1.9, 3.5, 2.3])

                    if id_ == winner_id:
                        color_p1 = '#fff'
                        color_p2 = '#b3b3b3'
                    else:
                        color_p2 = '#fff'
                        color_p1 = '#b3b3b3'

                    with tournament:
                        st.text('')
                        st.markdown(f"<h5 style='text-align: left;'>{tournament_name}</h5   >", unsafe_allow_html=True)
                        st.markdown(f"<h6 style='text-align: left;'>{surface}</h6>", unsafe_allow_html=True)
                        st.markdown(f"<div style='text-align: left;'>{date}", unsafe_allow_html=True)

                    with players:
                        pl1 = st.container()
                        pl2 = st.container()

                        with pl1:
                            st.markdown(f"<h4 style='text-align: left; color:{color_p1};'>{player}</h3>", unsafe_allow_html=True)

                        with pl2:
                            st.markdown("<div style='text-align: center;color:#7814ff;'>S</div>", unsafe_allow_html=True)
                            st.markdown(f"<h4 style='text-align: left;color:{color_p2};'>{player2}</h3>", unsafe_allow_html=True)

                    with result:
                        
                        if id_ == row['winner_id']:
                            if str.isnumeric(s1_p2_r):
                                if s1_p2_t == '-':
                                    s1_p2 = s1_p2_r
                                else:
                                    s1_p2 = s1_p2_r + f"<sup><sup> ({s1_p2_t}</sup></sup>"
                            else:
                                s1_p2 = '-'
                        if id_ == row['loser_id']:
                            if str.isnumeric(s1_p1_r):
                                if s1_p1_t == '-':
                                    s1_p1 = s1_p1_r
                                else:
                                    s1_p1 = s1_p1_r + f"<sup><sup> ({s1_p1_t}</sup></sup>"
                            else:
                                s1_p2 = '-'


                        if str.isnumeric(s2_p1_r):
                            if s2_p1_t == '-':
                                s2_p1 = s2_p1_r
                            else:
                                s2_p1 = s2_p1_r + f"<sup><sup> ({s2_p1_t}</sup></sup>"
                        else:
                            s2_p1 = '-'

                        if str.isnumeric(s2_p2_r):
                            if s2_p2_t == '-':
                                s2_p2 = s2_p2_r
                            else:
                                s2_p2 = s2_p2_r + f"<sup><sup> ({s2_p2_t}</sup></sup>"
                        else:
                            s2_p2 = '-'

                        if str.isnumeric(s3_p1_r):
                            if s3_p1_t == '-':
                                s3_p1 = s3_p1_r
                            else:
                                s3_p1 = s3_p1_r + f"<sup><sup> ({s3_p1_t}</sup></sup>"
                        else:
                            s3_p1 = '-'
                            
                        if str.isnumeric(s3_p2_r):
                            if s3_p2_t == '-':
                                s3_p2 = s3_p2_r
                            else:
                                s3_p2 = s3_p2_r + f"<sup><sup> ({s3_p2_t}</sup></sup>"
                        else:
                            s3_p2 = '-'

                        r1, r2, r3 = st.columns([3,3,3])   
                        with r1: 
                            pl1 = st.container()
                            pl2 = st.container()

                            with pl1:
                                st.markdown(f"<h4 style='text-align: left;color:{color_p1};'>{s1_p1}</h4>", unsafe_allow_html=True)

                            with pl2:
                                st.markdown("<div style='text-align: center;color:#7814ff;'>S</div>", unsafe_allow_html=True)
                                st.markdown(f"<h4 style='text-align: left;color:{color_p2};'>{s1_p2}</h4>", unsafe_allow_html=True)

                        with r2: 
                            pl1 = st.container()
                            pl2 = st.container()

                            with pl1:
                                st.markdown(f"<h4 style='text-align: left;color:{color_p1};'>{s2_p1}</h4>", unsafe_allow_html=True)

                            with pl2:
                                st.markdown("<div style='text-align: center;color:#7814ff;'>S</div>", unsafe_allow_html=True)
                                st.markdown(f"<h4 style='text-align: left;color:{color_p2};'>{s2_p2}</h4>", unsafe_allow_html=True)

                        with r3: 
                            pl1 = st.container()
                            pl2 = st.container()

                            with pl1:
                                st.markdown(f"<h4 style='text-align: left;color:{color_p1};'>{s3_p1}</h4>", unsafe_allow_html=True)

                            with pl2:
                                st.markdown("<div style='text-align: center;color:#7814ff;'>S</div>", unsafe_allow_html=True)
                                st.markdown(f"<h4 style='text-align: left;color:{color_p2};'>{s3_p2}</h4>", unsafe_allow_html=True)

                    st.write("")
                    st.divider()
                    st.write("")

            else:
                st.markdown(f"""<div style="text-align: center;">These players haven't face each other</div>""", unsafe_allow_html=True)

    else:
        st.write('')
        st.write('')
        st.markdown(f"""<div style="text-align: center;">Player selected not valid, choose another one</div>""", unsafe_allow_html=True)


    