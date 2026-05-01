import pandas as pd
from sklearn.preprocessing import LabelEncoder

def load_and_preprocess_data(path):

    df = pd.read_csv(path)

    # Remove missing values
    df.dropna(inplace=True)

    # Encode categorical columns
    le = LabelEncoder()

    for col in df.select_dtypes(include='object').columns:
        df[col] = le.fit_transform(df[col])

    return df