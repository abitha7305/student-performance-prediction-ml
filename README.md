**🎓 Student Performance Prediction System (OULAD)**

**Dataset Source: Kaggle - Student Performance Dataset
Link: https://www.kaggle.com/datasets/rocki37/open-university-learning-analytics-dataset**

**📝 Project Overview**
    This project is an Early Warning System (EWS) designed to predict student academic outcomes (Pass/Fail) in an online learning environment. 
    By analyzing a combination of demographic data, previous academic history, and real-time behavioral "clickstream" data, the system identifies at-risk students with high precision, allowing for timely pedagogical intervention.
    The system is trained on the Open University Learning Analytics Dataset (OULAD).
    
**🚀 Key FeaturesPredictive Analytics:**
    Uses XGBoost to achieve a state-of-the-art accuracy of 90.04%.
    Behavioral Tracking: Factors in student engagement via VLE (Virtual Learning Environment) clicks.
    Explainable AI: Includes Feature Importance mapping to show which variables drive the prediction.
    Web Dashboard: A fully functional Flask web application for real-time student assessment.
    
**📊 Performance Analysis**
    Our model was rigorously tested against traditional algorithms to ensure optimal performance for the OULAD dataset.
    AlgorithmAccuracyMean Absolute Error (MAE)K-Nearest Neighbors (KNN)72%0.61Random Forest85%0.49XGBoost (Proposed)90.04%0.45
    
**🏗️ System Architecture**
The application follows a modular architecture:
    Data Tier: Integration of studentInfo, studentVle, and studentAssessment records.
    Processing Tier: Real-time feature engineering (calculating weighted averages and click sums).
    Model Tier: XGBoost inference engine loaded via joblib.
    Presentation Tier: Responsive Bootstrap UI for instructor interaction.
    
**⚙️ Installation & Usage**
    1. RequirementsEnsure you have Python installed, then install the dependencies:Bashpip install -r requirements.txt
    2. Run the ApplicationBashpython app.py
    **Open your browser and navigate to http://127.0.0.1:5000**.
    
**📚 Academic References**
This project is informed by and references the following research:Wang, J., & Yu, Y. (2025). Machine learning approach to student performance prediction of online learning. PLOS ONE.Ahmed, E. (2024). Student Performance Prediction Using Machine Learning Algorithms. Wollo University.Kuzilek, J., Hlosta, M., & Zdrahal, Z. (2017). 

**🔮 Future EnhancementsSHAP Integration:** Adding local explainability to show exactly why a specific student was flagged.
    Deep Learning: Implementing LSTMs to analyze the time-series pattern of clicks rather than just the total sum.
    Live Database: Migrating from static .csv files to a live SQL database for real-time institution-wide deployment.
