from flask import Flask, render_template, request, send_file
from symspellpy.symspellpy import SymSpell, Verbosity
import os

# Initialize Flask app
app = Flask(__name__)

# Initialize SymSpell
sym_spell = SymSpell(max_dictionary_edit_distance=2, prefix_length=7)

# Load dictionary
dictionary_path = "en-80k.txt"  
if not sym_spell.load_dictionary(dictionary_path, term_index=0, count_index=1):
    raise FileNotFoundError("Dictionary file not found!")

# Helper function: Correct spelling in text
def correct_text(input_text):
    corrected_words = []
    corrections = {}

    for word in input_text.split():
        suggestions = sym_spell.lookup(word, Verbosity.CLOSEST, max_edit_distance=2)
        if suggestions and word.lower() != suggestions[0].term.lower():
            corrected_word = suggestions[0].term
            corrections[word] = corrected_word
            corrected_words.append(corrected_word)
        else:
            corrected_words.append(word)
    return " ".join(corrected_words), corrections

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process_input():
    # Process user input
    if request.method == 'POST':
        corrections = {}
        input_type = request.form.get("input_type")
        original_text = ""

        if input_type == "text":
            # Text input case
            original_text = request.form["user_text"]
        elif input_type == "file":
            # File upload case
            file = request.files["user_file"]
            if file:
                original_text = file.read().decode("utf-8")
        
        # Correct the text
        corrected_text, corrections = correct_text(original_text)
        
        # Save corrected output to a file
        output_file_path = "static/corrected_output.txt"
        with open(output_file_path, "w") as f:
            f.write(corrected_text)

        # Render results
        return render_template(
            'index.html',
            original_text=original_text,
            corrected_text=corrected_text,
            corrections=corrections,
            output_file_path=output_file_path
        )

# Run Flask app
if __name__ == '__main__':
    app.run(debug=True)
