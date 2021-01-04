# Python code
# Defines a simulation for Epic Jewels Chests Drops

def EpicJewelChest(n):
    
    import random
    begin=1
    end=10
    end2=100
    GoldInfATK = PurpleInfATK = BlueInfATK = GreenInfATK = GrayInfATK = 0
    GoldCavATK = PurpleCavATK = BlueCavATK = GreenCavATK = GrayCavATK = 0
    GoldRanATK = PurpleRanATK = BlueRanATK = GreenRanATK = GrayRanATK = 0
    GoldInfDEF = PurpleInfDEF = BlueInfDEF = GreenInfDEF = GrayInfDEF = 0
    GoldCavDEF = PurpleCavDEF = BlueCavDEF = GreenCavDEF = GrayCavDEF = 0
    GoldRanDEF = PurpleRanDEF = BlueRanDEF = GreenRanDEF = GrayRanDEF = 0
    GoldSieATK = PurpleSieATK = BlueSieATK = GreenSieATK = GraySieATK = 0
    GoldWallDEF = PurpleWallDEF = BlueWallDEF = GreenWallDEF = GrayWallDEF = 0
    GoldTrapATK = PurpleTrapATK = BlueTrapATK = GreenTrapATK = GrayTrapATK = 0
    GoldTrapDEF = PurpleTrapDEF = BlueTrapDEF = GreenTrapDEF = GrayTrapDEF = 0
    
    for i in range(n):
        TipoGema=random.randint(begin,end)
        ChestDropQuality=random.randint(begin,end2)
        if ChestDropQuality > 95: #Purple
            if TipoGema == 1:
                PurpleInfATK+=1
            elif TipoGema == 2:
                PurpleCavATK+=1
            elif TipoGema == 3:
                PurpleRanATK+=1
            elif TipoGema == 4:
                PurpleInfDEF+=1
            elif TipoGema == 5:
                PurpleCavDEF+=1
            elif TipoGema == 6:
                PurpleRanDEF+=1
            elif TipoGema == 7:
                PurpleSieATK+=1
            elif TipoGema == 8:
                PurpleWallDEF+=1
            elif TipoGema == 9:
                PurpleTrapATK+=1
            else:
                PurpleTrapDEF+=1
                
        elif ChestDropQuality > 80: #Blue
            if TipoGema == 1:
                BlueInfATK+=1
            elif TipoGema == 2:
                BlueCavATK+=1
            elif TipoGema == 3:
                BlueRanATK+=1
            elif TipoGema == 4:
                BlueInfDEF+=1
            elif TipoGema == 5:
                BlueCavDEF+=1
            elif TipoGema == 6:
                BlueRanDEF+=1
            elif TipoGema == 7:
                BlueSieATK+=1
            elif TipoGema == 8:
                BlueWallDEF+=1
            elif TipoGema == 9:
                BlueTrapATK+=1
            else:
                BlueTrapDEF+=1
                
        else: #Green
            if TipoGema == 1:
                GreenInfATK+=1
            elif TipoGema == 2:
                GreenCavATK+=1
            elif TipoGema == 3:
                GreenRanATK+=1
            elif TipoGema == 4:
                GreenInfDEF+=1
            elif TipoGema == 5:
                GreenCavDEF+=1
            elif TipoGema == 6:
                GreenRanDEF+=1
            elif TipoGema == 7:
                GreenSieATK+=1
            elif TipoGema == 8:
                GreenWallDEF+=1
            elif TipoGema == 9:
                GreenTrapATK+=1
            else:
                GreenTrapDEF+=1
            
    InfATK=(GoldInfATK*256)+(PurpleInfATK*64)+(BlueInfATK*16)+(GreenInfATK*4)+(GrayInfATK)
    CavATK=(GoldCavATK*256)+(PurpleCavATK*64)+(BlueCavATK*16)+(GreenCavATK*4)+(GrayCavATK)
    RanATK=(GoldRanATK*256)+(PurpleRanATK*64)+(BlueRanATK*16)+(GreenRanATK*4)+(GrayRanATK)
    InfDEF=(GoldInfDEF*256)+(PurpleInfDEF*64)+(BlueInfDEF*16)+(GreenInfDEF*4)+(GrayInfDEF)
    CavDEF=(GoldCavDEF*256)+(PurpleCavDEF*64)+(BlueCavDEF*16)+(GreenCavDEF*4)+(GrayCavDEF)
    RanDEF=(GoldRanDEF*256)+(PurpleRanDEF*64)+(BlueRanDEF*16)+(GreenRanDEF*4)+(GrayRanDEF)
    SieATK=(GoldSieATK*256)+(PurpleSieATK*64)+(BlueSieATK*16)+(GreenSieATK*4)+(GraySieATK)
    WallDEF=(GoldWallDEF*256)+(PurpleWallDEF*64)+(BlueWallDEF*16)+(GreenWallDEF*4)+(GrayWallDEF)
    TrapATK=(GoldTrapATK*256)+(PurpleTrapATK*64)+(BlueTrapATK*16)+(GreenTrapATK*4)+(GrayTrapATK)
    TrapDEF=(GoldTrapDEF*256)+(PurpleTrapDEF*64)+(BlueTrapDEF*16)+(GreenTrapDEF*4)+(GrayTrapDEF)

    print("InfATK",InfATK)
    print("CavATK",CavATK)
    print("RanATK",RanATK)
    print("InfDEF",InfDEF)
    print("CavDEF",CavDEF)
    print("RanDEF",RanDEF)
    print("SieATK",SieATK)
    print("WallDEF",WallDEF)
    print("TrapATK",TrapATK)
    print("TrapDEF",TrapDEF)

n=int(input("Amount of Epic Jewel chests: "))
EpicJewelChest(n)
