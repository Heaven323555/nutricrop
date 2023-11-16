import joblib
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd

class CustomOneHotEncoder(BaseEstimator, TransformerMixin):
    def __init__(self, categorical_features=None, reindex_columns=None):
        self.categorical_features = categorical_features
        self.reindex_columns = reindex_columns
        self.updated_feature_names = None

    def transform(self, X, **transformparams):
        # print (transformparams.get('arg1'))
        self.updated_feature_names = []
        hot_encoded_df = pd.get_dummies(data=X, columns=self.categorical_features, \
                                        drop_first=False).copy()
        # Lets reindex this thing, which will add any missing columns in the passed data
        print(hot_encoded_df.shape)
        hot_encoded_df = hot_encoded_df.reindex(columns=self.reindex_columns, fill_value=0)
        print(hot_encoded_df.shape)
        # Now we have reformed the encoded dataframe by filling any missing columns
        self.updated_feature_names = hot_encoded_df.columns
        return hot_encoded_df

    def fit(self, X, y=None, **fitparams):
        return self

    def get_feature_names(self):
        return self.updated_feature_names


# Load your pickled model (replace 'path/to/your_model.pkl' with the actual path)
crop_clf = joblib.load('/prediction/crop_classifier.pkl')
crop_reg = joblib.load('/prediction/agri_reg.pkl')


def predict_crop(Nitrogen, Phosphorous, Pottassium, Temp, humd, ph, rain):
    # Prepare the input data as a DataFrame
    data = pd.DataFrame([[Nitrogen, Phosphorous, Pottassium, Temp, humd, ph, rain]],
                        columns=['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall'])

    # Make predictions using the loaded model
    prediction = crop_clf.predict(data)

    return prediction[0]


def predict_yield(District, Crop_name, Area):
    df = pd.DataFrame({'District_Name': [District], 'Crop': [Crop_name], 'Area': [Area]})
    prediction = crop_reg.predict(df)

    return prediction[0]  # Corrected return statement

# You don't need the extra "return result_yield" at the end
