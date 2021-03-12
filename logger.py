from rasa.nlu.components import Component
from rasa.nlu import utils
from rasa.nlu.model import Metadata

import os

import typing
from typing import Any, Optional, Text, Dict

SENTIMENT_MODEL_FILE_NAME = 'logged.pk1'

class Logger(Component):
  name: "logger"
  provides: []
  requires: []
  defaults: {}
  language_list: ["en"]
  
  def __init__(self, component_config=None):
    super(Logger, self).__init__(component_config)
  
  def train(self, training_data, cfg, **kwargs):
    pass

  def process(self, message, **kwargs):
    print("Message:", message.data)

  
  def persist(self, file_name, model_dir):
    pass