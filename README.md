# Machine Learning Models

## Summary:  
In order to raise more awareness about building data provided from the Systems Engineer Building (SEB), the team utilized the [CHISSL Tool](https://github.com/pnnl/chissl) on SEB data. The CHISSL tool allowed the team to find patterns within the data. Patterns were created along with a PNNL team member to make the following labels for the given units of the data:

```
Zone Temperature 
- Summer Occurrence
- Controlled Summer
- Controlled Winter
- Override Release
```
```
Zone Airflow
- Normal Operation
- Hunting
- Constant
- Override
```
With these patterns, labels were created for each instance on the data. The data was then split into a training set (80%) and test set (20%) to create two machine learning models.  

For **Zone Temperature**, a Random Forest model was created.  
For **Zone Airflow** a Decision Tree Classier model was created.  

Both models are packaged in a joblib file which allows the model saved in memory. You can find the models [here](https://github.com/PNNL-Project/ml-models/tree/master/models)
