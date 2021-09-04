import random as rd
import tkinter as tk
import time

window = tk.Tk()
window.title("巨人大战")
window.geometry("2000x1000")

text = tk.Text(window,width=50,height=60,bg="black",fg="white")
text.place(x=1400,y=425,anchor="e")

class Titan:
    def __init__(self,name,health,attack,armor,skill,threshhold):
        self.name = name
        self.health = health
        self.attack = attack
        self.armor = armor
        self.skill = skill
        self.total_health = health
        self.threshhold = threshhold
        
    def Choose(self):
        while True:                                       
            target = rd.choice(Titans)
            if target != self:
                break
        
        self.target = target
        
        text.insert("end",f"{self.name}对{self.target.name}发动了攻击！\n")
        
    def Attack(self):
        self.Choose()
        
        random_attack = rd.randint(self.attack-10, self.attack+10)     
        damage = int(100/(100+self.target.armor)*random_attack)
        self.target.health -= damage
        HealthBar[self.target.name].config(width=int(self.target.health/self.target.total_health*HealthBarWidth))
        DisplayBar[self.target.name].config(text=f"{self.target.health}/{self.target.total_health}")                           
        window.update()
        text.insert("end",f"{self.target.name}受到了{damage}点伤害！还剩{self.target.health}点生命值！\n")
        
        if self.target.health <= 0:
            self.target.Die()
        else:
            self.target.Skill()
        
    def Die(self):
        Titans.remove(self)
        text.insert("end",f"{self.name}阵亡了！\n")
        
class AttackingTitan(Titan):
    def __init__(self, name, health, attack, armor,skill,threshhold):
        Titan.__init__(self, name, health, attack, armor,skill,threshhold)
        self.attack_increase = 50
        
    def Skill(self):
        "生命值小于阈值时，受到伤害增加一定攻击力"
        if self.health <= self.threshhold and self.skill > 0:
            text.insert("end",f"***艾伦发动技能！攻击力增加{self.attack_increase}！***\n")
            self.attack += self.attack_increase
            self.skill -= 1
            
class ArmorTitan(Titan):
    def __init__(self, name, health, attack, armor,skill,threshhold):
        Titan.__init__(self, name, health, attack, armor,skill,threshhold)
        self.armor_increase = 30
        
    def Skill(self):
        "生命值小于阈值时，受到伤害增加一定护甲"
        if self.health <= self.threshhold and self.skill > 0:
            text.insert("end",f"***莱纳发动技能！护甲增加{self.armor_increase}！***\n")
            self.armor += self.armor_increase
            self.skill -= 1 
            
class FemaleTitan(Titan):
    def __init__(self, name, health, attack, armor,skill,threshhold):
        Titan.__init__(self, name, health, attack, armor,skill,threshhold)
        self.HealthSteal = False
        self.health_steal_constant = 100
        
    def Skill(self):
        "生命值小于阈值时，获得一定吸血 "
        if self.health <self.threshhold and self.skill > 0:
            text.insert("end",f"***阿妮发动技能！获得{self.health_steal_constant}%吸血！***\n")
            self.HealthSteal = True
            self.skill -= 1
            
    def Attack(self):
        self.Choose()
             
        random_attack = rd.randint(self.attack-10, self.attack+10)
        damage = int(100/(100+self.target.armor)*random_attack)
        self.target.health -= damage
        HealthBar[self.target.name].config(width=int(self.target.health/self.target.total_health*HealthBarWidth))
        DisplayBar[self.target.name].config(text=f"{self.target.health}/{self.target.total_health}")                           
        window.update()
        text.insert("end",f"{self.target.name}受到了{damage}点伤害！还剩{self.target.health}点生命值！\n")
        
        if self.target.health <= 0:
            self.target.Die()
        else:
            self.target.Skill()
            
        if self.HealthSteal:
            heal = int(damage*self.health_steal_constant/100)
            text.insert("end",f"{self.name}恢复了{heal}点生命值！\n")
            self.health += heal
            
class ColossalTitan(Titan):
    def __init__(self, name, health, attack, armor, skill,threshhold):
        Titan.__init__(self,name, health, attack, armor, skill,threshhold)
        self.times = 5
        
    def Choose(self):
        text.insert("end",f"{self.name}灼烧了所有敌人！\n")
        targets = []
        for target in Titans:
            if target != self:
                targets.append(target)
                
        self.targets = targets
        
    def Attack(self):
        self.Choose()
        
        for target in self.targets:
            random_attack = rd.randint(self.attack-10, self.attack+10)     #计入护甲
            damage = int(100/(100+target.armor)*random_attack)
            target.health -= damage
            HealthBar[target.name].config(width=int(target.health/target.total_health*HealthBarWidth))
            DisplayBar[target.name].config(text=f"{target.health}/{target.total_health}")
            window.update()
            text.insert("end",f"{target.name}受到了{damage}点伤害！还剩{target.health}点生命值！\n")
        
            if target.health <= 0:
                target.Die()
            else:
                target.Skill()
    
    def Skill(self):
        "生命值小于阈值时，连续灼烧数次"
        if self.health < self.threshhold and self.skill > 0:
            text.insert("end",f"***{self.name}发动了技能！灼烧敌人！***\n")
            for i in range(self.times):
                self.Attack()
                
            self.skill -= 1
            
class FoundingTitan(Titan):
    def __init__(self, name, health, attack, armor, skill, threshhold):
        Titan.__init__(self,name, health, attack, armor, skill, threshhold)
        
    def NewChoose(self):
        if len(Titans) > 2:
            while True:                                       
                new_target = rd.choice(Titans)
                if new_target != self and new_target != self.target:
                    break
        
            self.new_target = new_target
        
    def Attack(self):
        self.Choose()
        
        random_attack = rd.randint(self.attack-10, self.attack+10)     
        damage = int(100/(100+self.target.armor)*random_attack)
        self.target.health -= damage
        HealthBar[self.target.name].config(width=int(self.target.health/self.target.total_health*HealthBarWidth))
        DisplayBar[self.target.name].config(text=f"{self.target.health}/{self.target.total_health}")                           
        window.update()
        text.insert("end",f"{self.target.name}受到了{damage}点伤害！还剩{self.target.health}点生命值！\n")
        
        self.NewChoose()
        self.target.target = self.new_target
        text.insert("end",f"{self.name}操控{self.target.name}攻击了{self.new_target.name}!")
        self.target.Attack()
        
    def Skill(self):
        pass
    
healths = {"艾伦":1200,"莱纳":1200,"阿妮":800,"贝尔托特":2000,"尤弥尔":1000}
attacks = {"艾伦":100,"莱纳":50,"阿妮":60,"贝尔托特":30,"尤弥尔":50}
armors = {"艾伦":60,"莱纳":100,"阿妮":70,"贝尔托特":50,"尤弥尔":50}
skills = {"艾伦":2,"莱纳":2,"阿妮":1,"贝尔托特":1,"尤弥尔":0}
threshhold = {"艾伦":500,"莱纳":800,"阿妮":400,"贝尔托特":1000,"尤弥尔":0}

Eren = AttackingTitan("艾伦",healths["艾伦"],attacks["艾伦"],armors["艾伦"],skills["艾伦"],threshhold["艾伦"])
Reiner = ArmorTitan("莱纳",healths["莱纳"],attacks["莱纳"],armors["莱纳"],skills["莱纳"],threshhold["莱纳"])
Annie = FemaleTitan("阿妮",healths["阿妮"],attacks["阿妮"],armors["阿妮"],skills["阿妮"],threshhold["阿妮"])
Bertolt = ColossalTitan("贝尔托特",healths["贝尔托特"],attacks["贝尔托特"],armors["贝尔托特"],skills["贝尔托特"],threshhold["贝尔托特"])
Ymir = FoundingTitan("尤弥尔", healths["尤弥尔"], attacks["尤弥尔"], armors["尤弥尔"], skills["尤弥尔"], threshhold["尤弥尔"])

HealthBarWidth = 100
HealthBar = {"艾伦":tk.Label(window,width=HealthBarWidth,height=2,bg="yellow"),
             "莱纳":tk.Label(window,width=HealthBarWidth,height=2,bg="green"),
             "阿妮":tk.Label(window,width=HealthBarWidth,height=2,bg="blue"),
             "贝尔托特":tk.Label(window,width=HealthBarWidth,height=2,bg="red"),
             "尤弥尔":tk.Label(window,width=HealthBarWidth,height=2,bg="grey"),}
DisplayBarWidth = 8
DisplayBar = {"艾伦":tk.Label(window,width=DisplayBarWidth,height=2,bg="yellow"),
              "莱纳":tk.Label(window,width=DisplayBarWidth,height=2,bg="green"),
              "阿妮":tk.Label(window,width=DisplayBarWidth,height=2,bg="blue"),
              "贝尔托特":tk.Label(window,width=DisplayBarWidth,height=2,bg="red"),
              "尤弥尔":tk.Label(window,width=DisplayBarWidth,height=2,bg="grey"),}

Titans = [Eren,Reiner,Annie,Bertolt,Ymir]

HealthBar["艾伦"].place(x=0,y=1000*1/(len(Titans)+1)-100,anchor="w")
HealthBar["莱纳"].place(x=0,y=1000*2/(len(Titans)+1)-100,anchor="w")
HealthBar["阿妮"].place(x=0,y=1000*3/(len(Titans)+1)-100,anchor="w")
HealthBar["贝尔托特"].place(x=0,y=1000*4/(len(Titans)+1)-100,anchor="w")
HealthBar["尤弥尔"].place(x=0,y=1000*5/(len(Titans)+1)-100,anchor="w")

DisplayBar["艾伦"].place(x=0,y=1000*1/(len(Titans)+1)+30-100,anchor="w")
DisplayBar["莱纳"].place(x=0,y=1000*2/(len(Titans)+1)+30-100,anchor="w")
DisplayBar["阿妮"].place(x=0,y=1000*3/(len(Titans)+1)+30-100,anchor="w")
DisplayBar["贝尔托特"].place(x=0,y=1000*4/(len(Titans)+1)+30-100,anchor="w")
DisplayBar["尤弥尔"].place(x=0,y=1000*5/(len(Titans)+1)+30-100,anchor="w")

def Start():
    text.insert("end","-----=====比赛开始=====-----\n")

    round = 1
    while True:
        global Titans
        rd.shuffle(Titans)
            
        text.insert("end","\n")
        text.insert("end",f"###第{round}回合###\n")
        for Titan in Titans:
            Titan.Attack()
            time.sleep(0.1)
            text.insert("end", "\n")
                
        if len(Titans) == 1:
            text.insert("end",f"战斗结束！{Titans[0].name}获胜!\n")
            break
        
        round += 1
        window.update()

Start = tk.Button(window,text="START",command=Start)
Start.place(x=1000,y=600,anchor="center")
    
window.mainloop()
    