import codecademylib3

# Import pandas with alias
import pandas as pd

# Import dataset as a Pandas Dataframe
auto = pd.read_csv('autos.csv', index_col=0)

# Print the first 10 rows of the auto dataset
print(auto.head())

# Print the data types of the auto dataframe
print(auto.dtypes)

# Change the data type of price to float
auto["price"] = auto["price"].astype("float")
print(auto["price"].dtypes)

# Set the engine_size data type to category
auto["engine_size"] = pd.Categorical(auto["engine_size"],["small", "medium", "large"], ordered = True)
print(auto["engine_size"].unique())

# Create the engine_codes variable by encoding engine_size
auto["engine_codes"] = auto["engine_size"].cat.codes
print(auto["engine_codes"].head())
# One-Hot Encode the body-style variable
auto = pd.get_dummies(data = auto, columns = ["body-style"])
print(auto.head())