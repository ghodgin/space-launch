import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns




def american_launch_data():
    launch_df = pd.read_csv("data/Space_Corrected.csv")

    cleaned_launch_df = launch_df.drop(['Unnamed: 0.1', 'Unnamed: 0'], axis=1)
    cleaned_launch_df['Date'] = cleaned_launch_df['Datum'].str[:16]
    cleaned_launch_df.drop(columns=['Datum'], inplace=True)
    cleaned_launch_df['Date'] = pd.to_datetime(cleaned_launch_df['Date'], format='%a %b %d, %Y')

    cutoff_date = pd.to_datetime('2000-01-01') ## Turn of the millenia, optimal for showing the growth in american space launches

    combined_names = ['SpaceX' , 'NASA', 'ULA']
    combined_nasa_spacex_ula = cleaned_launch_df[cleaned_launch_df['Company Name'].str.contains('|'.join(combined_names))]
    america_rahh_df = combined_nasa_spacex_ula[combined_nasa_spacex_ula['Date'] > cutoff_date]
    launch_counts = america_rahh_df.groupby(['Date', 'Company Name']).size().reset_index(name='Launch Count')
    grouped_counts = launch_counts.groupby(['Company Name', launch_counts['Date'].dt.year])['Launch Count'].sum().reset_index()
    
    
    plt.figure(figsize=(12,6))
    sns.barplot(x='Date', y='Launch Count', hue='Company Name', data=grouped_counts, palette='Paired')
    plt.title('Number of Launches over time by US organizations / companies')
    plt.xlabel('Date')
    plt.ylabel('Number of launches')
    plt.xticks(rotation=45, size=9)
    plt.tight_layout()
    
    return plt

american_launch_data().show()

