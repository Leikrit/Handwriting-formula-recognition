# How to preprocess my data?

> Hint: There might be some redundant files in this repository, that are the original ones from image-to-latex. Just ignore them and follow the steps below.

Firstly, you should have a dataset (directory) of images (in the format of jpg/png) and renamed as `1.jpg`, as well as a directory of labels renamed as `1.txt` (make sure the format of labels are all txt). 

Then, following the order of:

- fmm.py
- data_filter.py
- extract_image_according_to_label_list.py
- data_preprocess_for_im2latex.py

> Hint: Make sure you have changed the file path to yours in each of these files.

After that, you should see 4 `.lst` files in the data root (where the image directory and label directory locates). Rename the file `im2latex_formulas.norm.lst` to be `im2latex_formulas.norm.new.lst`. Then your dataset is ready to go.
