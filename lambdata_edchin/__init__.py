VERSION=1.3

import pandas as pd

#___ Variance:average of the squared differences from the mean____
def variance(numbers):
    #___ calculate mean________________
    me_an=sum(numbers) / len(numbers)
    #____calculate variance using a list comprehension__________
    return sum((x - me_an) ** 2 for x in numbers) / len(numbers)

#______ Create a csv file for submission to Kaggle ___________
def create_kaggle_submission(pred_array,x_test_df,dest_url):
  pred_df=pd.DataFrame(pred_array,columns=['status_group'])
  ids=pd.DataFrame(x_test_df.id,columns=['id'])
  ids=ids.astype('int32')
  submit_df=pd.concat([ids, pred_df], axis=1)
  submit_df.to_csv(dest_url, index=False, header=['id','status_group'])
  return