import pandas as pd
import numpy as np

def ridge_regression_predict(train_df: pd.DataFrame, test_df: pd.DataFrame, alpha: float) -> np.ndarray:
    """
    Implements Ridge Regression from scratch (closed-form solution) and predicts target values on the test set.
    """
    # Prepare training data
    X_train = train_df.drop(columns='y').values
    y_train = train_df['y'].values

    # Prepare test data
    X_test = test_df.drop(columns='y', errors='ignore').values

    # Add bias term
    X_train_bias = np.hstack([np.ones((X_train.shape[0], 1)), X_train])
    X_test_bias = np.hstack([np.ones((X_test.shape[0], 1)), X_test])

    # Closed-form Ridge Regression: w = (X^T X + alpha*I)^-1 X^T y
    n_features = X_train_bias.shape[1]
    I = np.eye(n_features)
    I[0, 0] = 0  # Don't regularize bias
    w = np.linalg.inv(X_train_bias.T @ X_train_bias + alpha * I) @ X_train_bias.T @ y_train

    # Predict
    y_pred = X_test_bias @ w
    return y_pred

if __name__ == '__main__':
    n_samples, n_features = 10, 5
    rng = np.random.RandomState(0)
    y = rng.randn(n_samples)
    X = rng.randn(n_samples, n_features)
    train_df = pd.DataFrame(X, columns=[f'feature_{i}' for i in range(n_features)])
    train_df['y'] = y

    # Create a test set
    test_df = pd.DataFrame(X, columns=[f'feature_{i}' for i in range(n_features)])
    test_df['y'] = y

    # Predict
    y_pred = ridge_regression_predict(train_df, test_df, alpha=1.0)
    print("Predictions:", y_pred)