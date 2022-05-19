## Flask API for predicting punctuation and capitalization using NLP

Punctuation En Bert is a Bert based Punctuation and Capitalization model with BERT model by Nvidia. For each word in the input text, the model:  
- predicts a punctuation mark that should follow the word (if any). The model supports commas, periods and question marks.
- predicts if the word should be capitalized or not.

The NLP model can be downloaded [here](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/nemo/models/punctuation_en_bert) and needs to be present in the same directory as ```app.py```

### Setup
- Install requirements with ```pip3 install -r requirements.txt``` preferably in a virtual environment.
- Launch the application with ```python3 app.py```.  

### Usage
```GET``` requests can be done to the following endpoints 
- ```http://localhost:8080/``` returns a JSON response with usage instructions
- ```http://localhost:8080/capitalizePunct?text=hello how are you``` returns a JSON with predicted punctuation and capitalization i.e. ```Hello, how are you?```
- ```http://localhost:8080/restorePunct?text=hello how are you``` returns a JSON with indexes of words where a missing punctuation is predicted, as well as the predicted punctuation.  

### Example Responses
```http://localhost:8080/```  
> ```{"usage examples":{"capitalizeAndPunctuate":"http://localhost:8080/capitalizePunct?text=hello how are you","restorePunct":"http://localhost:8080/restorePunct?text=hello how are you"}}```  

```http://localhost:8080/capitalizePunct?text=hello how are you```  
> ```{"output":"Hello, how are you?"}```  

```http://localhost:8080/restorePunct?text=hello how are you```
> ```{"output":[{"index":0,"label":",","word":"hello"},{"index":3,"label":"?","word":"you"}]}```




