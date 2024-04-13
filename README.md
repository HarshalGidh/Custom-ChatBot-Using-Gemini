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
streamlit run app.py
```

```bash
# Run the following command to run vision chatbot 
streamlit run vision.py
```
```bash
# Run the following command to run Q&A chatbot with Chat History
streamlit run qachat.py
```

Now, opne local host to see the ChatBot
```bash
open up localhost:
```
## UI of Basic ChatBot 

![Screenshot 2024-04-13 202502](https://github.com/HarshalGidh/Custom-ChatBot-Using-Gemini/assets/126465410/2c5a23d9-f025-41c7-9aee-db5410db3134)

## UI of Image ChatBot 

### Image input
![Screenshot 2024-04-13 202854](https://github.com/HarshalGidh/Custom-ChatBot-Using-Gemini/assets/126465410/a19da267-a3fa-47d5-afdc-86bd0b4093b1)
### Response 
![Screenshot 2024-04-13 202915](https://github.com/HarshalGidh/Custom-ChatBot-Using-Gemini/assets/126465410/545f284f-5150-4b07-bac5-2f997cf8a069)
### Image input along with text input 
![Screenshot 2024-04-13 202951](https://github.com/HarshalGidh/Custom-ChatBot-Using-Gemini/assets/126465410/89a99769-e6b0-471d-853d-d87d9218cb0d)
### Response 
![Screenshot 2024-04-13 203008](https://github.com/HarshalGidh/Custom-ChatBot-Using-Gemini/assets/126465410/b05072c7-f4ab-4f03-9765-91c2e8558ef0)

## UI of Q&A ChatBot
![Screenshot 2024-04-13 203202](https://github.com/HarshalGidh/Custom-ChatBot-Using-Gemini/assets/126465410/7381a11e-3355-4b75-88b5-b2c850f6fc88)
![Screenshot 2024-04-13 203329](https://github.com/HarshalGidh/Custom-ChatBot-Using-Gemini/assets/126465410/f31b9611-4c81-4ce0-addb-4d6d4322d17f)
### Chat History 
![Screenshot 2024-04-13 203354](https://github.com/HarshalGidh/Custom-ChatBot-Using-Gemini/assets/126465410/cf9f7be4-44dc-4954-b3ae-462a349161e5)


