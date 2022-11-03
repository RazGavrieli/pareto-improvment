class Agent:
    def __init__(self, values:list[int]) -> None:
        self.__values = values

    def value(self, option:int) -> float:
        """
        INPUT: The index of an option
        OUTPUT: The value of the option (to the agent).
        """
        return self.__values[option]

def isParetoImprovment(agents:list[Agent], option1:int, option2:int) -> bool:
    """
    Option1 is called "Pareto Improvment" to option2 if it benefits 
    at least one person without making it worse for anyone else.
    """
    # return False if at least one agent loses on the option2
    for agent in agents:
        if agent.value(option1) < agent.value(option2):
            return False
            
    # return False if none of the agents gains anything
    for agent in agents:
        if agent.value(option1) > agent.value(option2):
            return True

    # return false because both options are the same (therefore, can't be an improvment)
    return False

def isParetoOptimal(agents:list[Agent], option:int, allOptions:list[int]) -> bool:
    """
    option is Pareto Optimal (aka Pareto Efficient) if none of the other 
    options (allOptions) are Pareto Improvment to it.
    """
    for otherOption in allOptions:
        if isParetoImprovment(agents=agents, option1=otherOption, option2=option):
            return False
    return True

def egalitarian(agents:list[Agent], allOptions:list[int]=[0,1,2,3,4]) -> int:
    z=0
    maxMin = -1
    for i in allOptions:
        currMin = 99999
        for agent in agents:
            if agent.value(i) < currMin:
                currMin = agent.value(i)
        if currMin > maxMin:
            maxMin = currMin
            z = i

    return z


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
        print(i, isParetoOptimal(agents=agents, option=i, allOptions=currOptions), sum)
        
        
    print(egalitarian(agents=agents, allOptions=[0,1,2,3,4]))

    
