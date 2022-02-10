# Solution - [competition name]

Username: <...>

## Summary

General summary of the steps for your solution. Consider questions like:

- What kind of data preprocessing did you do?
- What types of models and/or pretrained model backbones did you use? Is your final prediction an ensemble?
- Did you modify the output of your trained model(s)?

# Setup

1. Install the prerequisities
     - Python version <...>

2. Install the required python packages

3. ...

All of the steps necessary to set up an environment in which your code will run, starting on a fresh system with no dependencies (e.g. a brand new Linux, Mac OS X, or Windows installation).


This should include:
- Python version
- Versions and installation instructions for any tools that cannot be installed as Python packages. Eg. If you use FFmpeg for video processing, this section might include:
  
  > FFmpeg v3:
  > ```
  > sudo apt update
  > sudo apt install ffmpeg
  > ```
- All required python packages, including versions. **We recommend listing these clearly in a `requirements.txt` or `environment.yml` file**
- The expected file structure before inference or training is run

# Hardware

The solution was run on <...>

Training time: <...>

Inference time: <...>

Machine specs you used for inference/training, and rough estimates of how long each step took.

# Run training

Instructions for training a model from scratch using your code. Ideally, you will have a main point of entry such as an executable script that runs all steps of the pipeline in a deterministic fashion e.g., a `.py` file, `.sh` file, or Jupyter notebook.

Consider questions like:
- What are all of the data sources needed? Where and how is each used?
- How much space will your model weights file(s) require?
- Where will model weights be saved out to by default?
- How can we access your trained model weights? We only rerun the inference step, so we should be able to download any model files needed without rerunning the full training process.
    - We make competition solutions open-source to increase the impact of all that hard work. If possible, model weights should be publicly available for download.
- Does training require network access or any open-source downloads?

# Run inference

Instructions for generating a final submission using your code. Ideally, you will have a main point of entry to your code such as an executable script that runs all steps of the pipeline in a deterministic fashion e.g., a `.py` file, `.sh` file, or Jupyter notebook.

**We should be able to rerun inference programmatically using only the raw competition data and your model weights.** There should not be any retraining or manual input required. Your goal should be to have an entry point to inference that would work on any new data samples that are in the same format as the test data you were provided. 

Consider questions like:
- What are all of the data sources needed? Where and how is each used?
- If there is a data preprocessing step, how do we run processing on the test set only? Remember that we only need to rerun inference, not training.
- How much space will any interim processed data files require?
- What files will be saved out during inference and what is each used for? Where will the final submission be saved out to by default?
- Are there any common pitfalls we should be aware of for troubleshooting?