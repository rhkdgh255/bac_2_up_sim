import random
from prettytable import PrettyTable
from matplotlib import pyplot as plt

# set principle
principle = float(input('设定本金: '))

# starting wager
sw = float(input('设定初始下注(需为最小面额筹码的整数倍): '))

# multiplier when loss
mp = float(input('设定乘数: '))

# take profit (percentage of priciple, 1 indicates doubling the principle)
pl = float(input('设定止盈线(如计划在本金增加50%时停止游戏, 请输入0.5): '))

def play(principle):
    def bet(_wager):
        res = random.randrange(2)
        if res == 0:
            txn.append(txn[-1] + _wager)
            return [sw, 'success']
        elif res == 1:
            txn.append(txn[-1] - _wager)
            return [_wager * mp, 'failure']

    txn = [principle]
    endGame = False
    wager = sw
    while (endGame == False):
        if (txn[-1] < wager):
            wager = 1
        data = bet(wager)
        # print(data[1])
        wager = data[0]
        if (txn[-1] == 0):
            return [txn, 'bankrupt']
        elif (txn[-1] >= principle * (1 + pl)):
            return [txn, 'take profit']

# trial
profitTimes = 0
bankruptTimes = 0
trials = int(input('设定模拟次数, 建议为1000: '))
i = 0
while (i < trials):
    result = play(principle)
    # print(len(result[0]))
    # print(result[1])
    figStat = None
    if result[1] == 'take profit':
        profitTimes += 1
        figStat = 'success'
    elif result[1] == 'bankrupt':
        bankruptTimes += 1
        figStat = 'failure'
    plt.plot(result[0])
    plt.suptitle(f'Change of Balance - Trial {i}',fontsize= 15, fontweight='bold')
    plt.title(f'{principle}-{sw}-{mp}-{pl}-{i}-{figStat}',fontsize= 10)
    plt.xlabel('No. of bets')
    plt.ylabel('Balance')
    plt.savefig(f'./fig/{principle}-{sw}-{mp}-{pl}-{i}.jpg')
    plt.clf()
    i += 1

x = PrettyTable()
x.field_names = ['Earning Counts', 'Bankcruptcy Counts', 'Success Rate', 'Bankruptcy Rate']
x.add_row([profitTimes,trials-profitTimes,profitTimes/trials,1-profitTimes/trials])     
print(x)   
