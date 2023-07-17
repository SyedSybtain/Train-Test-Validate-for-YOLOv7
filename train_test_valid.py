# https://github.com/SyedSybtain
import os
import random
import shutil

def split_data(data_dir, train_ratio, test_ratio, val_ratio):
    # Get list of all image and annotation filenames
    all_images = os.listdir(os.path.join(data_dir, 'images'))
    all_annots = os.listdir(os.path.join(data_dir, 'labels'))
    # Shuffle the list of images and labels in the same order
    random.seed(42)
    random.shuffle(all_images)
    random.seed(42)
    random.shuffle(all_annots)

    # Calculate the number of images for each set
    num_images = len(all_images)
    train_num = int(num_images * train_ratio)
    test_num = int(num_images * test_ratio)
    val_num = int(num_images * val_ratio)

    # Create the train, test and validation directories
    train_dir = os.path.join(data_dir, 'train')
    test_dir = os.path.join(data_dir, 'test')
    val_dir = os.path.join(data_dir, 'val')
    os.makedirs(os.path.join(train_dir, 'images'), exist_ok=True)
    os.makedirs(os.path.join(train_dir, 'labels'), exist_ok=True)
    os.makedirs(os.path.join(test_dir, 'images'), exist_ok=True)
    os.makedirs(os.path.join(test_dir, 'labels'), exist_ok=True)
    os.makedirs(os.path.join(val_dir, 'images'), exist_ok=True)
    os.makedirs(os.path.join(val_dir, 'labels'), exist_ok=True)

    # Move the images and labels to their respective directories
    for i, image_file in enumerate(all_images):
        src_image_path = os.path.join(data_dir, 'images', image_file)
        src_annot_path = os.path.join(data_dir, 'labels', image_file.replace('.jpg', '.txt'))
        if i < train_num:
            dst_image_path = os.path.join(train_dir, 'images', image_file)
            dst_annot_path = os.path.join(train_dir, 'labels', image_file.replace('.jpg', '.txt'))
        elif i < train_num + test_num:
            dst_image_path = os.path.join(test_dir, 'images', image_file)
            dst_annot_path = os.path.join(test_dir, 'labels', image_file.replace('.jpg', '.txt'))
        else:
            dst_image_path = os.path.join(val_dir, 'images', image_file)
            dst_annot_path = os.path.join(val_dir, 'labels', image_file.replace('.jpg', '.txt'))
        shutil.copy(src_image_path, dst_image_path)
        shutil.copy(src_annot_path, dst_annot_path)

if __name__ == '__main__':
    data_dir = 'lpnum_final'
    train_ratio = 0.7
    test_ratio = 0.1
    val_ratio = 0.2
    split_data(data_dir, train_ratio, test_ratio, val_ratio)
