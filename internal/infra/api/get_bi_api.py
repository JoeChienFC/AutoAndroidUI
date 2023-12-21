import requests


class API:
    def get_api_community_result(community_ids):
        url = f'https://bi-analytics-tool-framy-stage.uc.run.playsee.co/api/test/community_vtr?community_ids={community_ids}'
        headers = {
            'api-key': '8e9cca36d2b64dfe994fb8b77dafa03f'
        }

        try:
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                return response.json()
            else:
                print(f"请求失败，状态码: {response.status_code}")
        except requests.RequestException as e:
            print(f"请求发生错误: {e}")

    def get_api_community_result_view_count(community_ids):
        url = f'https://bi-analytics-tool-framy-stage.uc.run.playsee.co/api/test/community_vtr?community_ids={community_ids}'
        headers = {
            'api-key': '8e9cca36d2b64dfe994fb8b77dafa03f'
        }

        try:
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                result = response.json()
                return result['results'][0]['view_count']
            else:
                print(f"请求失败，状态码: {response.status_code}")
        except requests.RequestException as e:
            print(f"请求发生错误: {e}")