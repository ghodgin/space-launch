import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def american_launch_data():

    launch_df = pd.read_csv("data/Space_Corrected.csv")

    ##Cleans the launch data and changes the date column to datetime format
    cleaned_launch_df = launch_df.drop(['Unnamed: 0.1', 'Unnamed: 0'], axis=1)
    cleaned_launch_df['Date'] = cleaned_launch_df['Datum'].str[:16]
    cleaned_launch_df.drop(columns=['Datum'], inplace=True)
    cleaned_launch_df['Date'] = pd.to_datetime(cleaned_launch_df['Date'], format='%a %b %d, %Y')
    
    ## Turn of the millenia, optimal for showing the growth in american space launches
    cutoff_date = pd.to_datetime('2000-01-01') 

    ## Takes the above DF and counts launches per organization
    combined_names = ['SpaceX' , 'NASA', 'ULA']
    combined_nasa_spacex_ula = cleaned_launch_df[cleaned_launch_df['Company Name'].str.contains('|'.join(combined_names))]
    america_rahh_df = combined_nasa_spacex_ula[combined_nasa_spacex_ula['Date'] > cutoff_date]
    launch_counts = america_rahh_df.groupby(['Date', 'Company Name']).size().reset_index(name='Launch Count')
    grouped_counts = launch_counts.groupby(['Company Name', launch_counts['Date'].dt.year])['Launch Count'].sum().reset_index()
    
    ## Plots the 'grouped_counts' df
    plt.figure(figsize=(12,6))
    sns.barplot(x='Date', y='Launch Count', hue='Company Name', data=grouped_counts, palette='Paired')
    plt.title('Number of Launches over time by US organizations / companies')
    plt.xlabel('Date')
    plt.ylabel('Number of launches')
    plt.xticks(rotation=45, size=9)
    plt.tight_layout()
    
    return plt

american_launch_data().show()



def included_russia():

    launch_df = pd.read_csv("data/Space_Corrected.csv")
    cleaned_launch_df = launch_df.drop(['Unnamed: 0.1', 'Unnamed: 0'], axis=1)
    cleaned_launch_df['Date'] = cleaned_launch_df['Datum'].str[:16]
    cleaned_launch_df.drop(columns=['Datum'], inplace=True)
    cleaned_launch_df['Date'] = pd.to_datetime(cleaned_launch_df['Date'], format='%a %b %d, %Y')

    cutoff_date = pd.to_datetime('2000-01-01')

    ## Combines russian agencies for comparison
    combined_names_usa_ussr = ['SpaceX' , 'NASA', 'ULA', 'Roscosmos', 'RVSN USSR']
    combined_usa_ussr = cleaned_launch_df[cleaned_launch_df['Company Name'].str.contains('|'.join(combined_names_usa_ussr))]
    updated_launch_counts = combined_usa_ussr.groupby(['Date', 'Company Name']).size().reset_index(name='Launch Count')
    comparative_df = updated_launch_counts[updated_launch_counts['Date'] > cutoff_date]
    updated_groups = comparative_df.groupby(['Company Name', comparative_df['Date'].dt.year])['Launch Count'].sum().reset_index()

    plt.figure(figsize=(12,6))
    sns.barplot(x='Date', y='Launch Count', hue='Company Name', data=updated_groups, palette='Paired')
    plt.title('Number of Launches over time by organization')
    plt.xlabel('Date')
    plt.ylabel('Number of launches')
    plt.xticks(rotation=45, size=10)
    plt.tight_layout()

    return plt

included_russia().show()


def nasa_vs_ussr():

    launch_df = pd.read_csv("data/Space_Corrected.csv")

    to_2000 = pd.to_datetime('2000-01-01')

    cleaned_launch_df = launch_df.drop(['Unnamed: 0.1', 'Unnamed: 0'], axis=1)
    cleaned_launch_df['Date'] = cleaned_launch_df['Datum'].str[:16]
    cleaned_launch_df.drop(columns=['Datum'], inplace=True)
    cleaned_launch_df['Date'] = pd.to_datetime(cleaned_launch_df['Date'], format='%a %b %d, %Y')

    russia_and_nasa_names = ['NASA' , 'RVSN USSR']
    russia_and_nasa = cleaned_launch_df[cleaned_launch_df['Company Name'].str.contains('|'.join(russia_and_nasa_names))]
    russia_and_nasa[russia_and_nasa['Date'] > to_2000]

    test = russia_and_nasa.groupby(['Date', 'Company Name']).size().reset_index(name='Launch Count')

    comparative_usa_russia = test.groupby(['Company Name', test['Date'].dt.year])['Launch Count'].sum().reset_index()
    
    plt.figure(figsize=(17,6))
    sns.barplot(x='Date', y='Launch Count', hue='Company Name', data=comparative_usa_russia, palette='Paired')
    plt.title('Number of Launches over time from NASA and the USSR')
    plt.xlabel('Date')
    plt.ylabel('Number of launches')
    plt.xticks(rotation=90, size=10)
    ## plt.arrow(x=40.5, y=20, dx =-3, dy=-3, width=.8, head_width=2)
    plt.annotate('Fall of the Soviet Union', xy=[35, 15], xytext=[38, 40], arrowprops=dict(color="black"))
    plt.tight_layout()

    return plt

nasa_vs_ussr().show()