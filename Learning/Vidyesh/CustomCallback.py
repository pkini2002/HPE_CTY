"""**Callback Functions With 2 Classes ( For Implementing With Similar Flow To Other Frameworks )**

Steps:
1.   Create A Class With All The Callback Functions. This Class Created In Must Contain All The Required Callbacks Like **OnTrain, OnTrainStart, OnTrainEnd**. This Class Can be Called SwarmCallbacks as in TF
2.   Most of the Fit Methods for Models in Scikit learn do not have the callback feature as in Tensorflow. So We Need To Create Our Own Estimator using the Base Estimator Class which includes the Existing Estimator as the SubEstimator To Include *Callback* as a Valid Parameter to our fit function.This Class Acts as a Wrapper and can be called ***SwarmEstimator*** 


> **Note:** The Above Task Can be Done Using A Single Class As Shown in the Above Cell But It Wont Have a Similar Workflow
"""
from sklearn.base import BaseEstimator
from sklearn.model_selection import train_test_split

#STEP 1: Design SwarmCallbacks Class
class SwarmCallbacks(): #CALLBACK FUNCTIONS ARE DEFINED IN THIS CLASS
  def __init__(self):
    self.X_train = None
    self.X_test = None 
    self.Y_train = None 
    self.Y_test = None

  def onTrainStart(self,message):
    self.X_train,self.X_test,self.Y_train,self.Y_test = train_test_split(X,y,test_size=0.2)
    print(message)
    return  (self.X_train,self.X_test,self.Y_train,self.Y_test)

  def onTrainEnd(self,message,model):
    print(message)
    for i in range(model.n_estimators):
      print("Estimator",i+1,":",model.estimators_[i].predict(self.X_test))
    print("Accuracy Of The Model:",model.score(self.X_test,self.Y_test))

  def onTrain(self,progress):
    print("Training",progress*100,"% Completed")
    
#STEP 2: Design SwarmEstimator Class from BaseEstimator
class SwarmEstimator(BaseEstimator): #Custom Estimator That Overrides Fit Methods To Have the Callback Parameter
  def __init__(self,model): #Constructor To Initialise The Estimator
    self.model=model
    self.start_message="Training Started"   #Pre-Defined Parameters If Needed
    self.end_message="Training Ended"
    self._callback = None

  #Parameters: Model = Estimator Object of Scikit Learn (Eg: KNN Estimator Object, AdaBoost Estimator Object Etc)... More can be added
  
  def fit(self,X,Y=None,callback=None): #Overiding Fit Method to Have A Callback Keyword Argument
    if callback:
      [self._callback] = callback #Setting the Callback Object...Note: It Must Be Verified that it is an Instance of SwarmCallbacks Class Only !!!

    (X_train,X_test,Y_train,Y_test)=self._callback.onTrainStart(self.start_message); #Pre Training Callback in Swarm Callbacks

    if Y is not None: #For Supervised Learning
      for i in range(self.model.n_estimators):                # Training Callbacks in Swarm Callbacks Must Be Iterative Because ( For Now Using Forest Algorithms Having N Estimators Attribute )
        self.model.fit(X_train,Y_train)                       # Using Fit again and again overides Existing Data
        self._callback.onTrain((i+1)/self.model.n_estimators) # Data Can Be Optimised During Each Iteration Using This Function To get Higher Accuracy
                                                              # Now This Function is Just used for Printing Purposes
    else: #For Unsupervised Learning
      self.model.fit(X_train) #A Similar Implementation to Above can be done here
                                                
    self._callback.onTrainEnd(self.end_message,self.model)  #Post-Training Callbacks in Swarm Callbacks 
    
  def __getattr__(self,name):     #Custom Method Used to Get All The Methods & Members Under The Model Object
    attr = getattr(self.model,name)
    if callable(attr):
        def callback_wrapper(*args, **kwargs):
            result = attr(*args, **kwargs)
            return result
        return callback_wrapper
    else:
        return attr
  
  def set_params(self,**params): #Used to Change Hyper Parameters Of The Model
    self.model.set_params(**params)
    return self.get_params()

#WORKFLOW
from sklearn import datasets
from sklearn.ensemble import RandomForestRegressor

#Dataset
iris = datasets.load_iris()

#Setting Of Data
X = iris.data 
y = iris.target

#Choosing Model
rf = RandomForestRegressor(n_estimators=10)

#Create Swarm Estimator
swarmModel = SwarmEstimator(rf)

#Set CallBack Class
swarmCallback = SwarmCallbacks()

#Use Swarm Estimator to Call Fit with callback set as SwarmCallback Object
swarmModel.fit(X,y,callback=[swarmCallback])

#Predict
print(swarmModel.predict(X))

#Model
print(swarmModel.model)

#Get HyperParameters Of the Model
print(swarmModel.get_params())

#Set HyperParameters Of the Model
params={"warm_start":"True"}
print(swarmModel.set_params(**params))