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

# Setup the word frequency dict.
import codecs

NWORDS = {}
word_counts = codecs.open('ar.txt', encoding='utf-8').read().split("\n")
for word_count in word_counts:
  if word_count:
    [word, n] = word_count.split()
    NWORDS[word] = int(n)

def sort_by_frequency(words):
  return sorted(words, key=NWORDS.get, reverse=True)


def transliterate_word(english):
  ret = set()

  def recur(letters, word):
    if len(letters) == 0:
      ret.add(word)
      return
    max_key_len = len(max(list(en_to_ar), key=len))
    for i in range(1, max_key_len + 1):
      l = letters[:i]
      if l in en_to_ar:
        for ar in en_to_ar[l]:
          recur(letters[i:], word + ar)

  recur(english, '')
  return ret

def transliterate(sentence):
  words = sentence.split()
  ret = []
  for word in words:
    candidates = list(transliterate_word(word))
    ret.append(sort_by_frequency(candidates)[0])
  return ' '.join(ret)

print transliterate('thahab alwalado 2la almadrasa lyata3alam allo3\'ah al3arabieh belenglizieh')
print transliterate('matha taf3alo ya fata')
print transliterate('qlto laka 2thhab men hona 2mok tab7atho 3ank')

