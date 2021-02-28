import connexion
from joblib import load

# Instantiate our Flask app object
app = connexion.FlaskApp(__name__, port=8082, specification_dir='swagger/')
application = app.app

# Load our pre-trained model
clf = load('zone_temperature_model.joblib')

# Implement a simple health check function (GET)
def health():
    # Test to make sure our service is actually healthy
    try:
        predict(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.283840854,0.220556274,0.204051153,0.135780367,0.106521999,0.007492703,-0.038271588)
    except:
        return {"Message": "Service is unhealthy"}, 500

    return {"Message": "Service is OK"}

# Implement the prediction
def predict(hour_0, hour_1, hour_2, hour_3, hour_4, hour_5, hour_6, hour_7, hour_8, hour_9, hour_10, hour_11, hour_12, hour_13, hour_14, hour_15, hour_16, hour_17, hour_18, hour_19, hour_20, hour_21, hour_22, hour_23):
    
    # Accept the feature values for clf.predict()
    prediction = clf.predict_proba([[hour_0, hour_1, hour_2, hour_3, hour_4, hour_5, hour_6, hour_7, hour_8, hour_9, hour_10, hour_11, hour_12, hour_13, hour_14, hour_15, hour_16, hour_17, hour_18, hour_19, hour_20, hour_21, hour_22, hour_23]])

    # Return the prediction as a json
    return {"prediction" : str(prediction)}

def test():
    return {"Message": "Test is OK"}

# Read the API definition for our service from the yaml file
app.add_api("zonetemp_classification_api.yaml")

# Start the app
if __name__ == "__main__":
    app.run()
