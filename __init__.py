from mycroft import MycroftSkill, intent_file_handler


class Ann(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('ann.intent')
    def handle_ann(self, message):
        self.speak_dialog('ann')


def create_skill():
    return Ann()

