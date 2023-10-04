import os
import time
import shutil


DOWNLOADS_PATH = "C:/Users/Furkan/Downloads"
HOUR_IN_SECONDS = 3600

while True:
    downloads_list = os.listdir(DOWNLOADS_PATH)

    if downloads_list:
        for item in downloads_list:
            item_path = os.path.join(DOWNLOADS_PATH, item)

            if (not item.endswith(".ini")) and (os.path.getctime(item_path) > HOUR_IN_SECONDS * 8):
                try:
                    if os.path.isfile(item_path):
                        os.remove(item_path)
                    else:
                        shutil.rmtree(item_path)
                    print(f"Removed item: {item}.")
                except Exception as e:
                    print(f"Something went wrong: {e}")

    time.sleep(HOUR_IN_SECONDS * 8)
