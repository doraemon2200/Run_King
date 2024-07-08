import pygame
import random
import time
pygame.font.init()


width, height = 1200, 800
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Unknown")
bg = pygame.transform.scale(pygame.image.load("bg.jpeg"), (width, height))
font = pygame.font.SysFont("comicsans", 30)
player_width = 100
player_height = 140
stone_width = 40
stone_height = 70
stone_vel = 5
player_x = 30
player_y = 445
player_vel = 10
jump = False
jump_count = 10


def draw(player, stones, elapsed_time, rect):
    win.blit(bg, (0, 0))

    time_text = font.render(f"{round(elapsed_time)}s", 1, "black")
    win.blit(time_text, (10,10))

    for stone in stones:
        pygame.draw.rect(win, "brown", stone)



    win.blit(player, (rect.x, rect.y))

    pygame.display.update()




def main():
    global player_y, player_x, jump, jump_count
    run = True

    player = pygame.transform.scale(pygame.image.load("character.png"), (player_width, player_height))
    p_rect = player.get_rect(topleft = (player_x, player_y))
    print(p_rect.size)
    chr_copy = player.copy()
    player_left = pygame.transform.flip(chr_copy, True, False)
    start_time = time.time()
    elapsed_time = 0
    stone_asc_time = 2000
    stone_speed = 0
    stones = []
    hit = False
    clock = pygame.time.Clock()


    while run:
        pygame.time.delay(20)

        stone_speed += clock.tick(200)

        elapsed_time = time.time() - start_time
        
        if stone_speed >= stone_asc_time:
            for i in range(1):
                stone_x = 1200
                stone = pygame.Rect(stone_x, 505, stone_width, stone_height)
                stones.append(stone)

            stone_asc_time = max(2000, stone_asc_time - 50)
            stone_speed = 0


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break


        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            p_rect.x -= player_vel
        if keys[pygame.K_RIGHT]:
            p_rect.x += player_vel
        if not jump:
            #will not jump as he had already jumped under space so jump = True
            if keys[pygame.K_SPACE] or keys[pygame.K_UP]:
                jump = True
        else:
            if jump_count >= -10:
                p_rect.y -= (jump_count * abs(jump_count)) * 0.5
                p_rect.x += 6
                jump_count -= 1
            else:
                jump_count = 10
                p_rect.y = 445
                jump = False

        for stone in stones[:]:
            stone.x -= stone_vel
            if stone.x < 0:
                stones.remove(stone)
            if stone.colliderect(p_rect, ):
                stones.remove(stone)
                hit = True
                break

        if hit:
            lost_text = font.render(f"You Lost \n Your time is {round(elapsed_time)}s", 1, "black")
            win.blit(lost_text, (width/2-lost_text.get_width()/2, 200))
            pygame.display.update()
            pygame.time.delay(4000)
            break


        draw(player, stones, elapsed_time, p_rect)

    pygame.quit()


if __name__ == "__main__":
    main()
