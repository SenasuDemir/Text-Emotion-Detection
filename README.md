# 🎭 Text Emotion Detection  
Predicting emotions from text using NLP and Machine Learning  

## 📌 Aim  
The goal of this project is to predict the **emotion** expressed in a given piece of text. Since emotions are often conveyed through **personal experiences**, the project focuses on analyzing text data to classify the underlying emotion. By leveraging **Natural Language Processing (NLP)** techniques and **Machine Learning** models, the aim is to build a system capable of automatically categorizing text into different emotional states.  

## 📊 Dataset Explanation  
The dataset consists of two columns:  

- **🏷 Label:** Represents the emotion associated with the text, encoded as a **one-hot vector** (binary values). Each position corresponds to a specific emotion, with `1` indicating the presence of that emotion.  
- **📝 Text:** Sentences or short passages that describe emotional experiences. The emotions include **love, happiness, sadness, anger, surprise, etc.**  

### 🏷 Example  
A one-hot vector representation could look like:  
1. 0. 0. 0. 0. 0. 0.
Here, the `1` in the first position could represent **love** as the predicted emotion.  

## 🎯 Objective  
This project involves:  
✅ **Preprocessing** the text (cleaning, tokenization, etc.)  
✅ Applying **feature extraction** methods (TF-IDF, word embeddings)  
✅ Training machine learning models like **Logistic Regression, Random Forest, or Deep Learning models**  
✅ Predicting the **emotion label** for unseen text  

## 🚀 Models & Results  
Several machine learning models were tested for emotion classification, with **Logistic Regression** achieving the highest accuracy:  

| Model | Accuracy |
|--------|------------|
| 📈 **Logistic Regression** | **58.69%** |
| 🌲 Random Forest | 57.02% |
| 🚀 Gradient Boosting | 54.81% |
| 📊 Bernoulli NB | 54.27% |
| 🔢 Multinomial NB | 54.27% |
| 🌳 Decision Tree | 47.46% |
| ⚡ AdaBoost | 46.39% |

## 📉 Confusion Matrix  
Below is the confusion matrix for **Logistic Regression**, the best-performing model:  

![Confusion Matrix](image.png)  

## 🔥 Live Demo  
Try out the **Text Emotion Detection** model on Hugging Face Spaces:  
👉 [Hugging Face Space](https://huggingface.co/spaces/Senasu/Text_Emotion_Detection)  


## 📜 Conclusion  
This project successfully implemented machine learning models to classify emotions from text. While **Logistic Regression (58.69%)** provided the best results, there is room for improvement with **deep learning techniques** and **larger datasets**. This study demonstrates the feasibility of **machine learning for emotion recognition** and sets the foundation for further advancements in **sentiment analysis and affective computing**.  

---

💡 **Developed by [@Senasu](https://github.com/Senasu)**  
📧 Feel free to reach out for questions or contributions!  
