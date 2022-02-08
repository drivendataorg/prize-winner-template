> *Congratulations* on making it to this step! You're almost done :)
> This repository is provided to help with structuring and documenting your solution code before you submit it for review. We recommend cloning this repository as a starting point for your submission.
> 
> To verify each prize winner, we will:
> - Review all of your code to ensure that it complies with the competition rules
> - Fully rerun the inference step of your solution to ensure that your winning score can be reproduced
> 
> A clear, thorough README is critical to this process. Below, we have provided a README template to fill in for your submission. For a full example README, see the `example_submission` folder.
> 
> Your goal is to **set up your solution as if it were a finished open-source project**. In particular, make sure that the inference step is fully reproducible with any new set of data. For a full list of what you need to submit, see the [Prize recipient documentation guide]('TODO- ADD LINK').



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
- All required python packages, including versions. We recommend listing these in a `requirements.txt` or `environment.yml` file
- The expected file structure before inference or training is run

# Hardware

The solution was run on <...>

Training time: <...>

Inference time: <...>

Machine specs you used for inference/training, and rough estimates of how long each step took.

# Run training

Instructions for training a model from scratch using your code. Ideally, you will have a main point of entry such as an executable script that runs all steps of the pipeline in a deterministic fashion. Eg. a `.py` file, `.sh` file, or IPython notebook

Consider questions like:
- How much space will your model weights file(s) require?
- Where will model weights be saved out to by default?
- How can we access your trained model weights? We only rerun the inference step, so we should be able to download any model files needed without rerunning the full training process.
    - We make competition solutions open-source to increase the impact of all that hard work. If possible, model weights should be publicly available for download.
- Does training require network access or any open-source downloads?

# Run inference

Instructions for generating a final submission using your code. Ideally, you will have a main point of entry to your code such as an executable script that runs all steps of the pipeline in a deterministic fashion. Eg. a `.py` file, `.sh` file, or IPython notebook

**We should be able to rerun inference programmatically using only the raw competition data and your model weights.** There should not be any retraining or manual input required.

Consider questions like:
- If there is a data preprocessing step, how do we run processing on the test set only? Remember that we only need to rerun inference, not training.
- How much space will any interim processed data files require?
- What files will be saved out during inference and what is each used for? Where will the final submission be saved out to by default?
- Are there any common pitfalls we should be aware of for troubleshooting?


# Tips & Resources

- [Prize recipient documentation guide](TODO: add link)
- We recommend our [open source data science template](http://drivendata.github.io/cookiecutter-data-science/) as an effective structure for sharing code
- An example README is provided in the `example_submission` folder, along with corresponding code for reference. The example submission is based on the benchmark [blog post](https://www.drivendata.co/blog/genetic-attribution-benchmark/) for the Genetic Engineering Attribution Challenge.
- The [3rd Place winner](https://github.com/drivendataorg/deep-chimpact-winners/tree/master/3rd%20Place) from the Deep Chimpact: Depth Estimation for Wildlife Conservation competition provides a good example of a well-written README for more complicated code. A big thank you to user vecxoz for a well-written and clearly documented solution!