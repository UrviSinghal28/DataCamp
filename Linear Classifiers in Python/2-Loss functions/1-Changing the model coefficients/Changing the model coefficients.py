# Set the coefficients
model.coef_ = np.array([[-1,2]])
model.intercept_ = np.array([-4])

# Plot the data and decision boundary
plot_classifier(X,y,model)

# Print the number of errors
num_err = np.sum(y != model.predict(X))
print("Number of errors:", num_err)
