from abc import ABCMeta, abstractmethod
from six import add_metaclass
from itertools import chain

from nltk.internals import overridden
from nltk.metrics import accuracy

from nltk.tag.util import untag


@add_metaclass(ABCMeta)
class TaggerI(object):
    @abstractmethod
    def tag(self, tokens):
        if overridden(self.tag_sents):
            return self.tag_sents([tokens])[0]


    def tag_sents(self, sentences):
        return [self.tag(sent) for sent in sentences]


    def evaluate(self, gold):

        tagged_sents = self.tag_sents(untag(sent) for sent in gold)
        gold_tokens = list(chain(*gold))
        test_tokens = list(chain(*tagged_sents))
        return accuracy(gold_tokens, test_tokens)


    def _check_params(self, train, model):
        if (train and model) or (not train and not model):
            raise ValueError(
                    'Must specify either training data or trained model.')