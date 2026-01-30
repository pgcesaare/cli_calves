import pandas as pd
from utils.header import normalize_headers

def process_df(df):

      df['week_range'] = (df["date_in"].dt.to_period("W-SUN").astype(str))
      
      #filtering by weeks with 5 days or more worth of placements
      week_counts = df.groupby('week_range')['date_in'].nunique()
      complete_weeks = week_counts[week_counts >= 5].index
      
      df = df[df['week_range'].isin(complete_weeks)]

      return df

def format_week(df):
      df['week_range'] = df['week_range'].str.replace('/', ' - ')
      return df

def get_avg_per_week():

      #processing dataframe
      df = normalize_headers()
      df = process_df(df)

      #logic
      df = df[['breed', 'week_range']]
      df = df.groupby('week_range')['breed'].size().reset_index(name='total_calves')
      avg = df['total_calves'].mean()

      #formatting week_range
      df = format_week(df)

      return df, avg

def get_avg_per_day():

      #processing dataframe
      df = normalize_headers()
      df = process_df(df)

      #logic
      last_two_weeks = (df['week_range'].sort_values().unique()[-2:])
      df = df[df['week_range'].isin(last_two_weeks)]
      df['date_in'] = df['date_in'].dt.date   
      df = df.groupby(['week_range', 'date_in']).size().reset_index(name="total_calves")
      avg = df['total_calves'].mean()

      #formatting week_range
      df = format_week(df)

      return df, avg

