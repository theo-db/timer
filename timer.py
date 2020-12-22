import time, pygame

class Time:
    def __init__(self):
        self.start = time.time()
    def get_time(self):
        return round(time.time() - self.start,2)

def main():
    size = (600,400)
    pygame.init()
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("timer")
    font = pygame.font.SysFont("monospace", 100)
    timing = False
    finished = False
    display = ""
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if timing:
                    timing = False
                    finished = True
                    TIME = timer.get_time()
                    print(TIME)
                    display = str(TIME)
            if event.type == pygame.KEYUP:
                if not timing and not finished:
                    timing = True
                    timer = Time()
                elif finished:
                    finished = False
        if timing:
            display = str(timer.get_time())
        screen.fill((0,0,0))
        t = font.render(display, False, (255,255,255))
        screen.blit(t, (100, 150))
        pygame.display.flip()
        pygame.time.wait(1)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        raise e
    finally:
        pygame.quit()
                    
