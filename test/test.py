import libchecker
import unittest


class Test(unittest.TestCase):
    def test_regex(self):
        responses = libchecker.query("libjcore222.so")
        self.assertEqual(len(responses), 1)
        response = responses[0]
        self.assertEqual(response.label, "极光推送")
        self.assertEqual(response.isRegexRule, 1)

    def test_type(self):
        responses = libchecker.query(
            "com.taobao.accs.ServiceReceiver", libchecker.RuleType.RECEIVER
        )
        self.assertEqual(len(responses), 1)
        response = responses[0]
        self.assertEqual(response.label, "阿里移动推送")

    def test_normal(self):
        responses = libchecker.query("libxcrash.so", libchecker.RuleType.SO)
        self.assertEqual(len(responses), 1)
        response = responses[0]
        self.assertEqual(response.label, "xCrash")


if __name__ == "__main__":
    unittest.main()
