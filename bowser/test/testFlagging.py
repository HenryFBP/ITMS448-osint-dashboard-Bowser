import unittest

from bowser.contentFlagger import ContentFlaggerBadWords, ContentFlagger


class ContentFlaggerTests(unittest.TestCase):
	def test_default_naive_contentflagger(self):
		cfn = ContentFlaggerBadWords()

		# No bad words!
		self.assertTrue(cfn.flag_content('fck'))
		self.assertTrue(cfn.flag_content('fuck'))
		self.assertTrue(cfn.flag_content('feck'))
		self.assertTrue(cfn.flag_content('f?ck'))

	def test_custom_contentflagger(self):
		cf = ContentFlagger(
			regex_matches=[r'abc \d\d\d'],
			keywords=['potato']
		)

		# ABC digit digit digit should get flagged
		self.assertTrue(cf.flag_content('abc 234'))
		self.assertTrue(cf.flag_content('abc 111'))
		self.assertTrue(cf.flag_content('abc 300'))

		# this contains 'potato', a keyword.
		self.assertTrue(cf.flag_content('  a sdffdas afsdafds asdf asdfafsd asdf asdf !!potato!! asdfafsd asdfafsdasdf '))

		# only 2 digits. shouldn't match.
		self.assertFalse(cf.flag_content('abc 12X'))