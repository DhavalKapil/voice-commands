from abc import ABCMeta, abstractmethod

class Task(object):
  
  __metaclass__ = ABCMeta

  @abstractmethod
  def action(self, user_text):
    """Action method to be performed
    on receiving any user input"""
    pass
