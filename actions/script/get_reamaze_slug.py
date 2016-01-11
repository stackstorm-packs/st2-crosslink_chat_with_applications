# coding=utf-8
from st2actions.runners.pythonrunner import Action
import re


class GetReamazeSlug(Action):
    def __init__(self, config):
        super(GetReamazeSlug, self).__init__(config)

    def run(self, text):
        regex = 'https?:\/\/(.*)\.reamaze.com\/admin\/conversations\/([^\s]+)'
        search = re.search(regex, text)
        payload = {
            'brand': search.group(1),
            'slug': search.group(2),
        }
        return payload
