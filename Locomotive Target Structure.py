from graphics import*
from random import randint
    
def Project():
    #Final Project
    
    wn=GraphWin("Ryan Lam Final Project", 800, 500)
    wn.setBackground("lightgreen")
    
    instr=Image(Point(400,250),"instructions.png")
    instr.draw(wn)

    entername=Text(Point(400,50),"Enter name in IDLE \n then "
                   "read instructions below")
    entername.draw(wn)
    
    name=input("Enter your name: ")
    
    wn.getMouse()
    entername.undraw()
    instr.undraw()
    time.sleep(1)

    randX=randint(0,1)
    
    if randX == 0:
        OvaX=0
        OvaXX=75
        
    if randX == 1:
        OvaX=725
        OvaXX=800
    Ova=Oval(Point(OvaX,30),Point(OvaXX,50))
    Ova.setFill("black")
    Ova.draw(wn)

    score=0
    Click = 0
    ryan = True
    ryan2 = False
    
    for i in range(10):
        
        if OvaX == 725:
            
            if ryan:
                    
                randY=randint(2,3)
                
                if randY == 2:
                    CirX=325
                    Cir=Circle(Point(CirX,510),10)
                    Cir.setFill("red")
                    Cir.draw(wn)

                if randY == 3:
                    CirX=475
                    Cir=Circle(Point(CirX,510),10)
                    Cir.setFill("red")
                    Cir.draw(wn)
                    
                ryan = False
            if ryan2:
                randX=randint(0,1)
    
                if randX == 0:
                    OvaX=0
                    OvaXX=75
                    Ova=Oval(Point(OvaX,30),Point(OvaXX,50))
                    Ova.setFill("black")
                    Ova.draw(wn)
                if randX == 1:
                    OvaX=725
                    OvaXX=800
                    Ova=Oval(Point(OvaX,30),Point(OvaXX,50))
                    Ova.setFill("black")
                    Ova.draw(wn)
                ryan2 = False  
            for a in range(145):                
                Ova.move(-5,0)
                time.sleep(0.015)
                OvaL=Ova.getP1().getX()
                OvaR=Ova.getP2().getX()
                CirY=Cir.getCenter().getY()
                
                if wn.checkMouse() != None:
                    Click = 1
                if Click == 1:
                    Cir.move(0,-6.5)
                if CirY < 6.5:
                    Cir.undraw()
                    Cir=Circle(Point(CirX,510),10)
                    Cir.setFill("red")
                    Cir.draw(wn)
                    score-=1
                    if score < 0:
                        score = 0
                    Click = 0
                elif CirX > OvaL and CirX < OvaR and CirY <50:
                    Ova.undraw()
                    Cir.undraw()
                    Cir=Circle(Point(CirX,510),10)
                    Cir.setFill("red")
                    Cir.draw(wn)
                    score+=3
                    if score >= 63:
                        score=63
                        break
                    ryan2 = True
                    Click = 0
                                  
            for b in range(145):
                Ova.move(5,0)
                time.sleep(0.015)
                OvaL=Ova.getP1().getX()
                OvaR=Ova.getP2().getX()
                CirY=Cir.getCenter().getY()
                
                if wn.checkMouse() != None:
                    Click = 1
                if Click == 1:
                    Cir.move(0,-6.5)
                if CirY < 6.5:
                    Cir.undraw()
                    Cir=Circle(Point(CirX,510),10)
                    Cir.setFill("red")
                    Cir.draw(wn)
                    score-=1
                    if score < 0:
                        score = 0
                    Click = 0
                elif CirX > OvaL and CirX < OvaR and CirY <50:
                    Ova.undraw()
                    Cir.undraw()
                    Cir=Circle(Point(CirX,510),10)
                    Cir.setFill("red")
                    Cir.draw(wn)
                    score+=3
                    if score >= 63:
                        score=63
                        break
                    ryan2 = True
                    Click = 0
                
        if OvaX == 0:
            
            if ryan:
            
                randY=randint(2,3)
                
                if randY == 2:
                    CirX=325
                    Cir=Circle(Point(CirX,510),10)
                    Cir.setFill("red")
                    Cir.draw(wn)

                if randY == 3:
                    CirX=475
                    Cir=Circle(Point(CirX,510),10)
                    Cir.setFill("red")
                    Cir.draw(wn)
                ryan = False
            if ryan2:
                randX=randint(0,1)
    
                if randX == 0:
                    OvaX=0
                    OvaXX=75
                    Ova=Oval(Point(OvaX,30),Point(OvaXX,50))
                    Ova.setFill("black")
                    Ova.draw(wn)
                if randX == 1:
                    OvaX=725
                    OvaXX=800
                    Ova=Oval(Point(OvaX,30),Point(OvaXX,50))
                    Ova.setFill("black")
                    Ova.draw(wn)
                ryan2 = False
            for c in range(145):
                Ova.move(5,0)
                time.sleep(0.015)
                OvaL=Ova.getP1().getX()
                OvaR=Ova.getP2().getX()
                CirY=Cir.getCenter().getY()
                
                if wn.checkMouse() != None:
                    Click = 1
                if Click == 1:
                    Cir.move(0,-6.5)
                if CirY < 6.5:
                    Cir.undraw()
                    Cir=Circle(Point(CirX,510),10)
                    Cir.setFill("red")
                    Cir.draw(wn)
                    score-=1
                    if score < 0:
                        score = 0
                    Click = 0
                elif CirX > OvaL and CirX < OvaR and CirY <50:
                    Ova.undraw()
                    Cir.undraw()
                    Cir=Circle(Point(CirX,510),10)
                    Cir.setFill("red")
                    Cir.draw(wn)
                    score+=3
                    if score >= 63:
                        score=63
                        break
                    ryan2 = True
                    Click = 0
                   
                        
            for d in range(145):
                Ova.move(-5,0)
                time.sleep(0.015)
                OvaL=Ova.getP1().getX()
                OvaR=Ova.getP2().getX()
                CirY=Cir.getCenter().getY()
                
                if wn.checkMouse() != None:
                    Click = 1
                if Click == 1:
                    Cir.move(0,-6.5)
                if CirY < 6.5:
                    Cir.undraw()
                    Cir=Circle(Point(CirX,510),10)
                    Cir.setFill("red")
                    Cir.draw(wn)
                    score-=1
                    if score < 0:
                        score = 0
                    Click = 0
                elif CirX > OvaL and CirX < OvaR and CirY <50:
                    Ova.undraw()
                    Cir.undraw()
                    Cir=Circle(Point(CirX,510),10)
                    Cir.setFill("red")
                    Cir.draw(wn)
                    score+=3
                    if score >= 63:
                        score=63
                        break
                    ryan2 = True                  
                    Click = 0
                    
    print("Your final score is ", score)
    din=open("scores.txt","a")
    din.write(name+"\t"+"\t"+str(score)+ "\n")
    din.close()

 
    
Project()
