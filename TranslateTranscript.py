import re
import html
from deep_translator import GoogleTranslator

def extract_vtt_content(filename):
    # Read the VTT file
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Split into caption blocks
    blocks = content.split('\n\n')

    # Open output file
    with open("Output_transcript.vtt", 'w', encoding='utf-8') as f:
        f.write("WEBVTT\n\n")  # Print header
        
        # Process each block
        for block in blocks[1:]:  # Skip the WEBVTT header
            lines = block.strip().split('\n')
            if len(lines) >= 3:  # Valid blocks should have at least 3 lines
                id_line = lines[0]
                timestamp = lines[1]
                text = '\n'.join(lines[2:])
                
                # Extract speaker and text
                match = re.search(r'<v ([^>]+)>([^<]*)</v>', text)
                if match:
                    speaker = html.unescape(match.group(1))
                    original_text = html.unescape(match.group(2))
                    
                    
                    f.write(f"{id_line}\n")
                    f.write(f"{timestamp}\n")
                    f.write(f"<v {speaker}>")
                    translator = GoogleTranslator(source='sv', target='en')
                    translated_text = translator.translate(original_text)
                    f.write(f"{translated_text}</v>\n")
                    f.write("\n")  # Separator between blocks

# Process the file
extract_vtt_content("Input_transcript.vtt")