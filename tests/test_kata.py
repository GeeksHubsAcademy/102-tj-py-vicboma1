import pytest
import unittest   # The test framework

from kata import apply

class Test_kata(unittest.TestCase):

    def test_test01(self):
        result = apply(1) 
        assert(result == None) 
   

    def test_test02(self):
        expected = [2]
        result = apply(2) 
        assert(expected == result) 
   

    def test_test03(self):
        expected =  [2,3] 
        result = apply(3) 
        assert(expected == result) 
   

    def test_test04(self):
        expected =  [2,3,5,7] 
        result = apply(10) 
        assert(expected == result) 
   

    def test_test05(self):
        expected =  [2,3,5,7,11,13,17,19] 
        result = apply(20) 
        assert(expected == result) 
   

    def test_test06(self):
        expected =  [2,3,5,7,11,13,17,19,23,29] 
        result = apply(30) 
        assert(expected == result) 
   

    def test_test07(self):
        expected =  [2,3,5,7,11,13,17,19,23,29,31,37] 
        result = apply(40) 
        assert(expected == result) 
   

    def test_test08(self):
        expected =  [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47] 
        result = apply(50) 
        assert(expected == result) 
   

    def test_test09(self):
        expected =  [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97] 
        result = apply(100) 
        assert(expected == result) 
   

    def test_test10(self):
        expected =  [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269,271,277,281,283,293,307,311,313,317,331,337,347,349,353,359,367,373,379,383,389,397,401,409,419,421,431,433,439,443,449,457,461,463,467,479,487,491,499] 
        result = apply(500) 
        assert(expected == result) 
   

    def test_test11(self):
        expected =  [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269,271,277,281,283,293,307,311,313,317,331,337,347,349,353,359,367,373,379,383,389,397,401,409,419,421,431,433,439,443,449,457,461,463,467,479,487,491,499,503,509,521,523,541,547,557,563,569,571,577,587,593,599,601,607,613,617,619,631,641,643,647,653,659,661,673,677,683,691,701,709,719,727,733,739,743,751,757,761,769,773,787,797,809,811,821,823,827,829,839,853,857,859,863,877,881,883,887,907,911,919,929,937,941,947,953,967,971,977,983,991,997] 
        result = apply(1000) 
        assert(expected == result) 
   


if __name__ == '__main__':
	unittest.main()