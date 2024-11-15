### Quantasis-SpellChecker
Quantasis SpellChecker is a python based web application that leverages the SymSpell library to look for spelling errors and rectifies them using a dictionary.

### Why SymSpell ?
- I tried using TextBlob, but it was slow and made too many mistakes while correcting the mistakes. It is good in finding mistakes, but not rectifying them.
- Pyspellchecker was a faster choice, but inconsistent. It could accurately correct a typed text input, but not a text file input. Threw errors I could not understand.
- Lastly, I found SymSpell [at this GeeksForGeeks site](https://www.geeksforgeeks.org/spelling-correction-in-text-preprocessing-using-symspell/). It was  fast, convenient and understandable enough to try it out without having to worry much.
- Symspell comes with an available frequency dictionary for spellcheck in various languages. I used the english library ["en-80k.txt"](https://github.com/wolfgarbe/SymSpell/tree/master/SymSpell.FrequencyDictionary).
- I still do not understand SymSpell Library entirely and have to read more about it , nor it is fully accurate and functioning as one would expect right now. But it is a great start and easy implementation .

### Front-end 
- I used chat-gpt and bootstrap to create a basic template.

### Other than front-end , nowhere was AI used.

### For Flask Routing and Requests and FrontEnd connections, The following articles from GeeksForGeeks were used
- [How to Use CSS in Python Flask](https://www.geeksforgeeks.org/how-to-use-css-in-python-flask/)
- [Retrieving HTML Form data using Flask](https://www.geeksforgeeks.org/retrieving-html-from-data-using-flask/)

### Steps for installation
1. Install Flask and SymSpell
   ```
   pip install flask symspellpy
   ```
2. Setting up project directories
   ```
   SymSpellChecker/
   SymSpellChecker/templates/
   SymSpellChecker/templates/index.html  # HTML File
   SymSpellChecker/static/
   SymSpellChecker/static/style.css      # CSS File
   SymSpellChecker/app.py                # Flask Application 
   SymSpellChecker/en-80k.txt            # Word dictionary for SymSpell
   ```
3. Dictionary
   Make sure you have a dictionary of your choice present in the project directory/ folder
   In my case, it was ["en-80k.txt"](https://github.com/wolfgarbe/SymSpell/tree/master/SymSpell.FrequencyDictionary)

 4. Flask Application : app.py
 5. HTML Page : index.html
 6. CSS Page : style.css
 7. Run the flask application  as follows :
    ```
    python app.py
    ```
