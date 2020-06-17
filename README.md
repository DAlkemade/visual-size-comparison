# visual-size-comparison
Package for efficiently using the training set of Visual Genome (http://visualgenome.org/) for size comparisons using
max(height,width) of bounding boxes.

Includes code for propagation.

## Setup
Requires logging-setup-dla package, available on GitHub https://github.com/DAlkemade/logging-setup-dla

Get data from http://visualgenome.org/api/v0/api_home.html (tested with version 1.4) and move to `data` directory

## Run
Run the following for an example. This also shows some figures and statistics for the dataset.
```cmd
python example.py
```