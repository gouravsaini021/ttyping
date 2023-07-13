import curses
import time
import logging
import json
from os import environ


f = open('config.json')
data = json.load(f)
Audio=data["audio"]
if Audio:
	environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'  #This variable is set to remove pygame hello message
	from pygame import mixer
	mixer.init()
	typewriter_sound=mixer.Sound("audio/typewriter.mp3")
	error_sound=mixer.Sound("audio/error.mp3")


def show_result_screen(stdscr,total_time,total_typed_char,correct_typed_char,goal_wpm,selected_option):
	""" This function show final result on screen. """
	logging.debug(selected_option)
	stdscr.clear()
	h,w=stdscr.getmaxyx()
	total_time=round(total_time/60,2)
	gwpm=(total_typed_char/5)//total_time
	accuracy=int((correct_typed_char/total_typed_char)*100)
	curses.init_pair(4,curses.COLOR_WHITE,curses.COLOR_BLUE)
	stdscr.addstr(h//2,w//2,f'Goal WPM: {goal_wpm}')
	stdscr.addstr(h//2+1,w//2,f'WPM : {(gwpm*accuracy)//100}')
	stdscr.addstr(h//2+2,w//2,f'Accuracy : {accuracy}%')
	stdscr.addstr(h//2+3,w//2,f'Minute : {total_time}')

	if selected_option=='Home':
		stdscr.addstr(h//2+4,w//2,'Home',curses.color_pair(4))
	else:
		stdscr.addstr(h//2+4,w//2,'Home')

	if selected_option=='Next':
		stdscr.addstr(h//2+4,w//2+5,'Next',curses.color_pair(4))
	else:
		stdscr.addstr(h//2+4,w//2+5,'Next')
	
	if selected_option=='Repeat':
		stdscr.addstr(h//2+4,w//2+10,'Repeat',curses.color_pair(4))	
	else:
		stdscr.addstr(h//2+4,w//2+10,'Repeat')
	stdscr.refresh()	

	return



# GREEN=curses.init_pair(2,curses.COLOR_BLACK,curses.COLOR_GREEN)
def re_adjust_screen(stdscr,ch1,color_seq):
	"""When user change size of screen adjust according to that."""
	h,w=stdscr.getmaxyx()
	stdscr.clear()
	cur_w = 0
	cur_h = 0
	# for count, color_pair in enumerate(color_seq):
	# 	stdscr.addstr(cur_h,cur_w,ch1[count],curses.color_pair(color_pair))
	# 	cur_w+=1
	# 	if cur_w  == w:
	# 		cur_h +=1
	# 		cur_w =0
	m_index=len(color_seq)
	for i in range(3):
		stdscr.addstr(i,0,ch1[m_index:m_index+w])
		m_index+=w
	stdscr.refresh()

def show_next_line(stdscr,ch1,color_seq,index):
	h,w=stdscr.getmaxyx()
	stdscr.clear()
	if index>=w*1:
		start=index-w*1
	else:
		start=0
	cur_h=0
	cur_w=0
	for count in range(start,len(color_seq)):
		stdscr.addstr(cur_h,cur_w,ch1[count],curses.color_pair(color_seq[count]))
		cur_w+=1
		if cur_w  == w:
			cur_h +=1
			cur_w =0

	stdscr.addstr(cur_h,cur_w,ch1[len(color_seq):min(len(color_seq)+2*w,len(ch1))])
	
	stdscr.refresh()


def get_xxxxx(stdscr:curses.window,lesson_no:int):
	f = open('lesson.json')
	lessons=json.load(f)
	stdscr.clear()
	# ch1="think how do you think in this situation that really matters in life to create happy healthy and prosprous life."
	# ch1="The world is becoming increasingly digitized, and as a result, digital literacy has become a crucial skill to have. Whether it's understanding how to use new software or navigating social media, being digitally literate can help you in both your personal and professional life. So, take the time to learn and stay up-to-date with the latest digital trends to stay ahead of the curve."
	try:
		ch1=lessons[lesson_no]['lesson']
	except IndexError:
		return 
	goal_wpm=lessons[lesson_no]['goal_wpm']
	color_seq=[]
	h,w=stdscr.getmaxyx()
	#show only 3 lines of whole paragraph adjusted to screen
	for i in range(3):
		stdscr.addstr(i,0,ch1[i*w:w*(i+1)])
	stdscr.refresh()
	# current height and width
	cur_h=0
	cur_w=0
	i=0
	total_typed_char = 0
	correct_typed_char = 0

	curses.init_pair(2,curses.COLOR_BLACK,curses.COLOR_GREEN)
	curses.init_pair(3,curses.COLOR_BLACK,curses.COLOR_RED)
	while i<len(ch1):
		key=stdscr.getch()
		h,w=stdscr.getmaxyx()
		logging.debug(str(key))
		# stdscr.addstr(10,10,str(key))
		# stdscr.addstr(12,10,str(cur_w)+", "+str(w))
		# stdscr.addstr(15,10,str(cur_h))
		total_typed_char+=1
		if i==0:
			start_time=time.time()
		
		if key == curses.KEY_RESIZE:
			# when screen resize then re - render screen again.
			re_adjust_screen(stdscr=stdscr,ch1=ch1,color_seq=color_seq)
			total_typed_char-=1
			cur_w,cur_h=0,0
			continue
			 
		if w==cur_w:
			# if width out of screen re-adjust.
			cur_w=0
			cur_h+=1
			if cur_h>=2:
				# raise Exception("Sorry, no numbers below zero")
				show_next_line(stdscr,ch1,color_seq,i)
				cur_h=1
		logging.debug("char key: "+str(ord(ch1[i])))
		logging.debug("keyboard key:"+str(key))
		if chr(key)==ch1[i]:
			# This condition is for when user press right key 
			correct_typed_char+=1
			color_seq.append(2)
			stdscr.addstr(cur_h,cur_w,chr(key),curses.color_pair(2))
			if Audio:
				try:
					# sound_thread = threading.Thread(target=lambda:playsound("audio/typewriter.mp3"))
					# sound_thread.start()
					typewriter_sound.play()
				except:
					pass
			stdscr.refresh()
		
		# This condition is for when user press for backspace
		elif key==curses.KEY_BACKSPACE or key=='\x7f' or key==263:
			if cur_w==0:
				curses.beep()
				continue
			cur_w-=1
			i-=1
			color_seq.pop()
			stdscr.addstr(cur_h,cur_w,ch1[i])
			stdscr.refresh()
			continue
		else:
			# This condition is for when user press wrong key
			color_seq.append(3)
			stdscr.addstr(cur_h,cur_w,ch1[i],curses.color_pair(3))
			if Audio:
				try:
					# sound_thread = threading.Thread(target=lambda:playsound("audio/error.mp3"))
					# sound_thread.start()
					error_sound.play()
				except:
					pass
			stdscr.refresh()
		i+=1
		cur_w+=1
	end_time=time.time()
	total_time=end_time-start_time
	i=1
	options=['Home','Next','Repeat']
	while True:
		show_result_screen(stdscr,total_time,total_typed_char,correct_typed_char,goal_wpm,options[i])
		key=stdscr.getch()
		if key==curses.KEY_LEFT:
			i-=1
			if i<0 :
				i=len(options)-1
		if key==curses.KEY_RIGHT:
			i+=1
			if i>=len(options):
				i=0
		if key==curses.KEY_ENTER or key in [10,13]:
			if options[i]=='Home':
				break
			if options[i]=='Repeat':
				get_xxxxx(stdscr,lesson_no)
			if options[i]=='Next':
				get_xxxxx(stdscr,lesson_no+1)
			# this break help from returning all recursive function that all called in 'Repeat' and 'Next'
			break



		
