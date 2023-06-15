# This program converts text from PDF file to MP3 audio file
# The input is a path to the PDF file
# The output is an audio file

# Install modules: pdfplumber, gtts, art
from gtts import gTTS
import pdfplumber
from pathlib import Path
from art import tprint

# Function to convert PDF to audio MP3
def pdf_to_mp3(file_path='book.pdf', language='en'):
    # Checking the existence of the file received in file_path
    if Path(file_path).is_file() and Path(file_path).suffix == '.pdf':
        print(f'Your file: {file_path}')
        print('The Conversion is in the process...')
        # Open the PDF file in binary mode
        with pdfplumber.PDF(open(file=file_path, mode='rb')) as pdf:
            # Extract the pages
            pages = [page.extract_text() for page in pdf.pages]
        # Join the extracted pages
        text = ''.join(pages)
        # Delete \n with empty string so they don't spoil the audio file
        text = text.replace('\n', '')

        audio = gTTS(text=text, lang=language, slow=False)
        audio_file_name = Path(file_path).stem
        audio.save(f'{audio_file_name}.mp3')
        print(f'Your PDF has been successfully converted into MP3 audio')
        return f'{audio_file_name}.mp3 is ready to use'
    else:
        return 'Not exists!'
    
def main():
    tprint('PDF to MP3 Converter', font='white_bubble', space=1)
    # Use 'Cinderella.pdf' to test
    file_path = input('\nEnter file path of your PDF (or \'q\' to quit the program): ')
    if file_path == 'q':
        print('You quit the program')
        tprint('PDF to MP3 Converter', font='white_bubble', space=1)
        return
    else:
        # Use 'en' to test
        language = input('\nChoose the language of your PDF: ')
        if language == '':
            language = 'en'
        print(pdf_to_mp3(file_path=file_path, language=language))

if __name__ == '__main__':
    main()

