
"""
@package utilities

CheckPoint class implementation
It provides functionality to assert the result

Example:
    self.check_point.markFinal("Test Name", result, "Message")
"""
import utilities.custom_logger as cl
import logging
from base.selenium_webdriver import SeleniumDriver

class TestStatus(SeleniumDriver):

    log_exel = cl.custom_logger(logging.INFO)
    log = cl.custom_logger(logging.DEBUG, logging.INFO)

    def __init__(self, driver):
        """
        Inits CheckPoint class
        """
        super(TestStatus, self).__init__(driver)
        self.resultList = []

    def set_result(self, result, resultMessage):
        try:
            if result is not None:
                if result:
                    self.resultList.append("PASS")
                    self.log.info(f"### VERIFICATION SUCCESSFUL :: + {resultMessage}")
                else:
                    self.resultList.append("FAIL")
                    self.log.error(f"### VERIFICATION FAILED :: +  {resultMessage}")
            else:
                self.resultList.append("FAIL")
                self.log.error(f"### VERIFICATION FAILED :: +  {resultMessage}")
        except:
            self.resultList.append("FAIL")
            self.log.error("### Exception Occurred !!!")

    def mark(self, result, resultMessage):
        """
        Mark the result of the verification point in a test case
        """
        self.set_result(result, resultMessage)

    def mark_final(self, testName, result, resultMessage):
        """
        Mark the final result of the verification point in a test case
        This needs to be called at least once in a test case
        This should be final test status of the test case
        """
        self.set_result(result, resultMessage)

        if "FAIL" in self.resultList:
            self.log.error(f"{testName} ### TEST FAILED")
            self.resultList.clear()
            assert True == False
        else:
            self.log.info(f"{testName} ### TEST SUCCESSFUL")
            self.resultList.clear()
            assert True == True
