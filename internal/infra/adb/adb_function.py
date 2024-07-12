import re
import subprocess
import time
import uiautomator2 as u2


class ADBClient:
    def __init__(self):
        pass

    @staticmethod
    def grep_logcat_event_name(event_name):
        # 組合 adb logcat 指令
        command = rf'adb logcat -d | grep "\"event_name\":\"{event_name}\""'

        # 使用 subprocess 執行指令
        try:
            print(command)
            # time.sleep(1)
            # 使用 subprocess 執行指令，加上 stdout=subprocess.PIPE
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            print(f"logcat : {result.stdout}")

            if result.stdout:
                return True
            else:
                print(f"Error in logcat output: {result.stdout}")
                return False

        except subprocess.CalledProcessError as e:
            print(f"Error executing command: {e}")

    @staticmethod
    def grep_logcat_event_name_content_type(event_name, content_type):
        # 組合 adb logcat 指令
        command = rf'adb logcat -d | grep "\"event_name\":\"{event_name}\".*"content_type\":\"{content_type}\"'
        # 使用 subprocess 執行指令
        try:
            print(f"adb command : {command}")
            # 使用 subprocess 執行指令，加上 stdout=subprocess.PIPE
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            print(f"logcat : {result.stdout}")

            if result.stdout:
                return True
            else:
                print(f"Error in logcat output: {result.stdout}")
                return False

        except subprocess.CalledProcessError as e:
            print(f"Error executing command: {e}")

    @staticmethod
    def grep_logcat_userid():
        # 組合 adb logcat 指令
        command = rf'adb logcat -d | grep \"event_name\"'
        # 使用 subprocess 執行指令
        try:
            # 使用 subprocess 執行指令，加上 stdout=subprocess.PIPE
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            user_id_pattern = r'"user_id":"(\d+)"'

            if result.stdout:
                matches = re.findall(user_id_pattern, result.stdout)
                if matches:
                    return matches[-1]
                else:
                    return None

            else:
                print(f"Error in logcat output: {result.stdout}")
                return None

        except subprocess.CalledProcessError as e:
            print(f"Error executing command: {e}")
            return None

    @staticmethod
    def start_playsee_app():
        d = u2.connect()
        # ADB command to start the app by package name
        cmd = "adb shell am start -n com.framy.placey/.MainActivity"

        # Execute the ADB command
        subprocess.run(cmd, shell=True)
        d(description="btn_locationpicker").wait(timeout=10)

    @staticmethod
    def stop_playsee_app():
        cmd = "adb shell am force-stop com.framy.placey"
        subprocess.run(cmd, shell=True)

    @staticmethod
    def logcat_action_type_1408_community_id():
        cmd = "adb logcat -d | grep '\"action_type\":\"1408\"' | grep -o '\"community_id\":\"[^\"]*\"'"
        # 执行 adb 命令并获取输出
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        # 检查命令的返回码以及输出
        if result.returncode == 0:
            adb_communityid = result.stdout
            communityid = extract_community_ids(adb_communityid)[0]
            return communityid

    @staticmethod
    def check_action_type_1408_is_none():
        cmd = "adb logcat -d | grep '\"action_type\":\"1408\"' | grep -o '\"community_id\":\"[^\"]*\"'"
        try:
            # 执行 adb 命令并获取输出
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
            if result.stdout == "":
                return True
            else:
                return False
        except subprocess.CalledProcessError as e:
            print(f"Command execution failed with error: {e}")
            return None

    @staticmethod
    def clean_action_type_1408():
        for iteration in range(10):
            time.sleep(60)
            if ADBClient.check_action_type_1408_is_none():
                print("清空了1408")
                return None
        print("清空1408失敗")


def extract_community_ids(data):
    pattern = r'"community_id":"([^"]+)"'
    community_ids = []
    matches = re.finditer(pattern, data)
    for match in matches:
        community_id = match.group(1)
        community_ids.append(community_id)
    return community_ids
