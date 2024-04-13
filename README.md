# Custom-ChatBot-Using-Gemini

# How to run?
### STEPS:

Clone the repository

```bash
Project repo: https://github.com/HarshalGidh/Custom-ChatBot-Using-Gemini
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n chatbot python=3.10 -y
```

```bash
conda activate chatbot
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


### Create a `.env` file in the root directory and add your Google_API_Key credentials as follows:

```ini
GOOGLE_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```


```bash
# Run the following command to run basic chatbot 
python app.py
```

```bash
# Run the following command to run vision chatbot 
python vision.py
```
```bash
# Run the following command to run Q&A chatbot with Chat History
python qachat.py
```

Now, opne local host to see the ChatBot
```bash
open up localhost:
```