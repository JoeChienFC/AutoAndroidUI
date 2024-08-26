import os
import subprocess
import time

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