import pygame

pygame.init()
screen = pygame.display.set_mode((800,600))

mario = pygame.image.load('mario.gif')
mario_back = pygame.image.load('mario_back.png')

pygame.mixer.music.load('stage1.mp3')
pygame.mixer.music.play(0)

mario.set_colorkey((255,255,255))

done = False
r1 = pygame.Rect(11,4,14,17)   #สี่เหลี่่ยมของภาพมาริโอ ตอนหยุด
r2 = pygame.Rect(162,2,18,18)   #สี่เหลี่่ยมของภาพมาริโอ ตอนเดิน 1
r3 = pygame.Rect(182,2,18,18)   #สี่เหลี่่ยมของภาพมาริโอ ตอนเดิน 2
clock = pygame.time.Clock()   #ตัวกำหนด frame rate
mario_x = 65
mario_y = 533
mario_walk = False
mario_walk_step = 0

while not done:   #game loop  (ให้ใช้เวลาน้อยสุด)
    for event in pygame.event.get(): #เช็คอินพุท
        if event.type == pygame.QUIT:  #ออกโปรแกรม
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                mario_x -= 10
                mario_walk = True
            if event.key == pygame.K_RIGHT:
                mario_x += 10
                mario_walk = True
        else:
            if mario_walk_step == 0:
                mario_walk = False
            
    #screen.fill((255,255,255))   #เติมสีขาว
    screen.blit(mario_back,(0,0))
    if mario_walk == True:
        if mario_walk_step == 0:
            screen.blit(mario,(mario_x,mario_y),r2)
        elif mario_walk_step == 1:
            screen.blit(mario,(mario_x,mario_y),r3)
        mario_walk_step += 1
        if mario_walk_step == 1:
            mario_walk_step = 0
    else:        
        screen.blit(mario,(mario_x,mario_y),r1) #วาดรูปจาก mario surface ไปที่ตำแหน่ง 50,100 โดยใช้ภาพมาริโอจาก r1
        
    pygame.display.flip()    #วาดลงการ์ดจอ (ก่อนหน้านี้ วาดใน RAM) 
    clock.tick(30);          #ปรับเวลาให้ตรง 30 fps





    
