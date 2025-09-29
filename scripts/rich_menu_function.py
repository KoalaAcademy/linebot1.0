import requests


class RichMenu:
    def __init__(self, token):
        self.headers = {'Authorization': f'Bearer {token}'}

    def create_rich_menu(self, body):
        api_url = 'https://api.line.me/v2/bot/richmenu'

        response = requests.post(api_url, json=body, headers=self.headers).json()
        return response['richMenuId']

    def get_rich_menu_list(self):
        api_url = 'https://api.line.me/v2/bot/richmenu/list'

        response = requests.get(api_url, headers=self.headers).json()
        return response['richmenus']

    def get_rich_menu(self, rich_menu_id):
        api_url = f'https://api.line.me/v2/bot/richmenu/{rich_menu_id}'

        response = requests.get(api_url, headers=self.headers).json()
        return response

    def attach_image(self, rich_menu_id, image_name):
        api_url = f'https://api-data.line.me/v2/bot/richmenu/{rich_menu_id}/content'

        headers = self.headers.copy()
        file_extension = image_name.split('.')[-1]
        headers['Content-Type'] = f'image/{file_extension}'

        with open(image_name, 'rb') as file:
            requests.post(api_url, file, headers=headers)

    def set_default_rich_menu(self, rich_menu_id):
        api_url = f'https://api.line.me/v2/bot/user/all/richmenu/{rich_menu_id}'

        requests.post(api_url, headers=self.headers)

    def cancel_default_rich_menu(self):
        api_url = 'https://api.line.me/v2/bot/user/all/richmenu'

        requests.delete(api_url, headers=self.headers)

    def get_default_rich_menu_id(self):
        api_url = 'https://api.line.me/v2/bot/user/all/richmenu'

        response = requests.get(api_url, headers=self.headers).json()
        return response['richMenuId']

    def delete_rich_menu(self, rich_menu_id):
        api_url = f'https://api.line.me/v2/bot/richmenu/{rich_menu_id}'

        requests.delete(api_url, headers=self.headers)

