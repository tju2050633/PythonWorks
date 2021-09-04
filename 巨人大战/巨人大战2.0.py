from random import*
from tkinter import*
from time import*

#窗口
window = Tk()
window.title("巨人大战")
window.geometry("2000x1000")

text = Text(window,width=50,height=60,bg="black",fg="white")
text.place(x=1400,y=425,anchor="e")

#巨人类
class Titan:
    def __init__(self,name,health,attack,armor,skill):
        self.name = name
        self.health = health
        self.attack = attack
        self.armor = armor
        self.skill = skill
        self.total_health = health
        
    def Attack(self):
        "攻击方法"
        while True:                                       #随机选择目标（target）
            target = choice(Titans)
            if target != self:
                break
            
        text.insert("end",f"{self.name}对{target.name}发动了攻击！\n")
            
        random_attack = randint(self.attack-10, self.attack+10)     #计入护甲
        damage = int(100/(100+target.armor)*random_attack)
        target.health -= damage
        HealthBar[target.name].config(width=int(target.health/target.total_health*HealthBarWidth),
                                    text=f"{target.health}/{target.total_health}")
        window.update()
        text.insert("end",f"{target.name}受到了{damage}点伤害！还剩{target.health}点生命值！\n")
        
        if target.health <= 0:
            target.Die()
        else:
            target.Skill()
        
    def Die(self):
        Titans.remove(self)
        text.insert("end",f"{self.name}阵亡了！\n")
        
#九大巨人类
class AttackingTitan(Titan):
    "进击的巨人"
    def __init__(self, name, health, attack, armor,skill):
        Titan.__init__(self, name, health, attack, armor,skill)
        
    def Skill(self):
        "生命值小于阈值时，受到伤害增加一定攻击力"
        threshhold = 500
        attack_increase = 50
        if self.health <= threshhold and self.skill > 0:
            text.insert("end",f"***艾伦发动技能！攻击力增加{attack_increase}！***\n")
            self.attack += attack_increase
            self.skill -= 1
            
class ArmorTitan(Titan):
    def __init__(self, name, health, attack, armor,skill):
        Titan.__init__(self, name, health, attack, armor,skill)
        
    def Skill(self):
        "生命值小于阈值时，受到伤害增加一定护甲"
        threshhold = 800
        armor_increase = 30
        if self.health <= threshhold and self.skill > 0:
            text.insert("end",f"***莱纳发动技能！护甲增加{armor_increase}！***\n")
            self.armor += armor_increase
            self.skill -= 1 
            
class FemaleTitan(Titan):
    def __init__(self, name, health, attack, armor,skill):
        Titan.__init__(self, name, health, attack, armor,skill)
        self.HealthSteal = False
        
    def Skill(self):
        "生命值小于阈值时，获得一定吸血 "
        threshhold = 400
        global health_steal_constant
        health_steal_constant = 50
        if self.health <threshhold and self.skill > 0:
            text.insert("end",f"***阿妮发动技能！获得{health_steal_constant}%吸血！***\n")
            self.HealthSteal = True
            self.skill -= 1
            
    def Attack(self):
        while True:                                       
            target = choice(Titans)
            if target != self:
                break
            
        text.insert("end",f"{self.name}对{target.name}发动了攻击！\n")
             
        random_attack = randint(self.attack-10, self.attack+10)
        damage = int(100/(100+target.armor)*random_attack)
        target.health -= damage
        HealthBar[target.name].config(width=int(target.health/target.total_health*HealthBarWidth),
                                    text=f"{target.health}/{target.total_health}")
        window.update()
        text.insert("end",f"{target.name}受到了{damage}点伤害！还剩{target.health}点生命值！\n")
        
        if target.health <= 0:
            target.Die()
        else:
            target.Skill()
            
        if self.HealthSteal:
            heal = int(damage*health_steal_constant/100)
            text.insert("end",f"{self.name}恢复了{heal}点生命值！\n")
            self.health += heal
            
class ColossalTitan(Titan):
    def __init__(self, name, health, attack, armor, skill):
        Titan.__init__(self,name, health, attack, armor, skill)
        
    def Attack(self):
        text.insert("end",f"{self.name}灼烧了所有敌人！\n")
        targets = []
        for target in Titans:
            if target != self:
                targets.append(target)
        
        for target in targets:
            random_attack = randint(self.attack-10, self.attack+10)     #计入护甲
            damage = int(100/(100+target.armor)*random_attack)
            target.health -= damage
            HealthBar[target.name].config(width=int(target.health/target.total_health*HealthBarWidth),
                                    text=f"{target.health}/{target.total_health}")
            window.update()
            text.insert("end",f"{target.name}受到了{damage}点伤害！还剩{target.health}点生命值！\n")
        
            if target.health <= 0:
                target.Die()
            else:
                target.Skill()
    
    def Skill(self):
        "生命值小于阈值时，连续灼烧数次"
        threshhold = 1000
        times = 5
        if self.health < threshhold and self.skill > 0:
            text.insert("end",f"***{self.name}发动了技能！灼烧敌人！***\n")
            for i in range(times):
                self.Attack()
                
            self.skill -= 1
    
#继承者类
healths = {"艾伦":1200,"莱纳":1200,"阿妮":800,"贝尔托特":2000}
attacks = {"艾伦":100,"莱纳":50,"阿妮":60,"贝尔托特":30}
armors = {"艾伦":60,"莱纳":100,"阿妮":70,"贝尔托特":50}
skills = {"艾伦":2,"莱纳":2,"阿妮":1,"贝尔托特":1}

Eren = AttackingTitan("艾伦",healths["艾伦"],attacks["艾伦"],armors["艾伦"],skills["艾伦"])
Reiner = ArmorTitan("莱纳",healths["莱纳"],attacks["莱纳"],armors["莱纳"],skills["莱纳"])
Annie = FemaleTitan("阿妮",healths["阿妮"],attacks["阿妮"],armors["阿妮"],skills["阿妮"])
Bertolt = ColossalTitan("贝尔托特",healths["贝尔托特"],attacks["贝尔托特"],armors["贝尔托特"],skills["贝尔托特"])

HealthBarWidth = 100
HealthBar = {"艾伦":Label(window,width=HealthBarWidth,height=2,bg="yellow"),
             "莱纳":Label(window,width=HealthBarWidth,height=2,bg="green"),
             "阿妮":Label(window,width=HealthBarWidth,height=2,bg="blue"),
             "贝尔托特":Label(window,width=HealthBarWidth,height=2,bg="red")}
HealthBar["艾伦"].place(x=0,y=200,anchor="w")
HealthBar["莱纳"].place(x=0,y=400,anchor="w")
HealthBar["阿妮"].place(x=0,y=600,anchor="w")
HealthBar["贝尔托特"].place(x=0,y=800,anchor="w")

#战斗环节

Titans = [Eren,Reiner,Annie,Bertolt]
def Start():
    text.insert("end","-----=====比赛开始=====-----\n")

    round = 1
    while True:
        global Titans
        shuffle(Titans)
            
        text.insert("end","\n")
        text.insert("end",f"###第{round}回合###\n")
        for Titan in Titans:
            Titan.Attack()
                
        if len(Titans) == 1:
            text.insert("end",f"战斗结束！{Titans[0].name}获胜!\n")
            break
        
        round += 1
        window.update()
        sleep(0.5)

Start = Button(window,text="START",command=Start)
Start.place(x=1000,y=600,anchor="center")
    
window.mainloop()
    