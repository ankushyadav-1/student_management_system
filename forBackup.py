# import main
import pandas as pd
import shutil

shutil.copy('student.csv', 'student - Copy.csv')
print("✅ File copied successfully.\n")

df = pd.read_csv('student - Copy.csv')
print(df)
