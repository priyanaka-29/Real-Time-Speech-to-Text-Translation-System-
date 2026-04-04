from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import whisper
import os
from werkzeug.utils import secure_filename
import tempfile

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load Whisper model (using 'base' for good balance of speed and accuracy)
# Options: tiny, base, small, medium, large
print("Loading Whisper model...")
model = whisper.load_model("base")
print("Whisper model loaded successfully!")

# Configuration
UPLOAD_FOLDER = tempfile.gettempdir()
ALLOWED_EXTENSIONS = {'webm', 'wav', 'mp3', 'ogg', 'm4a'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    """Serve the main HTML file"""
    return send_from_directory('.', 'index.html')

@app.route('/ping', methods=['GET'])
def ping():
    """Health check endpoint"""
    return jsonify({"status": "ok", "message": "VoiceX Backend is running"})

@app.route('/speech-to-text', methods=['POST'])
def speech_to_text():
    """
    Process audio file with Whisper and return transcription
    
    Expects:
        - audio: audio file (multipart/form-data)
        - language (optional): target language for translation
    
    Returns:
        JSON with original_text, detected_language
    """
    try:
        # Check if audio file is present
        if 'audio' not in request.files:
            return jsonify({"error": "No audio file provided"}), 400
        
        file = request.files['audio']
        
        if file.filename == '':
            return jsonify({"error": "No file selected"}), 400
        
        if file and allowed_file(file.filename):
            # Save uploaded file temporarily
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            
            print(f"Processing audio file: {filename}")
            
            # Transcribe with Whisper
            result = model.transcribe(
                filepath,
                fp16=False,  # Use FP32 for CPU compatibility
                language='en',  # Force English for now, can be made dynamic
                task='transcribe'
            )
            
            # Extract text and language
            original_text = result['text'].strip()
            detected_language = result.get('language', 'en')
            
            # Clean up temp file
            try:
                os.remove(filepath)
            except:
                pass
            
            print(f"Transcription: {original_text}")
            print(f"Detected language: {detected_language}")
            
            return jsonify({
                "original_text": original_text,
                "detected_language": detected_language,
                "success": True
            })
        
        return jsonify({"error": "Invalid file type"}), 400
    
    except Exception as e:
        print(f"Error processing audio: {str(e)}")
        return jsonify({"error": str(e)}), 500

@app.route('/languages', methods=['GET'])
def get_languages():
    """Return list of supported languages"""
    languages = {
        "en": "English",
        "hi": "Hindi",
        "te": "Telugu",
        "fr": "French",
        "es": "Spanish",
        "de": "German",
        "zh": "Chinese",
        "ja": "Japanese",
        "ar": "Arabic",
        "pt": "Portuguese",
        "ru": "Russian",
        "ko": "Korean",
        "it": "Italian"
    }
    return jsonify(languages)

@app.errorhandler(413)
def request_entity_too_large(error):
    """Handle file too large error"""
    return jsonify({"error": "File too large. Maximum size is 16MB"}), 413

@app.errorhandler(500)
def internal_server_error(error):
    """Handle internal server errors"""
    return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    print("=" * 50)
    print("VoiceX Backend Server")
    print("=" * 50)
    print("Whisper model loaded successfully")
    print("Server starting on http://127.0.0.1:5000")
    print("=" * 50)
    
    # Run the Flask app
    app.run(
        host='127.0.0.1',
        port=5000,
        debug=True,
        threaded=True
    )
