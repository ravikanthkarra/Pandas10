import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    result = actor_director.groupby(['actor_id', 'director_id']).size().reset_index(name='cnt')
    result = result[(result['cnt'] > 2)]
    # print((result))
    return result[['actor_id', 'director_id']]
