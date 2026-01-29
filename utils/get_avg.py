import pandas as pd
from context.context import data as data_file

def get_avg_per_week():
      
      df = data_file.get()
      df['week_range'] = (df["Date In"].dt.to_period("W-SUN").astype(str))
      
      #filtering by weeks with 5 days or more worth of placements
      week_counts = df.groupby('week_range')['Date In'].nunique()
      complete_weeks = week_counts[week_counts >= 5].index
      complete_weeks
      
      df = df[df['week_range'].isin(complete_weeks)]

      df = df[['Breed', 'week_range']]

      df = df.groupby('week_range')['Breed'].size().reset_index(name='total_calves')

      avg = df['total_calves'].mean()

      return df, avg

def get_avg_per_day():

      df = data_file.get()
      df['week_range'] = (df["Date In"].dt.to_period("W-SUN").astype(str))

      #filtering by weeks with 5 days or more worth of placements
      week_counts = df.groupby('week_range')['Date In'].nunique()
      complete_weeks = week_counts[week_counts >= 5].index
      complete_weeks

      df = df[df['week_range'].isin(complete_weeks)]

      last_two_weeks = (df['week_range'].sort_values().unique()[-2:])
      
      df = df[df['week_range'].isin(last_two_weeks)]

      df = df.rename(columns={
      "Date In": "date_in"
      })
      
      df = df.groupby(['week_range', 'date_in']).size().reset_index(name="total_calves")

      avg = df['total_calves'].mean()

      return df, avg