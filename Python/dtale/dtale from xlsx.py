import pandas as pd
import dtale

data = pd.read_excel("YOUR_FILE_PATH.xlsx") 
d= dtale.show(data)
d.open_browser()