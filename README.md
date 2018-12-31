# Accident Detection Using CNN
## This is a team project, where our aim was to detect accidents on highways for speedy communication to nearby hospital/police station
### Approach:
1. Trained Imagenet with 50000 images for both Accident and Non-Accident
2. Added two LSTM layers(50 units each) to the bottleneck of the CNN layer, to take into account temporal data
3. Obtained the model from Tensorboard(95% Accuracy)
4. Ran the model on a Raspberry Pi with GSM module, Pi Camera,LCD Display,LED
5. Used the Pi Camera to capture accidents,and GSM Module to alert nearby Hospital/Police Station
