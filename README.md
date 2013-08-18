## Arabish (beta)

Arabic transliteration in Python. Similar to [Yamli.com](http://yamli.com), [Google Ta3reeb](http://www.google.com/intl/ar/inputtools/cloud/try/), and [Microsoft Maren](http://afkar.microsoft.com/en/maren/).

## Why

Because there isn't an open source transliteration project available. And it's not that hard!

## Approach

1. Given a list of simple mappings between one or two english letters representing a single arabic letter
2. Append to english letter keys in the mapping vowels to simply ignore the Harakaat.
2. Given an english word phonatically representing an arabic word.
3. Construct the set of all possible arabic words (valid or not) using a recursive search algorithm.
4. Use word frequency to get the most likely word to occur out of the list.

## Current state

I'm very pleased, even surprised with the initial results. With a better training corpus and some simple tweaking to the rules we can get at least up to 80% accuracy of Yamli or similar services.
The current training corpus is a [frequency list based on words from opensubtitles.org](http://invokeit.wordpress.com/frequency-word-lists/). And is mostly classical arabic.

See `TODO.txt`
