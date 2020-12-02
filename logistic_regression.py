from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

import json

# create a pipeline object
pipe = make_pipeline(
    StandardScaler(),
    LogisticRegression(random_state=0)
)

# load the iris dataset and split it into train and test sets
X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

# fit the whole pipeline
pipe.fit(X_train, y_train)
# we can now use it like any other estimator
###accuracy_score(pipe.predict(X_test), y_test)

def lambda_handler(event, context):
    result = {
        'accuracy_score': accuracy_score(pipe.predict(X_test), y_test)
    }
    return {
        'statusCode': 200,
        'body': json.dumps(result)
    }
