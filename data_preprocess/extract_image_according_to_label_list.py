import os
import shutil

label_dir = r'C:\Users\65344\Desktop\dataset1_after_filter\dev\labels/'
# label_dir = './data/math_210421/formula_labels_210421_no_chinese/'
image_dir = r'C:\Users\65344\Desktop\dataset1\dev\images/'

output_dir = r'C:\Users\65344\Desktop\dataset1_after_filter\dev\images/'

label_name_list = os.listdir(label_dir)
if not os.path.exists(output_dir):
    os.mkdir(output_dir)
for i in range(len(label_name_list)):
    label_name_list[i] = label_name_list[i][:-4]

# print(label_list)

image_name_list = os.listdir(image_dir)

for image_name in image_name_list:
    if image_name[:-4] in label_name_list:
        print(image_name)
        shutil.copy(image_dir + image_name, output_dir + image_name)