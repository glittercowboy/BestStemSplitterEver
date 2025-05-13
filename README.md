# BestStemSplitterEver

A powerful audio stem splitter that detects key and BPM, separates tracks into stems, and even breaks down drum tracks into individual components.

## Features

- 🎵 Automatically detects musical key and BPM of audio tracks
- 🎚️ Separates audio into multiple stems (vocals, bass, drums, other)
- 🥁 Splits drum stems into individual components (kick, snare, hats, toms)
- 🏷️ Names files with key and BPM information for easy organization
- ⚙️ Configurable output directories and file naming


## Installation

1. Clone this repository:

   ```
   git clone https://github.com/glittercowboy/BestStemSplitterEver.git
   cd BestStemSplitterEver
   ```


2. Install Poetry if you don't have it already
(official docs: https://python-poetry.org/docs/#installation):

```sh
curl -sSL https://install.python-poetry.org | python3 -
```

3. Install dependencies and download the drum separation model
```sh
poetry install
poetry run download-model
```

To Run the stem splitter:
```sh
poetry run stem-splitter path/to/your_audio_file.wav
```

- The output will be placed in the folder specified by `output_dir` in `config.yaml` (default: `~/Music/Stems`). Edit the `config.yaml` file to customize your setup
- You can override the output directory or config file with command-line options:
  ```sh
  poetry run stem-splitter path/to/your_audio_file.wav --output path/to/output_dir
  ```

### Options:

- `-c`, `--config`: Path to custom config file
- `-o`, `--output`: Override output directory
- `-m`, `--model`: Override the Demucs model to use

### Available Demucs Models:

- `htdemucs`: Original HT model, 4 sources (vocals, drums, bass, other)
- `htdemucs_6s`: 6 sources model (adds piano and guitar separation)
- `htdemucs_ft`: Fine-tuned 4 sources model
- `mdx_extra`: Higher quality but slower
- `mdx_extra_q`: Quantized version of mdx_extra

### Examples:

```sh
# Split a song with default configuration
poetry run stem-splitter my_song.mp3

# Use a custom config file
poetry run stem-splitter my_song.mp3 --config my_config.yaml

# Specify output directory
poetry run stem-splitter my_song.mp3 --output ~/Desktop/MySongStems

# Use a different model
poetry run stem-splitter my_song.mp3 --model htdemucs

# Combine options
poetry run stem-splitter my_song.mp3 --model mdx_extra --output ~/Desktop/HighQualityStems
```

## Output

The script will create:

- A folder with your song's stems named according to your configuration
- Individual audio files for each stem (vocals, bass, drums, etc.)
- Individual drum component files (kick, snare, hats, toms)

## How It Works

1. The script analyzes your audio file to detect key and BPM
2. It uses Demucs to split the audio into stems
3. It uses Drumsep to separate drum components
4. All files are organized and named according to your preferences


## License

MIT License

## Acknowledgements

- [Demucs](https://github.com/facebookresearch/demucs) for audio source separation
- [Librosa](https://github.com/librosa/librosa) for audio analysis
- [drumSep](https://github.com/inagoy/drumsep) for drum separation

# Alternative models
Improved version of the drum separation model used by BestStemSplitterEver for potential future inclusion:
https://github.com/jarredou/models/releases/tag/aufr33-jarredou_MDX23C_DrumSep_model_v0.1