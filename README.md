# Competition prize winner submission template

***Congratulations* on making it to this step! You're almost done** :tada:

This repository is provided to help with structuring and documenting your solution code before you submit it for review. **We recommend cloning this repository as a starting point for your submission.**

To verify each prize winner, we will:
- :mag: Review all of your code to ensure that it complies with the competition rules
- :recycle: Fully rerun the inference step of your solution to ensure that your winning score can be reproduced

Your goal is to **set up your solution as if it were a finished open-source project**. In particular, make sure that the inference step is fully reproducible with any new set of data. 

## Repo organization
```
.
├── Documentation_guide.pdf <- Full list of items winners are required to submit
├── README.md          <- You are here!
├── README_template.md <- Template that you can fill in to document your solution code
├── data               <- Folder for storing your solution's data
├── models             <- Folder for your trained models, model predictions, or model summaries
├── requirements.txt   <- Placeholder for requirements to recreate your analysis environment
├── src                <- Folder for your project's source code
└── example_submission <- Example submission folder
    ├── README.md      <- Example README containing all required information
    └── ...            <- Codebase for the example submission
```

## Example submission

The example submission is based on the benchmark [blog post](https://www.drivendata.co/blog/genetic-attribution-benchmark/) for the Genetic Engineering Attribution Challenge. The goal is to provide an example README that covers all necessary information for a winning submission. Code is provided for reference to help understand the example README.

The structure of this solution is based on DrivenData's [cookiecutter-data-science](https://github.com/drivendata/cookiecutter-data-science/tree/master/%7B%7B%20cookiecutter.repo_name%20%7D%7D) repo, which we recommend for your submission.

## Tips & Resources

- We recommend our cookiecutter [open source data science template](http://drivendata.github.io/cookiecutter-data-science/) as an effective structure for sharing code.
- The [3rd Place winner](https://github.com/drivendataorg/deep-chimpact-winners/tree/master/3rd%20Place) from the Deep Chimpact: Depth Estimation for Wildlife Conservation competition provides a good example of a well-written README for more complicated code. A big thank you to user vecxoz for a well-written and clearly documented solution!
- For a full list of what you need to submit, see the `Documentation_guide.pdf`.