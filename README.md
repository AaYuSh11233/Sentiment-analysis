# 🧠 Multimodal Emotion Analyzer  

## ✨ Introduction
This is a **multimodal sentiment & emotion analysis system** that can classify human emotions based on **text, image, or audio inputs.**  
It combines Machine Learning and Deep Learning models trained on public datasets to deliver accurate predictions.  
Deployed with an intuitive **Streamlit web interface** for easy interaction.

---

## 🛠️ Technologies Used
- **Python 3.10+**
- **scikit-learn**
- **tensorflow**
- **pillow**
- **trochvision**
- **PyTorch**
- **Streamlit**
- **pandas, numpy, tqdm**
- **Jupyter Notebook** for model training workflows

---

## 🎯 What It Does
✅ Classifies emotions & sentiment from:
- ✍️ **Text**
- 🖼️ **Image**
- 🎤 **Voice/Audio**

You can upload or type your input and receive the predicted sentiment in real time.

---

## 📁 Project Structure

```
sentiment-analysis/
├── app.py # Streamlit web app
├── data/
│ ├── text/ # text datasets (e.g., IMDB, Sentiment140)
│ ├── image/ # images for training/testing
│ └── audio/ # audio clips for training/testing
├── models/ # trained models & vectorizers
│ ├── text_model.pkl
│ ├── text_vectorizer.pkl
│ ├── image_model.pt
│ └── audio_model.pt
├── notebooks/ # Jupyter notebooks for experiments & training
│ ├── train_text_model.ipynb
│ ├── train_image_model.ipynb
│ └── train_audio_model.ipynb
├── scripts/ # helper scripts (e.g., CSV creation, data cleaning)
├── src/ # inference & training modules
├── requirements.txt # dependencies
└── README.md # this file
```

---

## 📦 Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/sentiment-analysis.git
cd sentiment-analysis
```

###  2️⃣ Setup Virtual Environment & Install Dependencies
```bash
python -m venv venv
source venv/bin/activate     # or .\venv\Scripts\activate on Windows
pip install -r requirements.txt
```

🧪 Train Models & Save Them
Using Jupyter Notebook
Run the appropriate notebook from notebooks/:

For text sentiment:

```bash
jupyter notebook notebooks/train_text_model.ipynb
```

For image & audio, run corresponding notebooks similarly.

These notebooks guide you through:
✅ Loading data
✅ Preprocessing
✅ Training
✅ Saving the model into the models/ folder

📊 How to Collect Data
✅ Text datasets:

[IMDB](https://ai.stanford.edu/~amaas/data/sentiment/)

[Sentiment140](http://help.sentiment140.com/for-students)

✅ Image & audio:

Use open datasets from Kaggle or record your own small dataset and place them in data/image/ and data/audio/

📝 Pseudo-code: Create IMDB CSV from Raw Files

```bash
For each split in [‘train’, ‘test’]:
    For each sentiment in [‘pos’, ‘neg’]:
        Set folder path to data/aclImdb/{split}/{sentiment}/
        For each file in folder:
            Open file and read text
            Append (text, sentiment) to a list
Write list as a CSV with columns: text,sentiment
```
Like You get a zip file from the text source links then after extracting save the main folder inside your project then make a `scripts/` folder and inside that make a python helper file to read all the files and convert it into a single csv take help from the Pseudo-code.

🌐 Run & Test in Browser
Start the web app:

```
streamlit run app.py
Visit in your browser at:
📍 http://localhost:8501
```

You can type text, upload an image or audio file and see predictions.

🧩 Issues
If you encounter a bug, unexpected behavior, or have suggestions for improvements, feel free to open an issue here:
👉 [GitHub Issues](https://github.com/AaYuSh11233/Sentiment-analysis/issues)

When reporting an issue, please include:

✅ A clear description of the problem

✅ Steps to reproduce it

✅ Expected vs actual behavior

✅ Screenshots or logs, if applicable

✅ Details about your environment (OS, Python version, etc.)

Your feedback helps make this project better for everyone. Thank you! 💡

🤝 Contribution
Contributions are welcome! Whether it’s a bug fix, feature suggestion, documentation improvement, or new idea — we’d love to see it.

🚀 To contribute:
Fork the repository:
👉 Fork this repo

Clone your fork:

```
git clone https://github.com/your-username/Sentiment-analysis.git
```

Create a feature branch:

```
git checkout -b feature/your-feature-name
```

Make your changes & commit:

```
git commit -m "Add: your clear and concise message"
Push your branch:
```

```
git push origin feature/your-feature-name
Open a Pull Request against the main branch of this repository.
```

We recommend following the [Conventional Commits](https://www.conventionalcommits.org/) standard for commit messages when possible.

🌟 Tips for contributors:
📄 Follow the existing code style and directory structure.

🧪 Add tests and update documentation for new features.

❤️ Be kind, respectful, and constructive during code reviews and discussions.

Thank you for helping improve this project! ✨
