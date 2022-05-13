from Lead.importLeads import TestImportLeads
from Lead.transferLeads import TestTransferLeads
from Opportunity.opportunityPipeline import TestOpportunityPipeline
from Opportunity.opportunityClosed import TestOpportunityClosed

import unittest
TC1=unittest.TestLoader().loadTestsFromModule(TestTransferLeads)
TC2=unittest.TestLoader().loadTestsFromModule(TestImportLeads)
TC3=unittest.TestLoader().loadTestsFromModule(TestOpportunityPipeline)
TC4=unittest.TestLoader().loadTestsFromModule(TestOpportunityClosed)

RegressionSuite = unittest.TestSuite([TC1])
SanitySuite=unittest.TestSuite([TC1,TC3])

unittest.TextTestRunner().run(RegressionSuite)
unittest.TextTestRunner().run(SanitySuite)