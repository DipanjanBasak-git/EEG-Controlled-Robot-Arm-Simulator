import json
import base64
from pathlib import Path

# Load the notebook
notebook_path = 'EEG_Signal_Classifier_using_Python_+_MNE_BCI_toolkits (3).ipynb'
with open(notebook_path, 'r', encoding='utf-8') as f:
    notebook = json.load(f)

# Directory to save images
images_dir = Path('images')
images_dir.mkdir(exist_ok=True)

image_count = 0
gif_count = 0

for i, cell in enumerate(notebook['cells']):
    if 'outputs' in cell:
        for output in cell['outputs']:
            if 'data' in output:
                if 'image/png' in output['data']:
                    # Save PNG
                    img_data = output['data']['image/png']
                    img_bytes = base64.b64decode(img_data)
                    img_path = images_dir / f'image_{image_count}.png'
                    with open(img_path, 'wb') as img_file:
                        img_file.write(img_bytes)
                    print(f'Saved {img_path}')
                    image_count += 1
                if 'image/gif' in output['data']:
                    # Save GIF
                    img_data = output['data']['image/gif']
                    img_bytes = base64.b64decode(img_data)
                    img_path = images_dir / f'animation_{gif_count}.gif'
                    with open(img_path, 'wb') as img_file:
                        img_file.write(img_bytes)
                    print(f'Saved {img_path}')
                    gif_count += 1

print(f'Extracted {image_count} PNG images and {gif_count} GIFs')