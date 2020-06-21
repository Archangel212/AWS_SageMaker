import pandas as pd
def trim_csv(csv_path,last_epoch):
  loss_df = pd.read_csv(csv_path, index_col=None)
  loss_df = loss_df.loc[loss_df["epoch"] <= last_epoch]
  loss_df.to_csv(csv_path,mode='w', index=False)
  print("csv trimed at epoch > %d" % (last_epoch))
