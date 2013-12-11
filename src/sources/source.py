import abc

class Source():
	__metaclass__ = abc.ABCMeta

	@abc.abstractmethod
	def executeDork(self, dork):
		""" Execute the provided dork based on the current source"""
		return