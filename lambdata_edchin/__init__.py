import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

VERSION=1.0

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

def train_validation_test_split(
    X, y, train_size=0.8, val_size=0.1, test_size=0.1, 
    random_state=None, shuffle=True):
        
    assert train_size + val_size + test_size == 1
    
    X_train_val, X_test, y_train_val, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state, shuffle=shuffle)
    
    X_train, X_val, y_train, y_val = train_test_split(
        X_train_val, y_train_val, test_size=val_size/(train_size+val_size), 
        random_state=random_state, shuffle=shuffle)
    
    return X_train, X_val, X_test, y_train, y_val, y_test