# coding=utf-8

ar_to_en = {
  u'ء': '2',
  u'أ': '2',
  u'ؤ': '2',
  u'إ': '2',
  u'ئ': '2',
  u'آ': '2',
  u'ا': 'a e',
  u'ب': 'b p',
  u'ت': 't',
  u'ث': 's th',
  u'ج': 'g j dj',
  u'ح': '7',
  u'خ': '5 kh 7\'',
  u'د': 'd',
  u'ذ': 'z dh th',
  u'ر': 'r',
  u'ز': 'z',
  u'س': 's',
  u'ش': 'sh ch',
  u'ص': 's 9',
  u'ض': 'd 9\'',
  u'ط': 't 6',
  u'ظ': 'z dh t\' 6\'',
  u'ع': '3',
  u'غ': '3\' gh',
  u'ف': 'f',
  u'ق': '2 g q 8 9',
  u'ك': 'k g',
  u'ل': 'l',
  u'م': 'm',
  u'ن': 'n',
  u'ه': 'h a e ah eh',
  u'ة': 'a e ah eh',
  u'و': 'w o u ou oo',
  u'ي': 'y i ee ei ai a',
  u'ى': 'y i ee ei ai a'
}

en_vowels = ['a', 'e', 'i', 'o', 'u']
# Arabic letters that is not effected by the presence of vowels.
# i.e. Can't have Harakaat.
ar_vowels = [u'ء', u'أ', u'ؤ', u'إ', u'ئ', u'آ', u'ا', u'ى']

en_to_ar = {}
for ar, en in ar_to_en.items():
  keys = en.split()
  if ar not in ar_vowels:
    # Add more keys to the list with a vowel at the end to make
    # up for harakat. i.e. Amjad -> amjd
    keys += [k + vowel for k in keys for vowel in en_vowels]
  for k in keys:
    try:
      en_to_ar[k].append(ar)
    except KeyError:
      en_to_ar[k] = [ar]

import json
import os

path = os.path.join(os.path.dirname(__file__), 'mapping.json')
open(path, 'w').write(json.dumps(en_to_ar, ensure_ascii=False).encode('utf-8'))
