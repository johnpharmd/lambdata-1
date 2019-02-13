#______ Create a csv file for submission to Kaggle ___________
def create_kaggle_submission(pred_array,x_test_df,dest_url):
  pred_df=pd.DataFrame(pred_array,columns=['status_group'])
  ids=pd.DataFrame(x_test_df.id,columns=['id'])
  ids=ids.astype('int32')
  submit_df=pd.concat([ids, pred_df], axis=1)
  submit_df.to_csv(dest_url, index=False, header=['id','status_group'])
  return

#______ Split model data into Train/Val/Test sets ___________
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