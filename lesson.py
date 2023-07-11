import curses
import logging
import json
import copy


def show_lesson_screen(stdscr:curses.window):
    f = open('lesson.json')
    lessons=json.load(f)
    SELECTED_LESSON=1
    max_lesson=len(lessons)
    curses.init_pair(5,curses.COLOR_RED,curses.COLOR_WHITE)
   
    while True:
        stdscr.clear()
        stdscr.addstr(0,0,'Select a Lesson to Continue.')
        logging.debug('selected ,'+str(SELECTED_LESSON))
        for i in range(30):
            if SELECTED_LESSON%30==0:
                pointer=((SELECTED_LESSON//30)-1)*(30)+i
            else:
                pointer=SELECTED_LESSON-(SELECTED_LESSON%30)+i
            if pointer<max_lesson:
                if SELECTED_LESSON==pointer+1:
                    stdscr.addstr((i//10)+1,(i%10)*4,str(pointer+1),curses.color_pair(5))
                else:
                    stdscr.addstr((i//10)+1,(i%10)*4,str(pointer+1))
        stdscr.addstr(40//10+2,0,lessons[SELECTED_LESSON-1]['title'])
        stdscr.refresh()
        key=stdscr.getch()
        if key==curses.KEY_UP:
            if SELECTED_LESSON-1 < 10:
                SELECTED_LESSON = min(10*(max_lesson//10)+SELECTED_LESSON,max_lesson)
            else:
                SELECTED_LESSON-=10
        elif key==curses.KEY_DOWN:
            SELECTED_LESSON+=10
            if SELECTED_LESSON>max_lesson:
                if min(SELECTED_LESSON,max_lesson)==max_lesson and SELECTED_LESSON-10!=max_lesson:
                    SELECTED_LESSON=min(SELECTED_LESSON,max_lesson)
                else:
                    SELECTED_LESSON=SELECTED_LESSON%10
                    if SELECTED_LESSON==0:
                        SELECTED_LESSON+=10
        elif key==curses.KEY_LEFT:
            SELECTED_LESSON-=1
            if SELECTED_LESSON==0:
                SELECTED_LESSON=max_lesson
        elif key==curses.KEY_RIGHT:
            SELECTED_LESSON+=1
            if SELECTED_LESSON>max_lesson:
                SELECTED_LESSON=1
        elif key==curses.KEY_ENTER or key in [10,13]:
            return SELECTED_LESSON-1

    
