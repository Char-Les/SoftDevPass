# Charles Weng
# SoftDev2   pd7
# K #15: Do You Even List?
# 2018-4-25

################################################################################
#                                   Defined Sets                               #
################################################################################

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alpha2 = "abcdefghijklmnopqrstuvwxyz"
nums = "1234567890"
symbols = ".?!&#,;:-_*"


################################################################################
#                                   functions                                  #
################################################################################

def pass_check(wow):
    upperCheck = 0
    lowerCheck = 0
    numCheck = 0
    symCheck = 0
    lenCheck = len(wow) / 3
    if (sum([1 if x in alpha else 0 for x in wow]) > 0):
        upperCheck = 1
    if (sum([1 if x in alpha2 else 0 for x in wow]) > 0):
        lowerCheck = 1
    if (sum([1 if x in nums else 0 for x in wow]) > 0):
        numCheck = 1
    if (sum([1 if x in symbols else 0 for x in wow]) > 0):
        symCheck = 1
    sumCheck = upperCheck + lowerCheck + numCheck + symCheck + lenCheck + 1
    if sumCheck > 10:
        return 10
    return sumCheck


def pass_bool(wow):
    return pass_check(wow) > 6


def tester(wow):
    print "|" + wow + "|"
    print "bool: " + str(pass_bool(wow))
    print "strength: " + str(pass_check(wow)) + "\n\n"


################################################################################
#                                   testing                                    #
################################################################################

tester("Password")
tester("NubPassword64")
tester("12345678901234567890")
tester("@")
tester("LeetG0d767@gmail")
