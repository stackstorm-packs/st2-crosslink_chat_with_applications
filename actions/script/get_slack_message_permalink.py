from st2actions.runners.pythonrunner import Action
import re, string


class GetSlackMessagePermalink(Action):
    def __init__(self, config):
        super(GetSlackMessagePermalink, self).__init__(config)

    def run(self, channel, timestamp, team='stackstorm'):
      timestamp_url = "p{}".format(string.replace(timestamp, '.', ''))
      url = 'https://{}.slack.com/archives/{}/{}'.format(
               team, channel, timestamp_url)
      return url
