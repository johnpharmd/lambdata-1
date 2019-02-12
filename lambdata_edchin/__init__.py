VERSION=1.0

import pandas as pd

def variance(results):
  #calculate the variance : the average of the squared differences from the mean.
  # calculate mean
  me_an = sum(results) / len(results)
  # calculate variance using a list comprehension
  return sum((x - me_an) ** 2 for x in results) / len(results)

def create_submission(pred_array,X_test_df,dest_url):
  pred_df=pd.DataFrame(pred_array,columns=['status_group'])
  pump_ids=pd.DataFrame(X_test_df.id,columns=['id'])
  pump_ids = pump_ids.astype('int32')
  submit_df=pd.concat([pump_ids, pred_df], axis=1)
  submit_df.to_csv(dest_url, index=False, header=['id','status_group'])
  return