import streamlit as st
import pandas as pd
import numpy as np
import re

import plotly.graph_objects as go


st.set_page_config(layout="wide")
df=pd.read_csv('countries of the world.csv')
df.dropna()


for i in range(len(df)):
    for j in range(len(df.columns)):
        value = df.loc[i, 'Region']
        if re.search('AFRICA', value, re.IGNORECASE):
            df.loc[i, 'Region'] = 'AFRICA'
        elif re.search('ASIA', value, re.IGNORECASE):
            df.loc[i, 'Region'] = 'ASIA'
        elif re.search('EUROPE', value, re.IGNORECASE):
            df.loc[i, 'Region'] = 'EUROPE'
        elif re.search('AMERICA', value, re.IGNORECASE):
            df.loc[i, 'Region'] = 'AMERICA'



list_regions=df["Region"].unique()

selected_continent=st.selectbox(label='Select country', options=list_regions)


country_name_list=[]
country_pop_list=[]



for i in range(len(df)):
    for j in range(len(df.columns)):
        if(df.loc[i,'Region']==selected_continent):
            country_name_list.append(df.loc[i,'Country'])
            country_pop_list.append(df.loc[i,'Population'])



dict_pop={}
for i in range(len(country_name_list)):
    dict_pop[country_name_list[i]]=country_pop_list[i]

sorted_dict = dict(sorted(dict_pop.items(), key=lambda item: item[1],reverse=True))


country_name_list_jr=[]
country_pop_list_jr=[]

if(len(sorted_dict)>=6):
    count=0
    for key in sorted_dict:
        if count==6:
            break

        country_name_list_jr.append(key)
        country_pop_list_jr.append(sorted_dict[key])
        count+=1
elif(len(sorted_dict)<6):
    for key in sorted_dict:

        country_name_list_jr.append(key)
        country_pop_list_jr.append(sorted_dict[key])


country_name_list=country_name_list_jr
country_pop_list=country_pop_list_jr


fig_pop = go.Figure(data=[go.Bar(x=country_name_list, y=country_pop_list)])
fig_pop.update_layout(title_text='Population', xaxis_title='Countries', yaxis_title='Population',width=600,height=400)





                   ########### sorting based on literracy ##########

dict_literaccy={}
for i in range(len(df)):
    if(df.loc[i,'Country'] in country_name_list):

        string_literacy=df.loc[i,'Literacy (%)']
        string_literacy=string_literacy.split(',')
        string_literacy='.'.join(string_literacy)
        dict_literaccy[df.loc[i,'Country']]=string_literacy

country_name_list_pop_literacy=[]
literacy_name_list_pop_literacy=[]

dict_literaccy = dict(sorted(dict_literaccy.items(), key=lambda item: item[1],reverse=True))

for key in dict_literaccy:
    country_name_list_pop_literacy.append(key)
    literacy_name_list_pop_literacy.append(dict_literaccy[key])



fig_pop_sort_literacy = go.Figure(data=[go.Bar(x=country_name_list_pop_literacy, y=literacy_name_list_pop_literacy)])
fig_pop_sort_literacy.update_layout(title_text='By Literacy', xaxis_title='Countries', yaxis_title='Literacy %',width=600,height=400)




                              ####### sorting based on mobile phone ##########


dict_pop_phone_user={}

for i in range(len(df)):
    for j in range(len(df.columns)):

        if(df.loc[i,'Country'] in country_name_list):
            string_phone=df.loc[i,'Phones (per 1000)']
            split_string_phone=string_phone.split(',')
            string_phone=split_string_phone[0]+split_string_phone[1]
            dict_pop_phone_user[df.loc[i,'Country']]=string_phone

dict_pop_phone_user = dict(sorted(dict_pop_phone_user.items(), key=lambda item: item[1],reverse=True))



pop_phone_name=[]
pop_phone_count=[]



for key in dict_pop_phone_user:
    pop_phone_name.append(key)
    pop_phone_count.append(dict_pop_phone_user[key])


fig_pop_sort_phone = go.Figure(data=[go.Bar(x=pop_phone_name, y=pop_phone_count)])
fig_pop_sort_phone.update_layout(title_text='By Phone users', xaxis_title='Countries', yaxis_title='%age phone users',width=600,height=400)



####################################################### 2 GDP per capita #####################################

dict_percapita={}

for i in range(len(df)):
    for j in range(len(df.columns)):
        if(df.loc[i,'Region']==selected_continent):
            dict_percapita[df.loc[i,'Country']]=df.loc[i,'GDP ($ per capita)']

dict_percapita = dict(sorted(dict_percapita.items(), key=lambda item: item[1],reverse=True))

gdp_name_list=[]
gdp_gdp_list=[]

if(len(dict_percapita)>=6):
    count=0
    for key in dict_percapita:
        if count==6:
            break

        gdp_name_list.append(key)
        gdp_gdp_list.append(dict_percapita[key])
        count+=1
elif(len(dict_percapita)<6):
    for key in dict_percapita:

        gdp_name_list.append(key)
        gdp_gdp_list.append(dict_percapita[key])


fig_gdp_original = go.Figure(data=[go.Bar(x=gdp_name_list, y=gdp_gdp_list)])
fig_gdp_original.update_layout(title_text='Bar Chart Example', xaxis_title='Categories', yaxis_title='Values',width=600,height=400)


                                ############### Agriculture ###################


list_gdp_agriculture_name=[]
list_gdp_agriculture=[]

for i in range(len(df)):
    if (df.loc[i, 'Country'] in gdp_name_list):
        # dict_percapita[df.loc[i,'Country']]=df.loc[i,'GDP ($ per capita)']
        string_agri = df.loc[i, 'Agriculture']
        list_agri = string_agri.split(",")
        string_agri = ".".join(list_agri)

        string_agri=str(float(string_agri)*100)

        list_gdp_agriculture_name.append(df.loc[i, 'Country'])
        list_gdp_agriculture.append(string_agri)


fig_gdp_agriculture = go.Figure(data=[go.Bar(x=list_gdp_agriculture_name, y=list_gdp_agriculture)])
fig_gdp_agriculture.update_layout(title_text='Bar Chart Example', xaxis_title='Categories', yaxis_title='Values',width=600,height=400)


                                    ######### Industry #########


list_gdp_industry_name=[]
list_gdp_industry=[]


for i in range(len(df)):
    if (df.loc[i, 'Country'] in gdp_name_list):
        # dict_percapita[df.loc[i,'Country']]=df.loc[i,'GDP ($ per capita)']
        string_industry = df.loc[i, 'Industry']
        list_agri = string_industry.split(",")
        string_industry = ".".join(list_agri)
        string_industry=str(float(string_industry)*100)

        list_gdp_industry_name.append(df.loc[i, 'Country'])
        list_gdp_industry.append(string_industry)

fig_gdp_industry = go.Figure(data=[go.Bar(x=list_gdp_industry_name, y=list_gdp_industry)])
fig_gdp_industry.update_layout(title_text='Bar Chart Example', xaxis_title='Categories', yaxis_title='Values',width=600,height=400)



                                        ############# Service ##############


list_gdp_service_name=[]
list_gdp_service=[]


for i in range(len(df)):
    if (df.loc[i, 'Country'] in gdp_name_list):

        string_service = df.loc[i, 'Service']
        list_agri = string_service.split(",")
        string_service = ".".join(list_agri)
        string_service=str(float(string_service)*100)

        list_gdp_service_name.append(df.loc[i, 'Country'])
        list_gdp_service.append(string_service)

fig_gdp_service = go.Figure(data=[go.Bar(x=list_gdp_service_name, y=list_gdp_service)])
fig_gdp_service.update_layout(title_text='Bar Chart Example', xaxis_title='Categories', yaxis_title='Values',width=600,height=400)



####################### $$$$$$$$$$$$$$$$$$$$$ ################ $$$$$$$$$$$$$$$$$$$$
df_gdp_growth = pd.read_csv('countries_gdp_growth.csv')
gdp_growth_countries = []
dist_country_gdp_growth = {}


country_list_for_gdp_growth = []

for i in range(len(df)):
    if df.loc[i, 'Region'] == selected_continent:
        country_list_for_gdp_growth.append(df.loc[i, 'Country'].strip())

for i in range(len(df_gdp_growth)):
    country_name = df_gdp_growth.loc[i, 'Country Name'].strip()


    if country_name in country_list_for_gdp_growth:
        dist_country_gdp_growth[country_name] = df_gdp_growth.loc[i, '2022 [YR2022]']



dist_country_gdp_growth= dict(sorted(dist_country_gdp_growth.items(), key=lambda item: item[1],reverse=True))


# st.write(dist_country_gdp_growth)
count=0
top_three_gdp_name=[]
for i in dist_country_gdp_growth:
    if count<3:
        top_three_gdp_name.append(i)
    count+=1

# st.write(top_three_gdp_name)

first_gdp_rate=[]
second_gdp_rate=[]
third_gdp_rate=[]

list_of_column=['2016 [YR2016]','2017 [YR2017]','2018 [YR2018]','2019 [YR2019]','2020 [YR2020]','2021 [YR2021]','2022 [YR2022]']

dict_title_gdp_growth={}

for i in range(len(df_gdp_growth)):
    if(df_gdp_growth.loc[i,'Country Name'].strip() in top_three_gdp_name):
        for j in list_of_column:
            if(len(first_gdp_rate)!=7 and len(second_gdp_rate)==0 and len(third_gdp_rate)==0):
                first_gdp_rate.append(str(df_gdp_growth.loc[i,j]))
                dict_title_gdp_growth[str(df_gdp_growth.loc[i,j])]=df_gdp_growth.loc[i,'Country Name'].strip()
            elif(len(second_gdp_rate)!=7 and len(third_gdp_rate)==0 and len(first_gdp_rate)==7):
                second_gdp_rate.append(str(df_gdp_growth.loc[i,j]))
                dict_title_gdp_growth[str(df_gdp_growth.loc[i, j])]=df_gdp_growth.loc[i, 'Country Name'].strip()
            elif(len(third_gdp_rate)!=7 and len(first_gdp_rate)==7 and len(second_gdp_rate)==7):
                third_gdp_rate.append(str(df_gdp_growth.loc[i,j]))
                dict_title_gdp_growth[str(df_gdp_growth.loc[i, j])]=df_gdp_growth.loc[i, 'Country Name'].strip()
        # dict_title_gdp_growth[]


dict_last_gdp_checker={}
dict_last_gdp_checker[first_gdp_rate[len(first_gdp_rate)-1]]=first_gdp_rate
dict_last_gdp_checker[second_gdp_rate[len(first_gdp_rate)-1]]=second_gdp_rate
dict_last_gdp_checker[third_gdp_rate[len(first_gdp_rate)-1]]=third_gdp_rate

dict_last_gdp_checker=dict(sorted(dict_last_gdp_checker.items(), key=lambda item: item[0],reverse=True))

random_list=[]
for key in dict_last_gdp_checker:
    random_list.append(dict_last_gdp_checker[key])

third_gdp_rate=random_list[2]
second_gdp_rate=random_list[1]
first_gdp_rate=random_list[0]

# st.write(first_gdp_rate)
# st.write(second_gdp_rate)
# st.write(third_gdp_rate)


                    ###############  inka graphs #################


data_gdp_first = {
    'Date': ['2016','2017','2018','2019','2020','2021','2022'],
    'Value': first_gdp_rate
}
df_first = pd.DataFrame(data_gdp_first)
# st.title('Line Chart Example')
title_of_fastest=dict_title_gdp_growth[first_gdp_rate[len(first_gdp_rate)-1]]

# st.title(dict_title_gdp_growth[first_gdp_rate[len(first_gdp_rate)-1]])
fig_gdp_first = go.Figure(data=go.Scatter(x=df_first['Date'], y=df_first['Value'], mode='lines'))
fig_gdp_first.update_layout(
    xaxis_title='Date',
    yaxis_title='Value',
    width=600,
    height=400
)
# st.plotly_chart(fig_gdp_first)

data_gdp_second = {
    'Date': ['2016','2017','2018','2019','2020','2021','2022'],
    'Value': second_gdp_rate
}
df_second = pd.DataFrame(data_gdp_second)
# st.title('Line Chart Example')
title_of_second_fastest=dict_title_gdp_growth[second_gdp_rate[len(second_gdp_rate)-1]]

# st.title(dict_title_gdp_growth[second_gdp_rate[len(second_gdp_rate)-1]])
fig_gdp_second = go.Figure(data=go.Scatter(x=df_second['Date'], y=df_second['Value'], mode='lines'))
fig_gdp_second.update_layout(
    xaxis_title='Date',
    yaxis_title='Value',
    width=600,
    height=400
)
# st.plotly_chart(fig_gdp_second)


data_gdp_third = {
    'Date': ['2016','2017','2018','2019','2020','2021','2022'],
    'Value': third_gdp_rate
}
df_third = pd.DataFrame(data_gdp_third)
# st.title('Line Chart Example')

title_of_third_fastest=dict_title_gdp_growth[third_gdp_rate[len(third_gdp_rate)-1]]

# st.title(dict_title_gdp_growth[third_gdp_rate[len(third_gdp_rate)-1]])
fig_gdp_third = go.Figure(data=go.Scatter(x=df_third['Date'], y=df_third['Value'], mode='lines'))
fig_gdp_third.update_layout(
    xaxis_title='Date',
    yaxis_title='Value',
    width=600,
    height=400
)

############################################################################################################
####################################################### last one ###########################################
############################################################################################################


                        ########## Area #########
top_six_arable=[]
dict_area={}
for i in range(len(df)):
    if(df.loc[i,'Region']==selected_continent):
        dict_area[df.loc[i,'Country']]=df.loc[i,'Area (sq. mi.)']
dict_area=dict(sorted(dict_area.items(), key=lambda item: item[1],reverse=True))
# st.write(dict_area)
count =0
list_name_area=[]
list_area_area=[]
for key in dict_area:
    if(count<6):
        list_name_area.append(key)
        list_area_area.append(dict_area[key])
        count+=1
fig_area = go.Figure(data=[go.Bar(x=list_name_area, y=list_area_area)])
fig_area.update_layout(title_text='Land Area', xaxis_title='Countries', yaxis_title='Area',width=600,height=400)
# st.plotly_chart(fig_area)

             ########### Crops ###########
dict_area_crops={}

for i in range(len(df)):
    if df.loc[i,'Country'] in list_name_area:
        crop_area=df.loc[i,'Crops (%)']
        crop_area=crop_area.split(',')
        crop_area=".".join(crop_area)
        dict_area_crops[df.loc[i,'Country']]=crop_area


dict_area_crops=dict(sorted(dict_area_crops.items(), key=lambda item: item[1],reverse=True))
list_crop_areas=[]
list_crop_areas_names=[]
for key in dict_area_crops:
    list_crop_areas.append(dict_area_crops[key])
    list_crop_areas_names.append(key)



# st.write(dict_area_crops)
fig_area_crops = go.Figure(data=[go.Bar(x=list_crop_areas_names, y=list_crop_areas)])
fig_area_crops.update_layout(title_text='Crop Area', xaxis_title='Countries', yaxis_title='Area',width=600,height=400)

# st.plotly_chart(fig_area_crops)




##################################################################################################################################
#############################################    PLACEHOLDER FOR POPULATION     ##################################################
##################################################################################################################################

place_holder = fig_pop
place_holder_plotly=None


gdp_place_holder=fig_gdp_original


place_holder_gdp_growth_rate=fig_gdp_first
place_holder_gdp_growth_rate_title=title_of_fastest

# Initialize the figure placeholder
# place_holder = fig_pop

def pop_sort_phone():
    global place_holder
    place_holder=None
    global place_holder_plotly
    place_holder_plotly=fig_pop_sort_phone
def pop_sort_literacy():
    # Update the placeholder when the button is clicked
    global place_holder
    place_holder = fig_pop_sort_literacy
def pop_original():
    global place_holder
    place_holder=fig_pop
    global place_holder_plotly
    place_holder_plotly=None

def fastest_gdp_growth_function():
    global place_holder_gdp_growth_rate
    place_holder_gdp_growth_rate=fig_gdp_first

    global place_holder_gdp_growth_rate_title
    place_holder_gdp_growth_rate_title=title_of_fastest

def second_gdp_growth_rate():
    global place_holder_gdp_growth_rate
    place_holder_gdp_growth_rate=fig_gdp_second

    global place_holder_gdp_growth_rate_title
    place_holder_gdp_growth_rate_title = title_of_second_fastest


def third_gdp_growth_rate():
    global place_holder_gdp_growth_rate
    place_holder_gdp_growth_rate=fig_gdp_third

    global place_holder_gdp_growth_rate_title
    place_holder_gdp_growth_rate_title = title_of_third_fastest


# Create two columns
col1, col2 = st.columns(2, gap='small')

with col1:
    st.header("Population")
    col11, col12,col13 = st.columns(3, gap='small')

    with col11:
        # Check if the button is clicked
        if st.button("Sort by literacy"):
            pop_sort_literacy()

    with col12:
        if st.button("Sort by phone users"):
            pop_sort_phone()

    with col13:
        if(st.button("original")):
            pop_original()



    # Display the placeholder figure
    if place_holder:
        # st.pyplot(place_holder)
        st.plotly_chart(place_holder)
    if place_holder_plotly:
        st.plotly_chart(place_holder_plotly)


###################################################################################################################
#################################################### Place holder for gdp growth ##################################
###################################################################################################################

    st.header("GDP growth rate")
    col31, col32,col33 = st.columns(3, gap='small')
    with col31:
        # Check if the button is clicked
        if st.button("fastest growing economy"):
            fastest_gdp_growth_function()
    with col32:
        if st.button("second fastest growing eco"):
            second_gdp_growth_rate()
    with col33:
        if st.button("Third fastest growing eco"):
            third_gdp_growth_rate()

    st.title(place_holder_gdp_growth_rate_title)
    st.plotly_chart(place_holder_gdp_growth_rate)




##################################################################################################################################
############################################################# PLACEHOLDER FOR GDP PER CAPITAL ####################################
##################################################################################################################################

place_holder_gdp=fig_gdp_original
place_holder_area=fig_area
# place_holder_crop_area=fig_area_crops

def gdp_sort_agriculture():
    global place_holder_gdp
    place_holder_gdp=fig_gdp_agriculture


def gdp_sort_industry():
    global place_holder_gdp
    place_holder_gdp=fig_gdp_industry


def gdp_sort_service():
    global place_holder_gdp
    place_holder_gdp=fig_gdp_service

def gdp_original():
    global place_holder_gdp
    place_holder_gdp=fig_gdp_original

def crops_field_area():
    global place_holder_area
    place_holder_area=fig_area_crops

def land_area():
    global place_holder_area
    place_holder_area=fig_area


with col2:
    st.header("GDP per capital")
    col21, col22, col23 ,col24= st.columns(4, gap='small')

    with col21:
        # Check if the button is clicked
        if st.button("Sort by Agriculture"):
            gdp_sort_agriculture()

    with col22:
        if st.button("Sort by Industry"):
            gdp_sort_industry()

    with col23:
        if (st.button("Sort by Service")):
            gdp_sort_service()
    with col24:
        if (st.button("original(gdp per capital)")):
            gdp_original()


    st.plotly_chart(place_holder_gdp)

    st.header("Land Area")
    col41, col42 = st.columns(2, gap='small')

    with col41:
        # Check if the button is clicked
        if st.button("By Crops field area"):
            crops_field_area()

    with col42:
        if st.button("Land Area"):
            land_area()

    st.plotly_chart(place_holder_area)



