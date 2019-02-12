VERSION=1.5

import pandas as pd

def variance(results):
  #calculate the variance : the average of the squared differences from the mean.
  # calculate mean
  m = sum(results) / len(results)
  # calculate variance using a list comprehension
  return sum((xi - m) ** 2 for xi in results) / len(results)

def create_submission(pred_array,X_test_df,dest_url):
  pred_df=pd.DataFrame(pred_array,columns=['status_group'])
  pump_ids=pd.DataFrame(X_test_df.id,columns=['id'])
  pump_ids = pump_ids.astype('int32')
  submit_df=pd.concat([pump_ids, pred_df], axis=1)
  submit_df.to_csv(dest_url, index=False, header=['id','status_group'])
  return