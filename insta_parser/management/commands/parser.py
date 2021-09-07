import json
from random import randint
from time import sleep
from typing import AnyStr, List, Dict

import requests
from django.core.management.base import BaseCommand
from seleniumwire.webdriver import Chrome

PROJECT_URL = 'http://localhost:8000'


class Command(BaseCommand):

    def handle(self, *args, **options):
        return self.parse('alexmusic12321', 'music_test123')

    @staticmethod
    def sign_in(username, password, driver):
        driver.get('https://www.instagram.com/')
        sleep(randint(2, 4))
        driver.find_element_by_css_selector('input[name=username]').send_keys(username)
        sleep(randint(2, 4))
        driver.find_element_by_css_selector('input[name=password]').send_keys(password)
        sleep(randint(2, 4))
        driver.find_element_by_css_selector('button[type=submit]').click()
        sleep(randint(3, 7))

    @staticmethod
    def get_input_data():
        return requests.get(f'{PROJECT_URL}/parser/instagram_data/').json()

    def parse(self, username, password):
        driver = Chrome()
        self.sign_in(username, password, driver)
        input_data = self.get_input_data()
        highlights = {item['title']: item['id'] for item in input_data['highlights']}
        story_hashtags = {item['hash_tag']: item['id'] for item in input_data['story_hashtags']}
        igtv_hashtags = {item['hash_tag']: item['id'] for item in input_data['igtv_hashtags']}
        output_data = dict()
        for user in input_data['users']:
            driver.get(user['instagram'])
            request = driver.wait_for_request('include_suggested_users')
            output_data['stories'] = self.get_stories(
                user['id'],
                driver,
                request,
                highlights,
                story_hashtags,
            )
            output_data['igtvs'] = self.get_igtv_data(
                driver,
                user,
                igtv_hashtags,
            )
        self.send_to_app(output_data)

    @staticmethod
    def get_stories(user: AnyStr, driver: Chrome, request: AnyStr, highlights: Dict, hashtags: Dict) -> List:
        """
        :param user: instagram user
        :param driver: browser
        :param request: driver request
        :param highlights: dict of highlights names
        :param hashtags: dict of hashtags names
        :return: stories data list
        """
        current_user_data = requests.get(request.url, headers=request.headers).text
        edges = json.loads(current_user_data)['data']['user']['edge_highlight_reels']['edges']
        items = []
        for edge in edges:
            node = edge['node']
            title = node['title']
            if title not in highlights:
                continue

            driver.get('https://www.instagram.com/stories/highlights/{}'.format(node['id']))
            sleep(randint(2, 4))
            request = driver.wait_for_request('show_story_viewer_list')
            response_data = json.loads(requests.get(request.url, headers=request.headers).text)
            for item in response_data['data']['reels_media'][0]['items']:
                video_resources = item.get('video_resources')
                tappable_objects = item['tappable_objects']
                if tappable_objects and tappable_objects[0]['__typename'] == 'GraphTappableHashtag':
                    hashtag = tappable_objects[0]['name']
                    if hashtag not in hashtags or not video_resources:
                        continue

                    items.append({
                        'hash_tag': hashtags[hashtag],
                        'highlight': highlights[title],
                        'user': user,
                        'url': video_resources[-1]['src'],
                    })
        return items

    @staticmethod
    def get_igtv_data(driver, user, hashtags):
        driver.get(f"{user['instagram']}channel/")
        sleep(randint(3, 6))
        items = []
        for item in driver.find_elements_by_css_selector('a._bz0w'):
            tag = item.find_element_by_css_selector('._2XLe_')
            if tag:
                hashtag = tag.text
                if hashtag not in hashtags:
                    continue

                items.append({
                    'hash_tag': hashtags[hashtag],
                    'user': user['id'],
                    'url': tag['href'],
                })
        return items

    @staticmethod
    def send_to_app(output_data):
        requests.post(f'{PROJECT_URL}/parser/instagram_data/', json=output_data)
