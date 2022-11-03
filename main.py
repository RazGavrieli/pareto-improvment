from pareto import *

if __name__ == "__main__":
    amiValueList = [1, 2, 3, 4, 5] 
    tamiValueList = [3, 1, 2, 5, 4] 
    ramiValueList = [3, 5, 5, 1, 1] 
    ami = Agent(amiValueList)
    tami = Agent(tamiValueList)
    rami = Agent(ramiValueList)
    agents = [ami, tami, rami]

    for i in range(0,5):
        sum = 0
        currOptions = [item for item in [0,1,2,3,4] if item not in [i]]
        for agent in agents:
            sum += agent.value(i)
        print("option number ",i, "|is pareto optimal: ", isParetoOptimal(agents=agents, option=i, allOptions=currOptions),"|utilitarian sum: ",  sum)
        
        
    print(egalitarian(agents=agents, allOptions=[0,1,2,3,4]))