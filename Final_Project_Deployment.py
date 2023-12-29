#Import package
import pickle
import streamlit as st

#Import data
pickle_in = open('model.pkl' ,'rb') 
classifier = pickle.load(pickle_in)

#Data Preprocessing
def prediction(xg,xga,venue_code,sh,sot,poss,dist,attendance,fk,pkatt,opp_code):
    if opp_code == 'Arsenal':
        opp_code = 0
    elif opp_code == 'Aston Villa':
        opp_code = 1
    elif opp_code == 'Brentford':
        opp_code = 2
    elif opp_code == 'Brighton':
        opp_code = 3
    elif opp_code == 'Burnley':
        opp_code = 4
    elif opp_code == 'Chelsea':
        opp_code = 5
    elif opp_code == 'Crystal Palace':
        opp_code = 6
    elif opp_code == 'Everton':
        opp_code = 7
    elif opp_code == 'Fulham':
        opp_code = 8
    elif opp_code == 'Leeds United':
        opp_code = 9
    elif opp_code == 'Leicester City':
        opp_code = 10
    elif opp_code == 'Liverpool':
        opp_code = 11
    elif opp_code == 'Manchester City':
        opp_code = 12
    elif opp_code == 'Manchester Utd':
        opp_code = 13
    elif opp_code == 'Newcastle Utd':
        opp_code = 14
    elif opp_code == 'Norwich City':
        opp_code = 15
    elif opp_code == 'Sheffield Utd':
        opp_code = 16
    elif opp_code == 'Southampton':
        opp_code = 17
    elif opp_code == 'Tottenham':
        opp_code = 18
    elif opp_code == 'Watford':
        opp_code = 19
    elif opp_code == 'West Brom':
        opp_code = 20
    elif opp_code == 'West Ham':
        opp_code = 21
    elif opp_code == 'Wolves':
        opp_code = 22
   

    if venue_code =='Home':
        venue_code = 1
    elif venue_code == 'Away':
        venue_code = 2

    #Making Prediction
    prediction=classifier.predict([[xg,xga,venue_code,sh,sot,poss,dist,attendance,fk,pkatt,opp_code]])

    if prediction==0:
        pred = 'Lose'
    elif prediction ==1:
        pred = 'Draw'
    elif prediction ==2:
        pred = 'Win'
    return pred


#Membuat Feature
st.title("Streamlit Premier League Analyzer using ML") 
xg=st.slider('Expected Goal (Evaluasi seberapa besar kemungkinan tembakan akan menghasilkan gol)',0.0,0.5,1.0)
xga=st.slider('Expected Goal Against (Evaluasi seberapa besar kemungkinan tembakan lawan akan menghasilkan gol)',0.0,0.5,1.0)
venue_code=st.select_slider('Match Dilakukan pada Stadiun Tim Atau Stadiun Lawan',['Home','Away'])
sh=st.number_input('Shot (Banyaknya Jumlah total tembakan)',0,10)
sot=st.number_input('Shot On Target (Banyaknya Jumlah total tembakan yang langsung mengancam gawang lawan)',0,10)
poss=st.number_input('Possession(seberapa banyak tim mengontrol bola selama waktu pertandingan)(%)',0,100)
dist=st.number_input('jarak total yang ditempuh oleh pemain atau tim selama pertandingan (km)',0,100)
attendance=st.number_input('Jumlah penonton pada stadiun',0,100000)
fk=st.number_input('Jumlah tendangan bebas oleh tim',0,30)
pkatt=st.number_input('jumlah Upaya Eksekusi Penalti',0,20)
opp_code=st.selectbox('Pilih Lawan',['Arsenal','Aston Villa','Brentford','Brighton','Burnley','Chelsea','Crystal Palace','Everton','Fulham','Leeds United','Leicester City','Liverpool','Manchester City','Manchester Utd','Newcastle Utd'
 ,'Norwich City' ,'Sheffield Utd' ,'Southampton' ,'Tottenham' ,'Watford'
 'West Brom' ,'West Ham', 'Wolves'])

#Membuat Button Prediction
if st.button('Prediksi hasil'):
    result = prediction(xg,xga,venue_code,sh,sot,poss,dist,attendance,fk,pkatt,opp_code)
    st.success(f'Hasilnya adalah {result}')





