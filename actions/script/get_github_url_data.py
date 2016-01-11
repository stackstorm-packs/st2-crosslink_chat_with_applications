# coding=utf-8
from st2actions.runners.pythonrunner import Action
import re


class GetGithubUrlData(Action):
    def __init__(self, config):
        super(GetGithubUrlData, self).__init__(config)

    def run(self, text):
        regex = '(https?:\/\/)?github.com\/(.*)\/(.*)\/(issues|pull)\/([0-9]+)#?(.*)?'
        search = re.search(r'{}'.format(regex), text)
        payload = {
            'user': search.group(2),
            'repo': search.group(3),
            'issue': search.group(5),
            'comment': search.group(6)
        }
        return payload
