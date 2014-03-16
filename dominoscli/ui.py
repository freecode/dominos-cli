import curses
import curses.textpad

class UI: 
    def __init__(self):
        self.stdscr = curses.initscr()
        curses.start_color()
        curses.noecho()
        self.stdscr.keypad(1)
        curses.cbreak()

    def close(self):
        curses.echo()
        self.stdscr.keypad(0)
        curses.nocbreak()
        curses.endwin()

    def display_menu(self, menu):
        self.stdscr.addstr("Pizzas:")
        i = 0
        for pizza in menu.pizzas:
              self.stdscr.addstr("\t")
              self.stdscr.addstr(pizza.name.encode("utf-8"))
              self.maketextbox(1,10, self.stdscr.getyx()[0], self.stdscr.getyx()[1], "0",deco="underline", underlineChr=curses.ACS_HLINE,textColorpair=curses.color_pair(0),decoColorpair=curses.color_pair(1))
              self.stdscr.addstr("\n")
              
        self.stdscr.getch() 
    
    # found this on stackoverflow
    def maketextbox(self, h,w,y,x,value="",deco=None,underlineChr = 0,textColorpair=0,decoColorpair=0):
        nw = curses.newwin(h,w,y,x)
        txtbox = curses.textpad.Textbox(nw)
        if deco=="frame":
            self.stdscr.attron(decoColorpair)
            curses.textpad.rectangle(screen,y-1,x-1,y+h,x+w)
            self.stdscr.attroff(decoColorpair)
        elif deco=="underline":
            self.stdscr.hline(y+1,x,underlineChr,w,decoColorpair)
    
        nw.addstr(0,0,value,textColorpair)
        nw.attron(textColorpair)
        self.stdscr.refresh()
        return txtbox   
