# Handwriting-formula-recognition
An <a href="https://github.com/kingyiusuen/image-to-latex">image-to-latex</a> inspired project.

We provides a framework that transforms handwriting forluma images into LaTeX forms. Moreover, the model was also trained to be Chinese-readable, which means it can recognize Chinese as well.

The basic framework is the same as **image-to-latex**, big thanks for the great work.

We improved the code so that it can be deployed to any language you want. Specifically, you should retrain the project with you own dataset, see the format in image-to-latex repository. Then, the vocabulary will store all the characters in your dataset.

> Hint: remember to make sure the encoding method supports your language, currently it is set to be "utf-8".
