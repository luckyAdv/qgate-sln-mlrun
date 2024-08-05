import unittest
import os
from qgate_sln_mlrun.qualityreport import QualityReport
from qgate_sln_mlrun import output, setup

class TestCommon(unittest.TestCase):
    INPUT_FILE = "qgate-sln-mlrun.env"
    SETUP_FILES = ["qgate-sln-mlrun-private.env", "qgate-sln-mlrun.env"]

    @classmethod
    def setUpClass(cls):
        if not os.path.isfile(os.path.join(".", cls.INPUT_FILE)):
            os.chdir(os.path.dirname(os.getcwd()))

    def setUp(self):
        self.stp = setup.Setup(self.SETUP_FILES)
        self.output_dir = "./tests_output/"
        self.stp_with_output = setup.Setup(self.SETUP_FILES, None, {"QGATE_OUTPUT": self.output_dir})

    def test_setup_str(self):
        print(str(self.stp))

    def test_setup_str_with_output(self):
        print(str(self.stp_with_output))

    def test_scenarios_name_desc(self):
        out = output.Output(self.stp, [output.Output.DEFAULT_TEMPLATE_HTML, output.Output.DEFAULT_TEMPLATE_TXT])
        report = QualityReport(self.stp, out)
        test_scenarios = report.build_scenarios(True, True)

        for test_scenario in test_scenarios:
            tst = test_scenario(self)
            print(f"{tst.name}: {tst.desc}: {tst.long_desc}")

if __name__ == "__main__":
    unittest.main()
