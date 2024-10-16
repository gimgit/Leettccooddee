import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    activity = activity[['player_id', 'event_date']]
    activity = activity.groupby(by=['player_id'], as_index=False)['event_date'].min()
    activity = activity.rename(columns={'event_date': 'first_login'})
    return activity