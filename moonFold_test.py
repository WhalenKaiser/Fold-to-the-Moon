Test.describe("Basic tests")
Test.assert_equals(fold_to(384000000),42)
Test.assert_equals(fold_to(0.00005),0)
Test.assert_equals(fold_to(-1),None)
