VERSION=1.0

import pandas as pd

def variance(numbers):
  #calculate the variance : the average of the squared differences from the mean.
  # calculate mean
  me_an = sum(numbers) / len(numbers)
  # calculate variance using a list comprehension
  return sum((x - me_an) ** 2 for x in numbers) / len(numbers)

def create_submission(pred_array,x_test_df,dest_url):
  pred_df=pd.DataFrame(pred_array,columns=['status_group'])
  ids=pd.DataFrame(x_test_df.id,columns=['id'])
  ids = ids.astype('int32')
  submit_df=pd.concat([ids, pred_df], axis=1)
  submit_df.to_csv(dest_url, index=False, header=['id','status_group'])
  return