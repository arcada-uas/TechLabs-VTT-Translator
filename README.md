# TechLabs-VTT-Translator
Quick script for translating transcripts in the format VTT using deep_translator 

Reads Input_transcript.vtt and outputs Output_transcript.vtt. 

Terrible implementation, uses one translation query per line of transcription, but it works.

## Setup & Usage

It's just a single python file you can run in the terminal

**_NOTE:_**  Check the filenames of input and ouput in the TranslateTranscript.py
- Create venv and activate
- Install dependency(ies)
- Run script and sit back and enjoy until you reach free api limits of your translation service


```
python -m venv translator
source translator/activate
pip install deep_translator
python -m TranslateTranscript.py
```

## Next steps
Help needed, feel free to submit a pull request where you assemble say 20 lines from the transcript at a time into a single query for the translator.

Not only will this reduce the amount of queries needed, it will also probably improve translations since sentences will have a larger context window.

