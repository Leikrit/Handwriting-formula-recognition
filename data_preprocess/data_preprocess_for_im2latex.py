import os
import random
import shutil

# shuffle

input_dir = r'C:\Users\65344\Desktop\dataset1\train\labels/'
output_dir = r'C:\Users\65344\PycharmProjects\image-to-latex-main\dataset1/'
output_file = r'C:\Users\65344\PycharmProjects\image-to-latex-main\dataset1\im2latex_formulas.norm.new.lst'
image_input_dir = r'C:\Users\65344\Desktop\dataset1_after_filter\train\images/'
image_name_list_train = os.listdir(r'C:\Users\65344\Desktop\dataset1_after_filter\train\images/')
image_name_list_dev = os.listdir(r'C:\Users\65344\Desktop\dataset1_after_filter\dev\images/')
image_name_list_test = os.listdir(r'C:\Users\65344\Desktop\dataset1_after_filter\test\images/')


label_name_list = os.listdir(r'C:\Users\65344\Desktop\dataset1_after_filter\train\labels/')
# random.shuffle(label_name_list)
total_num = len(label_name_list)
print(total_num)
train_list = []

for i in range(total_num):
    train_list.append(label_name_list[i])

label_name_list = os.listdir(r'C:\Users\65344\Desktop\dataset1_after_filter\dev\labels/')
# random.shuffle(label_name_list)
total_num = len(label_name_list)
print(total_num)
val_list = []

for i in range(total_num):
    val_list.append(label_name_list[i])

label_name_list = os.listdir(r'C:\Users\65344\Desktop\dataset1_after_filter\test\labels/')
# random.shuffle(label_name_list)
total_num = len(label_name_list)
print(total_num)
test_list = []

for i in range(total_num):
    test_list.append(label_name_list[i])

with open(output_file, 'w', encoding='utf-8') as f0:
    index = 0
    with open(output_dir + 'im2latex_train_filter.lst', 'w', encoding='utf-8') as f1:
        for i in range(len(train_list)):
            print(index, end='\r')
            train_label_name = train_list[i]
            image_name = train_label_name[:-4] + '.png'
            if image_name in image_name_list_train:
                f1.write(image_name + ' ' + str(index) + '\n')
                shutil.copy(r'C:\Users\65344\Desktop\dataset1_after_filter\train\images/' + image_name, output_dir + 'all_images/' + str(i) + '.png')
                with open(r'C:\Users\65344\Desktop\dataset1_after_filter\train\labels/' + train_label_name, 'r', encoding='utf-8') as f2:
                    line = f2.read()
                    f0.write(line + '\n')
                index += 1

    with open(output_dir + 'im2latex_validate_filter.lst', 'w', encoding='utf-8') as f1:
        for i in range(len(val_list)):
            print(index, end='\r')
            val_label_name = val_list[i]
            image_name = val_label_name[:-4] + '.png'
            if image_name in image_name_list_dev:
                f1.write(image_name + ' ' + str(index) + '\n')
                shutil.copy(r'C:\Users\65344\Desktop\dataset1_after_filter\dev\images/' + image_name, output_dir + 'all_images/' + str(i + len(train_list)) + '.png')
                with open(r'C:\Users\65344\Desktop\dataset1_after_filter\dev\labels/' + val_label_name, 'r', encoding='utf-8') as f2:
                    line = f2.read()
                    f0.write(line + '\n')
                index += 1

    with open(output_dir + 'im2latex_test_filter.lst', 'w', encoding='utf-8') as f1:
        for i in range(len(test_list)):
            print(index, end='\r')
            test_label_name = test_list[i]
            image_name = test_label_name[:-4] + '.png'
            if image_name in image_name_list_test:
                f1.write(image_name + ' ' + str(index) + '\n')
                shutil.copy(r'C:\Users\65344\Desktop\dataset1_after_filter\test\images/' + image_name, output_dir + 'all_images/' + str(i + len(train_list) + len(val_list)) + '.png')
                with open(r'C:\Users\65344\Desktop\dataset1_after_filter\test\labels/' + test_label_name, 'r', encoding='utf-8') as f2:
                    line = f2.read()
                    f0.write(line + '\n')
                index += 1

# shuffle end
