import os
class BranchCovDIY:
    histBranchBools = [False for i in range(37)]
    

    def writeRes(self):
        currTakenBranches = 0
        f = open("BranchCovRes.txt", "w")
        for currBranchNr in range(len(self.histBranchBools)):
            if(currBranchNr % 4 == 0 and currBranchNr != 0):
                f.write("||\n")
            f.write(f"|| Branch {currBranchNr} taken: {self.histBranchBools[currBranchNr]} ")
            currTakenBranches += 1
        
        f.write("||\n")
        f.write(f"The hist() function took {100*(currTakenBranches/len(self.histBranchBools))}% of its branches, {currTakenBranches} out of {len(self.histBranchBools)}, during the tests.")
        f.write("\n")
        f.close()



def main():
    test = BranchCovDIY
    test.writeRes(test)

if __name__ == "__main__":
    main()