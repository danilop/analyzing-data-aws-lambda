from sklearn.ensemble import RandomForestClassifier

import json

def lambda_handler(event, context):
    clf = RandomForestClassifier(random_state=0)
    X = [[ 1,  2,  3], [11, 12, 13]] # 2 samples, 3 features
    y = [0, 1]  # classes of each sample
    clf.fit(X, y) # fitting the classifier 
    A = [[4, 5, 6], [14, 15, 16], [3, 2, 1], [17, 15, 13]]
    result = {
        'type': 'RandomForestClassifier',
        'predict({})'.format(X): '{}'.format(clf.predict(X)),
        'predict({})'.format(A): '{}'.format(clf.predict(A))
    }
    return {
        'statusCode': 200,
        'body': json.dumps(result)
    }
