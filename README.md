# ML Model with Jenkins CI/CD Pipeline

This project demonstrates a simple machine learning model trained on the Iris dataset using a Decision Tree classifier. The project also includes a Jenkins CI/CD pipeline to automate the process of training, testing, and deploying the model.

## Project Structure

ml-jenkins-pipeline/
│
├── Jenkinsfile
├── train_model.py
├── test_model.py
└── requirements.txt

- **Jenkinsfile**: Defines the Jenkins CI/CD pipeline.
- **train_model.py**: Script to train the machine learning model.
- **test_model.py**: Script to test the trained machine learning model.
- **requirements.txt**: List of dependencies.

## Steps to Run the Project

1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/ml-jenkins-pipeline.git
   cd ml-jenkins-pipeline
   
2. Set up Python environment and install dependencies:
   python3 -m venv env
   source env/bin/activate
   pip install --upgrade pip
   pip install -r requirements.txt
   
3. Train the model:
   python train_model.py
   
4. Test the model:
   python test_model.py



