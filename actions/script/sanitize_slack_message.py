# coding=utf-8
from st2actions.runners.pythonrunner import Action
import re


class SanitizeSlackMessage(Action):
    def __init__(self, config):
        super(SanitizeSlackMessage, self).__init__(config)

    def run(self, text):
      return self.unfurl_urls(text)

    @staticmethod
    def unfurl_urls(text):
       return re.sub(r'<(https?:\/\/.*)>', '\\1', text)
