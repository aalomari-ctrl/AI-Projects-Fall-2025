# KASPER AI Seizure Log

### Creator: Kyle Johnson

KASPER AI is a machine-learning seizure-risk estimator designed to help users track potential seizure triggers, symptoms, and frequent patterns.
The idea is to provide risk analysis, pattern recognition, and data-driven feedback, but it is ***NOT*** a substitute for professional medical advice.

This project was built using [Epilepsy Disorder Dataset](https://www.kaggle.com/datasets/amanik000/epilepsy-disorder-dataset?resource=download) with diagnostic categories removed.

## Updates

- Added the Multilayer Perceptron model to the project and combined it with the Random Forest model into an ensemble
- Added a single-row dictionary to identify personal patterns more accurately with stored information
- Added Permutation Importance to view what 15 features mostly influence the predicted seizure risk compared to Random Forest
- Removed more unessential categories to focus on seizure-related triggers and symptoms from the dataset
- Users can input more than one symptom and trigger
- Better user feedback is produced

## Accuracy

- The Random Forest model had an accuracy of **93%**.
  - The demo version was **84%**.
- The Multilayer Perceptron model had an accuracy of **100%**.
- The Ensemble had an accuracy of **96%**.
