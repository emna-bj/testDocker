import typing
from typing import Any, Optional, Text, Dict, List, Type

from rasa.nlu.components import Component
from rasa.nlu import utils
from rasa.shared.nlu.training_data.message import Message
from spellchecker import SpellChecker
spell = SpellChecker()
if typing.TYPE_CHECKING:
    from rasa.nlu.model import Metadata

class CorrectSpelling(Component):

    name = "Spell_checker"
    provides = ["message"]
    requires = ["message"]
    language_list = ["fr"]

    def __init__(self, component_config=None):
        super(CorrectSpelling, self).__init__(component_config)

    def train(self, training_data, cfg, **kwargs):
        """Not needed, because the the model is pretrained"""
        pass


    def process(self, message: Message, **kwargs):
        """Retrieve the text message, do spelling correction word by word,
        then append all the words and form the sentence,
        pass it to next component of pipeline"""
        textdata = message.Text
        textdata = textdata.split()
        new_message = ' '.join(spell.correction(w) for w in textdata)
        message.Text = new_message


    def persist(self,file_name, model_dir):
        """Pass because a pre-trained model is already persisted"""
        pass