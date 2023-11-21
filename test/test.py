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
        self.assertEqual(response.name, "libxcrash.so")
        self.assertEqual(response.isRegexRule, 0)

    def test_query_many(self):
        responses = libchecker.query_many(
            ["libxcrash.so", "libcocos2dcpp.so"], libchecker.RuleType.SO
        )
        self.assertEqual(len(responses), 2)
        self.assertEqual(responses[0].label, "xCrash")
        self.assertEqual(responses[1].label, "cocos2d-cpp")


if __name__ == "__main__":
    unittest.main()
