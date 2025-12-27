
import os
import shutil


def copy_files(source_dir, target_dir):
    for path in os.listdir(source_dir):
        full_path = os.path.join(source_dir, path)
        if os.path.isdir(full_path):
            copy_files(full_path, os.path.join(target_dir, path))
        else:
            extension = os.path.splitext(path)[1]
            ext_path = os.path.join(target_dir, extension)
            os.makedirs(ext_path, exist_ok=True)
            shutil.copy2(full_path, os.path.join(ext_path, path))


if __name__ == "__main__":
    source_dir = "data/my_files"
    target_dir = "data/destination_copy"
    copy_files(source_dir, target_dir)
    print("Копіювання завершено.")