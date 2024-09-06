import os
import subprocess
import time
import datetime

import cv2
import uiautomator2 as u2


class ADBClient:
    def __init__(self):
        pass

    @staticmethod
    def push_data_to_camera():
        # 使用相对路径构建 adb push 命令
        current_working_directory = os.getcwd()
        print(f"Current working directory: {current_working_directory}")
        relative_path = r'data\data_camera'
        destination_path = '/sdcard/DCIM/Camera'

        command = rf'adb push {relative_path} {destination_path}'

        try:
            print(command)
            time.sleep(1)
            # 使用 subprocess 執行指令，加上 stdout=subprocess.PIPE
            subprocess.run(command, shell=True)
        except subprocess.CalledProcessError as e:
            print(f"Error executing command: {e}")

    @staticmethod
    def push_1_pic_to_camera():
        # 使用相对路径构建 adb push 命令
        current_working_directory = os.getcwd()
        print(f"Current working directory: {current_working_directory}")
        relative_path = r'data\data_1_pic'
        destination_path = '/sdcard/DCIM/Camera'

        command = rf'adb push {relative_path} {destination_path}'

        try:
            print(command)
            time.sleep(1)
            # 使用 subprocess 執行指令，加上 stdout=subprocess.PIPE
            subprocess.run(command, shell=True)
        except subprocess.CalledProcessError as e:
            print(f"Error executing command: {e}")

    @staticmethod
    def push_2_pic_to_camera():
        # 使用相对路径构建 adb push 命令
        current_working_directory = os.getcwd()
        print(f"Current working directory: {current_working_directory}")
        relative_path = r'data\data_2_pic'
        destination_path = '/sdcard/DCIM/Camera'

        command = rf'adb push {relative_path} {destination_path}'

        try:
            print(command)
            time.sleep(1)
            # 使用 subprocess 執行指令，加上 stdout=subprocess.PIPE
            subprocess.run(command, shell=True)
        except subprocess.CalledProcessError as e:
            print(f"Error executing command: {e}")

    @staticmethod
    def push_data_to_device(data=str, album=str):
        # 使用相对路径构建 adb push 命令
        current_working_directory = os.getcwd()
        print(f"Current working directory: {current_working_directory}")
        relative_path = fr'data\{data}'
        destination_path = f'/sdcard/DCIM/{album}'

        command = rf'adb push {relative_path} {destination_path}'

        try:
            print(command)
            time.sleep(1)
            # 使用 subprocess 執行指令，加上 stdout=subprocess.PIPE
            subprocess.run(command, shell=True)
        except subprocess.CalledProcessError as e:
            print(f"Error executing command: {e}")

    @staticmethod
    def push_location_pic_to_camera():
        # 使用相对路径构建 adb push 命令
        current_working_directory = os.getcwd()
        print(f"Current working directory: {current_working_directory}")
        relative_path = r'data\data_location'
        destination_path = '/sdcard/DCIM/Camera'

        command = rf'adb push {relative_path} {destination_path}'

        try:
            print(command)
            time.sleep(1)
            # 使用 subprocess 執行指令，加上 stdout=subprocess.PIPE
            subprocess.run(command, shell=True)
        except subprocess.CalledProcessError as e:
            print(f"Error executing command: {e}")

    @staticmethod
    def push_data_to_albums():
        # 使用相对路径构建 adb push 命令
        relative_path = r'data\data_albums'
        destination_path = '/sdcard/Pictures/'

        command = rf'adb push {relative_path} {destination_path}'

        # 使用 subprocess 執行指令
        try:
            print(command)
            # 使用 subprocess 執行指令，加上 stdout=subprocess.PIPE
            subprocess.run(command, shell=True)

        except subprocess.CalledProcessError as e:
            print(f"Error executing command: {e}")

    @staticmethod
    def delete_albums_camera_data():
        delete_albums_command = rf'adb shell rm -rf /sdcard/DCIM/Camera/*'
        delete_camera_command = rf'adb shell rm -rf /sdcard/Pictures/*'
        # 使用 subprocess 執行指令
        try:
            subprocess.run(delete_albums_command, shell=True)
            subprocess.run(delete_camera_command, shell=True)
        except subprocess.CalledProcessError as e:
            print(f"Error executing command: {e}")

    @staticmethod
    def refresh_gallery_albums():
        refresh_gallery_command = (
            'adb shell am broadcast -a android.intent.action.MEDIA_SCANNER_SCAN_FILE -d file:///sdcard/Pictures')
        # 使用 subprocess 執行指令
        try:
            subprocess.run(refresh_gallery_command, shell=True)
            time.sleep(1)
        except subprocess.CalledProcessError as e:
            print(f"Error executing command: {e}")

    @staticmethod
    def refresh_gallery_camera():
        refresh_gallery_command = (
            'adb shell am broadcast -a android.intent.action.MEDIA_SCANNER_SCAN_FILE -d file:///sdcard/DCIM/Camera')
        # 使用 subprocess 執行指令
        try:
            subprocess.run(refresh_gallery_command, shell=True)
            time.sleep(1)
        except subprocess.CalledProcessError as e:
            print(f"Error executing command: {e}")

    @staticmethod
    def clear_gallery_cache():
        clear_gallery_cache_command = 'adb shell pm clear com.nothing.gallery'
        # 使用 subprocess 執行指令
        try:
            subprocess.run(clear_gallery_cache_command, shell=True)
        except subprocess.CalledProcessError as e:
            print(f"Error executing command: {e}")

    @staticmethod
    def start_gallery_app():
        d = u2.connect()
        # ADB command to start the app by package name
        cmd = "adb shell am start -a android.intent.action.MAIN -n com.nothing.gallery/.activity.EntryActivity"

        # Execute the ADB command
        subprocess.run(cmd, shell=True)
        time.sleep(2)

    @staticmethod
    def start_settings():
        d = u2.connect()
        # ADB command to start the app by package name
        cmd = "adb shell am start -n com.android.settings/.Settings"

        # Execute the ADB command
        subprocess.run(cmd, shell=True)

    @staticmethod
    def stop_settings():
        # ADB command to start the app by package name
        cmd = "adb shell am force-stop com.android.settings"
        # Execute the ADB command
        subprocess.run(cmd, shell=True)

    @staticmethod
    def stop_gallery_app():
        cmd = "adb shell am force-stop com.nothing.gallery"
        subprocess.run(cmd, shell=True)

    @staticmethod
    def disable_auto_rotate():
        cmd = ("adb shell content insert --uri content://settings/system --bind "
               "name:s:accelerometer_rotation --bind value:i:0")
        subprocess.run(cmd, shell=True)

    @staticmethod
    def enable_auto_rotate():
        cmd = ("adb shell content insert --uri content://settings/system --bind "
               "name:s:accelerometer_rotation --bind value:i:1")
        subprocess.run(cmd, shell=True)

    @staticmethod
    def set_rotate():
        cmd = ("adb shell content insert --uri content://settings/system "
               "--bind name:s:user_rotation --bind value:i:1")

        subprocess.run(cmd, shell=True)

    @staticmethod
    def screenshot(file_name=None):
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot_png_name = f"{file_name}.png" or f"screenshot_{timestamp}.png"
        local_png_path = os.path.join(os.getcwd(), screenshot_png_name)

        try:
            # pytest.set_trace()
            # 使用 adb 截取屏幕并将其保存到本地文件
            subprocess.run(["adb", "shell", "screencap", "-p", f"/sdcard/{screenshot_png_name}"])
            # print(f"Local screenshot path: {local_png_path}")
            subprocess.run(["adb", "pull", f"/sdcard/{screenshot_png_name}", local_png_path], check=True)
            # print(f"Screenshot pulled to: {local_png_path}")

            subprocess.run(["adb", "shell", "rm", f"/sdcard/{screenshot_png_name}"])
            # print(f"Delete fail screenshot: {screenshot_png_name}")

            # 使用 OpenCV 裁剪顶部 5% 的部分
            img = cv2.imread(local_png_path)
            height, width, _ = img.shape
            cropped_img = img[int(height * 0.05):, :]  # 裁剪掉顶部 5%

            # 保存裁剪后的图像
            cv2.imwrite(local_png_path, cropped_img)
            # print(f"Screenshot pulled and cropped to: {local_png_path}")

            refresh_gallery_command = (
                'adb shell am broadcast -a android.intent.action.MEDIA_SCANNER_SCAN_FILE -d file:///sdcard/Pictures')
            subprocess.run(refresh_gallery_command, shell=True)

            return local_png_path
        except Exception as e:
            print(f"Failed to capture screenshot: {e}")

    @staticmethod
    def ref_screenshot(file_name=None):
        screenshot_png_name = f"{file_name}.png"
        # 获取当前工作目录的上上一层的路径
        base_path = os.path.abspath(os.path.join(os.getcwd(), "../../data/ref_page"))
        local_png_path = os.path.join(base_path, screenshot_png_name)

        try:
            # pytest.set_trace()
            # 使用 adb 截取屏幕并将其保存到本地文件
            subprocess.run(["adb", "shell", "screencap", "-p", f"/sdcard/{screenshot_png_name}"])
            # print(f"Local screenshot path: {local_png_path}")
            subprocess.run(["adb", "pull", f"/sdcard/{screenshot_png_name}", local_png_path], check=True)
            # print(f"Screenshot pulled to: {local_png_path}")

            subprocess.run(["adb", "shell", "rm", f"/sdcard/{screenshot_png_name}"])
            # print(f"Delete fail screenshot: {screenshot_png_name}")

            # 使用 OpenCV 裁剪顶部 5% 的部分
            img = cv2.imread(local_png_path)
            height, width, _ = img.shape
            cropped_img = img[int(height * 0.05):, :]  # 裁剪掉顶部 5%

            # 保存裁剪后的图像
            cv2.imwrite(local_png_path, cropped_img)
            # print(f"Screenshot pulled and cropped to: {local_png_path}")

            refresh_gallery_command = (
                'adb shell am broadcast -a android.intent.action.MEDIA_SCANNER_SCAN_FILE -d file:///sdcard/Pictures')
            subprocess.run(refresh_gallery_command, shell=True)

            return local_png_path
        except Exception as e:
            print(f"Failed to capture screenshot: {e}")
