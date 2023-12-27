class StarRail:
    """
    Star Rail 抽卡记录辅助程序
    """

    def __init__(self):
        """
        构造函数，初始化抽卡系统的起始状态。
        """
        self.starFrom = 0
        self.tenStarFrom = 0
        self.goldCharacter = 90
        self.goldWeapon = 80
        self.selectedOption = None
        self.threeStar = 0
        self.fourStar = 0
        self.fiveStar = 0
        self.res = None
        self.totDrawWithinProtection = 0

        print("欢迎来到星穷列车抽卡记录仪~")
        self.poolSelection()

    def poolSelection(self):
        poolSelected = False

        while not poolSelected:
            try:
                self.selectedOption = int(input("你要选择角色卡池还是光锥卡池。\n1. 角色卡池\n2. 光锥卡池\n"))
                if self.selectedOption not in [1, 2]:
                    print("请输入1或者2。")
                    continue
            except ValueError:
                print("无效输入，请输入1或者2。")
                continue

            if self.selectedOption == 1:
                self.starCharacterGacha(self.goldCharacter)
                break
            elif self.selectedOption == 2:
                self.starCharacterGacha(self.goldWeapon)
                break

    def pooSetting(self):
        isStarGacha = False
        while not isStarGacha:
            try:
                if self.selectedOption == 1:
                    self.starFrom = int(input("请问角色卡池已经抽了多少抽？\n"))
                    self.totDrawWithinProtection = self.starFrom
                    if self.starFrom not in range(0, 90):
                        print("请输入0到89哦！")
                        continue
                    else:
                        break
                else:
                    self.starFrom = int(input("请问光锥卡池卡池已经抽了多少抽？\n"))
                    self.totDrawWithinProtection = self.starFrom
                    if self.starFrom not in range(0, 80):
                        print("请输入0到79哦！")
                        continue
                    else:
                        break
            except:
                print("无效输入，请输入数字。")
                continue

        isStarGacha = False
        while not isStarGacha:
            try:
                self.tenStarFrom = int(input("10连出紫抽了多少抽？\n"))
                if self.tenStarFrom not in range(0, 10):
                    print("请输入0到10哦！")
                    continue
                else:
                    break

            except:
                print("无效输入，请输入数字。")
                continue

    def starCharacterGacha(self, pool):
        """使用continue使while循环进入下一次迭代"""
        self.pooSetting()
        print(f"抽卡开始，以开拓之名！(设置：角色池，已抽：{self.starFrom} 十连出紫抽数：{self.tenStarFrom})")

        toAceProtect = pool - self.totDrawWithinProtection
        if toAceProtect == 1:
            print("恭喜保底人， 下一抽必出金！")

        isAce = False
        while not isAce:
            try:
                self.res = int(input("请选择本次结果：\n1. 3★\n2. 4★\n3. 5★\n4. End\n"))
                if self.res not in range(1, 5):
                    print("请输入1到3哦！")
                    continue
                if toAceProtect == 1 and not (self.res == 3 or self.res == 4):
                    print("本抽是金色保底，必出金★★★★★请选择3")
                    continue
                elif self.tenStarFrom == 9 and not (self.res == 2 or self.res == 3 or self.res == 4):
                    print("本抽是十连保底，出金还是出紫呢？ 请选择2或者3.")
                    continue
            except:
                print("无效输入，请输入数字。")
                continue

            self.totDrawWithinProtection += 1

            if self.res == 1:
                self.threeStar += 1
                self.tenStarFrom += 1
            elif self.res == 2:
                self.fourStar += 1
                self.tenStarFrom = 0
            elif self.res == 3:
                self.fiveStar += 1
                self.tenStarFrom = 0
                self.totDrawWithinProtection = 0

            totDraw = self.threeStar + self.fourStar + self.fiveStar
            totOneRoundDraw = self.totDrawWithinProtection % pool
            toAceProtect = pool - totOneRoundDraw
            toFourStarProtection = 10 - self.tenStarFrom % 10

            if self.res == 4:
                print(
                    f"本轮抽卡共抽：{totDraw}, 出金数量：{self.fiveStar}, 出紫数量：{self.fourStar}, 出蓝数量：{self.threeStar}")
                break

            if toAceProtect == 1:
                print("恭喜保底人， 下一抽必出金！")

            print(
                f"本轮抽卡到目前为止共抽：{totDraw}\n保底内一共抽了：{totOneRoundDraw}\n距离保底还差：{toAceProtect}\n距离紫卡保底还差：{toFourStarProtection}\n出金数量：{self.fiveStar}, 出紫数量：{self.fourStar}, 出蓝数量：{self.threeStar}\n")


# Init gacha
starRailGacha = StarRail()
