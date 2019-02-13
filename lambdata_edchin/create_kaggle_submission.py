#______ Create a csv file for submission to Kaggle ___________
def create_kaggle_submission(pred_array,x_test_df,dest_url):
  pred_df=pandas.DataFrame(pred_array,columns=['status_group'])
  ids=pandas.DataFrame(x_test_df.id,columns=['id'])
  ids=ids.astype('int32')
  submit_df=pandas.concat([ids, pred_df], axis=1)
  submit_df.to_csv(dest_url, index=False, header=['id','status_group'])
  return