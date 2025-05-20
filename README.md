# House-prediction-project
housing prediction based on different inputs


# House price prediction App
- data preprocessing in jupyter notebook
- A linear regression model using scikit-learn
- A deployed interactive web app using streamlit

# Project structure
house_pred/
app.py
model.pkl
housing csv
housing prediction.ipynb
requirements.tex
README.md


# Features Used in Model
price = dependent variable
area = square feet
bedrooms = no of bedrooms
bathrooms = no of bathrooms
stories = no of stories 
mainroad = (yes/no)
guestroom = (yes/no)
basement =  (yes/no)
hotwaterheating =  (yes/no)
airconditioning =  (yes/no)
packing = no of parking space
prefarea =  (yes/no)

All categories were converted using a dummy variable of 1 and 0 (1=yes, 0= no)

# ML Model 
model was built using linear regression
library = scikit-learn
project was trained using housing prediction.ipynb and saved as model.pkl using 'pickle'
