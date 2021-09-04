import random as rd
import tkinter as tk
import time

window = tk.Tk()
window.title("巨人大战")
window.geometry("2000x1000")

text = tk.Text(window,width=50,height=60,bg="black",fg="white")
text.place(x=1400,y=425,anchor="e")

class Titan:
    def __init__(self,name,health,attack,armor,skill,threshhold,heal):
        self.name = name
        self.health = health
        self.attack = attack
        self.armor = armor
        self.skill = skill
        self.total_health = health
        self.threshhold = threshhold
        self.heal = heal
        
        self.total_damage = 0
        self.total_suffer = 0
        self.total_heal = 0
        
    def Choose(self):
        while True:                                       
            target = rd.choice(Titans)
            if target != self:
                break
        
        self.target = target
        
        text.insert("end",f"{self.name}对{self.target.name}发动了攻击！\n")
        
    def Attack(self):
        #选择目标，算出伤害，目标承伤
        self.Choose()
        random_attack = rd.randint(self.attack-10, self.attack+10)
        damage = int(100/(100+self.target.armor)*random_attack)
        self.total_damage += damage
        DisplayedDamage[f"{self.name}"].set(f"总输出：{self.total_damage}")
        self.target.Suffer(damage)
        
        #每次攻击完固定恢复
        if self.health + self.heal > self.total_health:
            remained_heal = self.total_health - self.health
            self.health += remained_heal
            HealthBar[self.name].config(width=int(self.health/self.total_health*HealthBarWidth))
            DisplayedHealth[f"{self.name}"].set(f"血量：{self.health}/{self.total_health}")
            
            self.total_heal += remained_heal
            DisplayedHeal[f"{self.name}"].set(f"总恢复：{self.total_heal}")
            
            if remained_heal > 0:
                text.insert("end",f"{self.name}恢复了{remained_heal}点生命值！\n")
            
        else:
            self.health += self.heal
            HealthBar[self.name].config(width=int(self.health/self.total_health*HealthBarWidth))
            DisplayedHealth[f"{self.name}"].set(f"血量：{self.health}/{self.total_health}")
            
            self.total_heal += self.heal
            DisplayedHeal[f"{self.name}"].set(f"总恢复：{self.total_heal}")
            
            text.insert("end",f"{self.name}恢复了{self.heal}点生命值！\n")
            
    def Suffer(self,damage):
        self.health -= damage
        self.total_suffer += damage
        HealthBar[self.name].config(width=int(self.health/self.total_health*HealthBarWidth))
        
        DisplayedHealth[f"{self.name}"].set(f"血量：{self.health}/{self.total_health}")
        DisplayedSuffer[f"{self.name}"].set(f"总承伤：{self.total_suffer}")
                           
        window.update()
        text.insert("end",f"{self.name}受到了{damage}点伤害！还剩{self.health}点生命值！\n")
        
        if self.health <= 0:
            self.Die()
        else:
            self.Skill()
        
    def Die(self):
        Titans.remove(self)
        text.insert("end",f"{self.name}阵亡了！\n")
        
class AttackingTitan(Titan):
    def __init__(self, name, health, attack, armor,skill,threshhold,heal):
        Titan.__init__(self, name, health, attack, armor,skill,threshhold,heal)
        self.attack_increase = 50
        
    def Skill(self):
        if self.health <= self.threshhold and self.skill > 0:
            text.insert("end",f"***艾伦发动技能！攻击力增加{self.attack_increase}！***\n")
            self.attack += self.attack_increase
            DisplayedAttack["艾伦"].set(f"攻击力：{self.attack}")
            self.skill -= 1
            DisplayedSkill["艾伦"].set(f"剩余技能次数：{self.skill}")
            
class ArmorTitan(Titan):
    def __init__(self, name, health, attack, armor,skill,threshhold,heal):
        Titan.__init__(self, name, health, attack, armor,skill,threshhold,heal)
        self.armor_increase = 30
        
    def Skill(self):
        if self.health <= self.threshhold and self.skill > 0:
            text.insert("end",f"***莱纳发动技能！护甲增加{self.armor_increase}！***\n")
            self.armor += self.armor_increase
            DisplayedArmor["莱纳"].set(f"护甲：{self.armor}")
            self.skill -= 1 
            DisplayedSkill["莱纳"].set(f"剩余技能次数：{self.skill}")
            
class FemaleTitan(Titan):
    def __init__(self, name, health, attack, armor,skill,threshhold,heal):
        Titan.__init__(self, name, health, attack, armor,skill,threshhold,heal)
        self.HealthSteal = False
        self.health_steal_constant = 100
        
    def Skill(self):
        if self.health <self.threshhold and self.skill > 0:
            text.insert("end",f"***阿妮发动技能！获得{self.health_steal_constant}%吸血！***\n")
            self.HealthSteal = True
            self.skill -= 1
            DisplayedSkill["阿妮"].set(f"剩余技能次数：{self.skill}")
            
    def Attack(self):
        self.Choose()
             
        random_attack = rd.randint(self.attack-10, self.attack+10)
        damage = int(100/(100+self.target.armor)*random_attack)
        self.total_damage += damage
        DisplayedDamage[f"{self.name}"].set(f"总输出：{self.total_damage}")
        self.target.Suffer(damage)
        
        if self.health + self.heal > self.total_health:
            remained_heal = self.total_health - self.health
            self.health += remained_heal
            HealthBar[self.name].config(width=int(self.health/self.total_health*HealthBarWidth))
            DisplayedHealth[f"{self.name}"].set(f"血量：{self.health}/{self.total_health}")
            
            self.total_heal += remained_heal
            DisplayedHeal[f"{self.name}"].set(f"总恢复：{self.total_heal}")
            
            if remained_heal > 0:
                text.insert("end",f"{self.name}恢复了{remained_heal}点生命值！\n")
            
        else:
            self.health += self.heal
            HealthBar[self.name].config(width=int(self.health/self.total_health*HealthBarWidth))
            DisplayedHealth[f"{self.name}"].set(f"血量：{self.health}/{self.total_health}")
            
            self.total_heal += self.heal
            DisplayedHeal[f"{self.name}"].set(f"总恢复：{self.total_heal}")
            
            text.insert("end",f"{self.name}恢复了{self.heal}点生命值！\n")
            
        if self.HealthSteal and self.health < self.threshhold:
            heal = int(damage*self.health_steal_constant/100)
            
            if self.health + heal > self.total_health:
                remained_heal = self.total_health - self.health
                self.health += remained_heal
                HealthBar[self.name].config(width=int(self.health/self.total_health*HealthBarWidth))
                DisplayedHealth[f"{self.name}"].set(f"血量：{self.health}/{self.total_health}")
                
                self.total_heal += remained_heal
                DisplayedHeal[f"{self.name}"].set(f"总恢复：{self.total_heal}")
                
                if remained_heal > 0:
                    text.insert("end",f"{self.name}恢复了{remained_heal}点生命值！\n")
            
            else:
                self.health += heal
                HealthBar[self.name].config(width=int(self.health/self.total_health*HealthBarWidth))
                DisplayedHealth[f"{self.name}"].set(f"血量：{self.health}/{self.total_health}")
                
                self.total_heal += heal
                DisplayedHeal[f"{self.name}"].set(f"总恢复：{self.total_heal}")
                
                text.insert("end",f"{self.name}通过吸血恢复了{self.heal}点生命值！\n")
            
class ColossalTitan(Titan):
    def __init__(self, name, health, attack, armor, skill,threshhold,heal):
        Titan.__init__(self,name, health, attack, armor, skill,threshhold,heal)
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
            random_attack = rd.randint(self.attack-10, self.attack+10)
            damage = int(100/(100+target.armor)*random_attack)
            self.total_damage += damage
            DisplayedDamage[f"{self.name}"].set(f"总输出：{self.total_damage}")
            target.Suffer(damage)
            
        if self.health + self.heal > self.total_health:
            remained_heal = self.total_health - self.health
            self.health += remained_heal
            HealthBar[self.name].config(width=int(self.health/self.total_health*HealthBarWidth))
            DisplayedHealth[f"{self.name}"].set(f"血量：{self.health}/{self.total_health}")
            
            self.total_heal += remained_heal
            DisplayedHeal[f"{self.name}"].set(f"总恢复：{self.total_heal}")
            
            if remained_heal > 0:
                text.insert("end",f"{self.name}恢复了{remained_heal}点生命值！\n")
            
        else:
            self.health += self.heal
            HealthBar[self.name].config(width=int(self.health/self.total_health*HealthBarWidth))
            DisplayedHealth[f"{self.name}"].set(f"血量：{self.health}/{self.total_health}")
            
            self.total_heal += self.heal
            DisplayedHeal[f"{self.name}"].set(f"总恢复：{self.total_heal}")
            
            text.insert("end",f"{self.name}恢复了{self.heal}点生命值！\n")
        
           
    def Skill(self):
        if self.health < self.threshhold and self.skill > 0:
            text.insert("end",f"***{self.name}发动了技能！灼烧敌人！***\n")
            for i in range(self.times):
                self.Attack()
                
            self.skill -= 1
            DisplayedSkill["贝尔托特"].set(f"剩余技能次数：{self.skill}")
            
class FoundingTitan(Titan):
    def __init__(self, name, health, attack, armor, skill, threshhold,heal):
        Titan.__init__(self,name, health, attack, armor, skill, threshhold,heal)
        self.new_target = False
        
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
        self.total_damage += damage
        DisplayedDamage[f"{self.name}"].set(f"总输出：{self.total_damage}")
        self.target.Suffer(damage)
        
        self.NewChoose()
        if self.new_target:
            text.insert("end",f"{self.name}操控{self.target.name}攻击了{self.new_target.name}!\n")
        
            random_attack = rd.randint(self.target.attack-10, self.target.attack+10)
            damage = int(100/(100+self.new_target.armor)*random_attack)
            self.total_damage += damage
            DisplayedDamage[f"{self.name}"].set(f"总输出：{self.total_damage}")
            self.new_target.Suffer(damage)
            self.new_target = False
            
        if self.health + self.heal > self.total_health:
            remained_heal = self.total_health - self.health
            self.health += remained_heal
            HealthBar[self.name].config(width=int(self.health/self.total_health*HealthBarWidth))
            DisplayedHealth[f"{self.name}"].set(f"血量：{self.health}/{self.total_health}")
            
            self.total_heal += remained_heal
            DisplayedHeal[f"{self.name}"].set(f"总恢复：{self.total_heal}")
            
            if remained_heal > 0:
                text.insert("end",f"{self.name}恢复了{remained_heal}点生命值！\n")
            
        else:
            self.health += self.heal
            HealthBar[self.name].config(width=int(self.health/self.total_health*HealthBarWidth))
            DisplayedHealth[f"{self.name}"].set(f"血量：{self.health}/{self.total_health}")
            
            self.total_heal += self.heal
            DisplayedHeal[f"{self.name}"].set(f"总恢复：{self.total_heal}")
            
            text.insert("end",f"{self.name}恢复了{self.heal}点生命值！\n")
        
    def Skill(self):
        pass
    
healths = {"艾伦":1000,"莱纳":1200,"阿妮":800,"贝尔托特":2000,"尤弥尔":1400}
attacks = {"艾伦":100,"莱纳":50,"阿妮":60,"贝尔托特":30,"尤弥尔":50}
armors = {"艾伦":60,"莱纳":100,"阿妮":70,"贝尔托特":50,"尤弥尔":50}
skills = {"艾伦":2,"莱纳":2,"阿妮":1,"贝尔托特":1,"尤弥尔":0}
threshhold = {"艾伦":500,"莱纳":800,"阿妮":400,"贝尔托特":1000,"尤弥尔":0}
heal = {"艾伦":20,"莱纳":12,"阿妮":30,"贝尔托特":20,"尤弥尔":20}

Eren = AttackingTitan("艾伦",healths["艾伦"],attacks["艾伦"],armors["艾伦"],skills["艾伦"],threshhold["艾伦"],heal["艾伦"])
Reiner = ArmorTitan("莱纳",healths["莱纳"],attacks["莱纳"],armors["莱纳"],skills["莱纳"],threshhold["莱纳"],heal["莱纳"])
Annie = FemaleTitan("阿妮",healths["阿妮"],attacks["阿妮"],armors["阿妮"],skills["阿妮"],threshhold["阿妮"],heal["阿妮"])
Bertolt = ColossalTitan("贝尔托特",healths["贝尔托特"],attacks["贝尔托特"],armors["贝尔托特"],skills["贝尔托特"],threshhold["贝尔托特"],heal["贝尔托特"])
Ymir = FoundingTitan("尤弥尔", healths["尤弥尔"], attacks["尤弥尔"], armors["尤弥尔"], skills["尤弥尔"], threshhold["尤弥尔"],heal["尤弥尔"])

HealthBarWidth = 100
HealthBar = {"艾伦":tk.Label(window,width=HealthBarWidth,height=2,bg="yellow"),
             "莱纳":tk.Label(window,width=HealthBarWidth,height=2,bg="green"),
             "阿妮":tk.Label(window,width=HealthBarWidth,height=2,bg="blue"),
             "贝尔托特":tk.Label(window,width=HealthBarWidth,height=2,bg="red"),
             "尤弥尔":tk.Label(window,width=HealthBarWidth,height=2,bg="grey"),
             }

DisplayBarWidth = 12
DisplayedHealth = {"艾伦":tk.StringVar(window,f"血量：{Eren.health}/{Eren.health}"),
                   "莱纳":tk.StringVar(window,f"血量：{Reiner.health}/{Reiner.health}"),
                   "阿妮":tk.StringVar(window,f"血量：{Annie.health}/{Annie.health}"),
                   "贝尔托特":tk.StringVar(window,f"血量：{Bertolt.health}/{Bertolt.health}"),
                   "尤弥尔":tk.StringVar(window,f"血量：{Ymir.health}/{Ymir.health}"),
                   }

DisplayedAttack = {"艾伦":tk.StringVar(window,f"攻击力：{Eren.attack}"),
                   "莱纳":tk.StringVar(window,f"攻击力：{Reiner.attack}"),
                   "阿妮":tk.StringVar(window,f"攻击力：{Annie.attack}"),
                   "贝尔托特":tk.StringVar(window,f"攻击力：{Bertolt.attack}"),
                   "尤弥尔":tk.StringVar(window,f"攻击力：{Ymir.attack}"),
                   }

DisplayedArmor = {"艾伦":tk.StringVar(window,f"护甲：{Eren.armor}"),
                   "莱纳":tk.StringVar(window,f"护甲：{Reiner.armor}"),
                   "阿妮":tk.StringVar(window,f"护甲：{Annie.armor}"),
                   "贝尔托特":tk.StringVar(window,f"护甲：{Bertolt.armor}"),
                   "尤弥尔":tk.StringVar(window,f"护甲：{Ymir.armor}"),
                   }

DisplayedSkill = {"艾伦":tk.StringVar(window,f"剩余技能次数：{Eren.skill}"),
                   "莱纳":tk.StringVar(window,f"剩余技能次数：{Reiner.skill}"),
                   "阿妮":tk.StringVar(window,f"剩余技能次数：{Annie.skill}"),
                   "贝尔托特":tk.StringVar(window,f"剩余技能次数：{Bertolt.skill}"),
                   "尤弥尔":tk.StringVar(window,f"剩余技能次数：{Ymir.skill}"),
                   }

DisplayedDamage = {"艾伦":tk.StringVar(window,"总输出：0"),
                   "莱纳":tk.StringVar(window,"总输出：0"),
                   "阿妮":tk.StringVar(window,"总输出：0"),
                   "贝尔托特":tk.StringVar(window,"总输出：0"),
                   "尤弥尔":tk.StringVar(window,"总输出：0"),
                   }

DisplayedSuffer = {"艾伦":tk.StringVar(window,"总承伤：0"),
                   "莱纳":tk.StringVar(window,"总承伤：0"),
                   "阿妮":tk.StringVar(window,"总承伤：0"),
                   "贝尔托特":tk.StringVar(window,"总承伤：0"),
                   "尤弥尔":tk.StringVar(window,"总承伤：0"),
                   }

DisplayedHeal = {"艾伦":tk.StringVar(window,"总恢复：0"),
                   "莱纳":tk.StringVar(window,"总恢复：0"),
                   "阿妮":tk.StringVar(window,"总恢复：0"),
                   "贝尔托特":tk.StringVar(window,"总恢复：0"),
                   "尤弥尔":tk.StringVar(window,"总恢复：0"),
                   }

NameDisplayBar = {"艾伦":tk.Label(window,width=DisplayBarWidth,height=2,bg="yellow",text="艾伦:进击的巨人"),
              "莱纳":tk.Label(window,width=DisplayBarWidth,height=2,bg="green",text="莱纳:铠之巨人"),
              "阿妮":tk.Label(window,width=DisplayBarWidth,height=2,bg="blue",text="阿妮:女巨人"),
              "贝尔托特":tk.Label(window,width=DisplayBarWidth,height=2,bg="red",text="贝尔托特:超大型巨人"),
              "尤弥尔":tk.Label(window,width=DisplayBarWidth,height=2,bg="grey",text="尤弥尔:始祖巨人"),
              }

HealthDisplayBar = {"艾伦":tk.Label(window,width=DisplayBarWidth,height=2,bg="yellow",textvariable=DisplayedHealth["艾伦"]),
              "莱纳":tk.Label(window,width=DisplayBarWidth,height=2,bg="green",textvariable=DisplayedHealth["莱纳"]),
              "阿妮":tk.Label(window,width=DisplayBarWidth,height=2,bg="blue",textvariable=DisplayedHealth["阿妮"]),
              "贝尔托特":tk.Label(window,width=DisplayBarWidth,height=2,bg="red",textvariable=DisplayedHealth["贝尔托特"]),
              "尤弥尔":tk.Label(window,width=DisplayBarWidth,height=2,bg="grey",textvariable=DisplayedHealth["尤弥尔"]),
              }

AttackDisplayBar = {"艾伦":tk.Label(window,width=DisplayBarWidth,height=2,bg="yellow",textvariable=DisplayedAttack["艾伦"]),
              "莱纳":tk.Label(window,width=DisplayBarWidth,height=2,bg="green",textvariable=DisplayedAttack["莱纳"]),
              "阿妮":tk.Label(window,width=DisplayBarWidth,height=2,bg="blue",textvariable=DisplayedAttack["阿妮"]),
              "贝尔托特":tk.Label(window,width=DisplayBarWidth,height=2,bg="red",textvariable=DisplayedAttack["贝尔托特"]),
              "尤弥尔":tk.Label(window,width=DisplayBarWidth,height=2,bg="grey",textvariable=DisplayedAttack["尤弥尔"]),
              }

ArmorDisplayBar = {"艾伦":tk.Label(window,width=DisplayBarWidth,height=2,bg="yellow",textvariable=DisplayedArmor["艾伦"]),
              "莱纳":tk.Label(window,width=DisplayBarWidth,height=2,bg="green",textvariable=DisplayedArmor["莱纳"]),
              "阿妮":tk.Label(window,width=DisplayBarWidth,height=2,bg="blue",textvariable=DisplayedArmor["阿妮"]),
              "贝尔托特":tk.Label(window,width=DisplayBarWidth,height=2,bg="red",textvariable=DisplayedArmor["贝尔托特"]),
              "尤弥尔":tk.Label(window,width=DisplayBarWidth,height=2,bg="grey",textvariable=DisplayedArmor["尤弥尔"]),
              }

SkillDisplayBar = {"艾伦":tk.Label(window,width=DisplayBarWidth,height=2,bg="yellow",textvariable=DisplayedSkill["艾伦"]),
              "莱纳":tk.Label(window,width=DisplayBarWidth,height=2,bg="green",textvariable=DisplayedSkill["莱纳"]),
              "阿妮":tk.Label(window,width=DisplayBarWidth,height=2,bg="blue",textvariable=DisplayedSkill["阿妮"]),
              "贝尔托特":tk.Label(window,width=DisplayBarWidth,height=2,bg="red",textvariable=DisplayedSkill["贝尔托特"]),
              "尤弥尔":tk.Label(window,width=DisplayBarWidth,height=2,bg="grey",textvariable=DisplayedSkill["尤弥尔"]),
              }

DamageDisplayBar = {"艾伦":tk.Label(window,width=DisplayBarWidth,height=2,bg="yellow",textvariable=DisplayedDamage["艾伦"]),
              "莱纳":tk.Label(window,width=DisplayBarWidth,height=2,bg="green",textvariable=DisplayedDamage["莱纳"]),
              "阿妮":tk.Label(window,width=DisplayBarWidth,height=2,bg="blue",textvariable=DisplayedDamage["阿妮"]),
              "贝尔托特":tk.Label(window,width=DisplayBarWidth,height=2,bg="red",textvariable=DisplayedDamage["贝尔托特"]),
              "尤弥尔":tk.Label(window,width=DisplayBarWidth,height=2,bg="grey",textvariable=DisplayedDamage["尤弥尔"]),
              }

SufferDisplayBar = {"艾伦":tk.Label(window,width=DisplayBarWidth,height=2,bg="yellow",textvariable=DisplayedSuffer["艾伦"]),
              "莱纳":tk.Label(window,width=DisplayBarWidth,height=2,bg="green",textvariable=DisplayedSuffer["莱纳"]),
              "阿妮":tk.Label(window,width=DisplayBarWidth,height=2,bg="blue",textvariable=DisplayedSuffer["阿妮"]),
              "贝尔托特":tk.Label(window,width=DisplayBarWidth,height=2,bg="red",textvariable=DisplayedSuffer["贝尔托特"]),
              "尤弥尔":tk.Label(window,width=DisplayBarWidth,height=2,bg="grey",textvariable=DisplayedSuffer["尤弥尔"]),
              }

HealDisplayBar = {"艾伦":tk.Label(window,width=DisplayBarWidth,height=2,bg="yellow",textvariable=DisplayedHeal["艾伦"]),
              "莱纳":tk.Label(window,width=DisplayBarWidth,height=2,bg="green",textvariable=DisplayedHeal["莱纳"]),
              "阿妮":tk.Label(window,width=DisplayBarWidth,height=2,bg="blue",textvariable=DisplayedHeal["阿妮"]),
              "贝尔托特":tk.Label(window,width=DisplayBarWidth,height=2,bg="red",textvariable=DisplayedHeal["贝尔托特"]),
              "尤弥尔":tk.Label(window,width=DisplayBarWidth,height=2,bg="grey",textvariable=DisplayedHeal["尤弥尔"]),
              }

Titans = [Eren,Reiner,Annie,Bertolt,Ymir]

HealthBar["艾伦"].place(x=0,y=1000*1/(len(Titans)+1)-100,anchor="w")
HealthBar["莱纳"].place(x=0,y=1000*2/(len(Titans)+1)-100,anchor="w")
HealthBar["阿妮"].place(x=0,y=1000*3/(len(Titans)+1)-100,anchor="w")
HealthBar["贝尔托特"].place(x=0,y=1000*4/(len(Titans)+1)-100,anchor="w")
HealthBar["尤弥尔"].place(x=0,y=1000*5/(len(Titans)+1)-100,anchor="w")

NameDisplayBar["艾伦"].place(x=0,y=1000*1/(len(Titans)+1)+30-100,anchor="w")
NameDisplayBar["莱纳"].place(x=0,y=1000*2/(len(Titans)+1)+30-100,anchor="w")
NameDisplayBar["阿妮"].place(x=0,y=1000*3/(len(Titans)+1)+30-100,anchor="w")
NameDisplayBar["贝尔托特"].place(x=0,y=1000*4/(len(Titans)+1)+30-100,anchor="w")
NameDisplayBar["尤弥尔"].place(x=0,y=1000*5/(len(Titans)+1)+30-100,anchor="w")

HealthDisplayBar["艾伦"].place(x=114,y=1000*1/(len(Titans)+1)+30-100,anchor="w")
HealthDisplayBar["莱纳"].place(x=114,y=1000*2/(len(Titans)+1)+30-100,anchor="w")
HealthDisplayBar["阿妮"].place(x=114,y=1000*3/(len(Titans)+1)+30-100,anchor="w")
HealthDisplayBar["贝尔托特"].place(x=114,y=1000*4/(len(Titans)+1)+30-100,anchor="w")
HealthDisplayBar["尤弥尔"].place(x=114,y=1000*5/(len(Titans)+1)+30-100,anchor="w")

AttackDisplayBar["艾伦"].place(x=228,y=1000*1/(len(Titans)+1)+30-100,anchor="w")
AttackDisplayBar["莱纳"].place(x=228,y=1000*2/(len(Titans)+1)+30-100,anchor="w")
AttackDisplayBar["阿妮"].place(x=228,y=1000*3/(len(Titans)+1)+30-100,anchor="w")
AttackDisplayBar["贝尔托特"].place(x=228,y=1000*4/(len(Titans)+1)+30-100,anchor="w")
AttackDisplayBar["尤弥尔"].place(x=228,y=1000*5/(len(Titans)+1)+30-100,anchor="w")

ArmorDisplayBar["艾伦"].place(x=342,y=1000*1/(len(Titans)+1)+30-100,anchor="w")
ArmorDisplayBar["莱纳"].place(x=342,y=1000*2/(len(Titans)+1)+30-100,anchor="w")
ArmorDisplayBar["阿妮"].place(x=342,y=1000*3/(len(Titans)+1)+30-100,anchor="w")
ArmorDisplayBar["贝尔托特"].place(x=342,y=1000*4/(len(Titans)+1)+30-100,anchor="w")
ArmorDisplayBar["尤弥尔"].place(x=342,y=1000*5/(len(Titans)+1)+30-100,anchor="w")

SkillDisplayBar["艾伦"].place(x=456,y=1000*1/(len(Titans)+1)+30-100,anchor="w")
SkillDisplayBar["莱纳"].place(x=456,y=1000*2/(len(Titans)+1)+30-100,anchor="w")
SkillDisplayBar["阿妮"].place(x=456,y=1000*3/(len(Titans)+1)+30-100,anchor="w")
SkillDisplayBar["贝尔托特"].place(x=456,y=1000*4/(len(Titans)+1)+30-100,anchor="w")
SkillDisplayBar["尤弥尔"].place(x=456,y=1000*5/(len(Titans)+1)+30-100,anchor="w")

DamageDisplayBar["艾伦"].place(x=570,y=1000*1/(len(Titans)+1)+30-100,anchor="w")
DamageDisplayBar["莱纳"].place(x=570,y=1000*2/(len(Titans)+1)+30-100,anchor="w")
DamageDisplayBar["阿妮"].place(x=570,y=1000*3/(len(Titans)+1)+30-100,anchor="w")
DamageDisplayBar["贝尔托特"].place(x=570,y=1000*4/(len(Titans)+1)+30-100,anchor="w")
DamageDisplayBar["尤弥尔"].place(x=570,y=1000*5/(len(Titans)+1)+30-100,anchor="w")

SufferDisplayBar["艾伦"].place(x=684,y=1000*1/(len(Titans)+1)+30-100,anchor="w")
SufferDisplayBar["莱纳"].place(x=684,y=1000*2/(len(Titans)+1)+30-100,anchor="w")
SufferDisplayBar["阿妮"].place(x=684,y=1000*3/(len(Titans)+1)+30-100,anchor="w")
SufferDisplayBar["贝尔托特"].place(x=684,y=1000*4/(len(Titans)+1)+30-100,anchor="w")
SufferDisplayBar["尤弥尔"].place(x=684,y=1000*5/(len(Titans)+1)+30-100,anchor="w")

HealDisplayBar["艾伦"].place(x=798,y=1000*1/(len(Titans)+1)+30-100,anchor="w")
HealDisplayBar["莱纳"].place(x=798,y=1000*2/(len(Titans)+1)+30-100,anchor="w")
HealDisplayBar["阿妮"].place(x=798,y=1000*3/(len(Titans)+1)+30-100,anchor="w")
HealDisplayBar["贝尔托特"].place(x=798,y=1000*4/(len(Titans)+1)+30-100,anchor="w")
HealDisplayBar["尤弥尔"].place(x=798,y=1000*5/(len(Titans)+1)+30-100,anchor="w")

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
            
            time.sleep(0.05)
            text.insert("end", "\n")
                
        if len(Titans) == 1:
            text.insert("end",f"战斗结束！{Titans[0].name}获胜!\n")
            break
        
        round += 1

        window.update()

Start = tk.Button(window,text="START",command=Start)
Start.place(x=1000,y=600,anchor="center")
    
window.mainloop()
    