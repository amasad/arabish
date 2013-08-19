# coding=utf-8
import sys
sys.path.append('../arabish')
from arabish import transliterate as t
import unittest

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
      pass

    def test_conservative_classical_arabic(self):
      self.assertEqual(
        t('thahab alwalado 2la almadrasa lyata3alam allo3\'ah al3arabieh belenglizieh'),
        u'ذهب الولد إلى المدرسة ليتعلم اللغة العربة بالانجليزية'
      )
      self.assertEqual(
        t('matha taf3alo ya fata'),
        u'ماذا تفعل يا فتى'
      )
      self.assertEqual(
        t('qlto laka 2thhab men hona 2mok tab7atho 3ank'),
        u'قلت لك أذهب من هنا أمك تبحث عنك'
      )
      self.assertEqual(
        t('talawathat almiah'),
        u'تلوثت المياه'
      )

    def test_simple_collqicual(self):
      self.assertEqual(
        t('sho betgool'),
        u'شو بتقول'
      )

    def test_word_start(self):
      self.assertEqual(
        t('ela'),
        u'إلى'
      )
      self.assertEqual(
        t('omok'),
        u'أمك'
      )
      self.assertEqual(
        t('al'),
        u'ال'
      )

    # def test_non_dictionary_word(self):
    #   self.assertEqual(
    #     t('almessenger'),
    #     u'المسنجر'
    #   )

if __name__ == '__main__':
  unittest.main()