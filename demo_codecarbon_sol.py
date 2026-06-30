from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
import time

from codecarbon import EmissionsTracker
tracker = EmissionsTracker(allow_multiple_runs=True, log_level="error")


#Loading dataset
digits = load_digits()

#Splitting datasets into train and test datasets
X_train, X_test, y_train, y_test = train_test_split(
    digits.data, digits.target, test_size=0.2, random_state=42
)
#Summary
print(f"Training examples: {len(X_train)}")
print(f"Test examples: {len(X_test)}")
print(f"Each image is a {digits.images[0].shape} pixel grid, flattened to {X_train.shape[1]} numbers")



MAX_ITERATIONS = 200  # how many training iterations the model gets
N_REPEATS = 20        # repeat the fit this many times, just to get a measurable duration

tracker.start()
start_time = time.time()

# Training
for _ in range(N_REPEATS):
    model = MLPClassifier(hidden_layer_sizes=(64,), max_iter=MAX_ITERATIONS, random_state=42)
    model.fit(X_train, y_train)

elapsed = time.time() - start_time
emissions = tracker.stop()

# Computing Metrics
accuracy = accuracy_score(y_test, model.predict(X_test))
energy = tracker._total_energy.kWh

# Summary
print(f"\n=== Results (max_iter={MAX_ITERATIONS}, trained {N_REPEATS} times) ===")
print(f"Accuracy:      {accuracy*100:.2f}%")
print(f"Total time:    {elapsed:.2f} sec")
print(f"CO2 emitted:   {emissions*1000:.6f} g CO2eq")
print(f"Energy used:   {energy:.8f} kWh")
