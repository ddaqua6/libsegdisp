from gpiozero import LED
disp_a = "null"
disp_b = "null"
disp_c = "null"
disp_d = "null"
disp_e = "null"
disp_f = "null"
disp_g = "null"
disp_dot = "null"
list = []
def configure(a="null", b="null", c="null", d="null", e="null", f="null", g="null", dot="null"):
        global disp_a
        global disp_b
        global disp_c
        global disp_d
        global disp_e
        global disp_f
        global disp_g
        global disp_dot
	global list
        if a != "null":
                disp_a = LED(int(a))
		list.append(disp_a)
        if b != "null":
                disp_b = LED(int(b))
		list.append(disp_b)
        if c != "null":
                disp_c = LED(int(c))
		list.append(disp_c)
        if d != "null":
                disp_d = LED(int(d))
		list.append(disp_d)
        if e != "null":
                disp_e = LED(int(e))
		list.append(disp_e)
        if f != "null":
                disp_f = LED(int(f))
		list.append(disp_f)
        if g != "null":
                disp_g = LED(int(g))
		list.append(disp_g)
        if dot != "null":
                disp_dot = LED(int(dot))
		list.append(disp_dot)
def miss(info):
	print("Error: " + info)
def play(char):
        for i in list:
		i.off()
	if char == 1:
                if disp_b != "null" and disp_c != "null":
                        disp_b.on()
                        disp_c.on()
                else:
                        miss("Fields B, C not configured.")
        elif char == 2:
                if disp_a != "null" and disp_b != "null" and disp_g != "null" and disp_e != "null" and disp_d != "null":
                        disp_a.on()
                        disp_b.on()
                        disp_g.on()
                        disp_e.on()
                        disp_d.on()
                else:
                        miss("Fields A, B, D, E, G not configured.")
        elif char == 3:
                if disp_a != "null" and disp_b != "null" and disp_g != "null" and disp_c != "null" and disp_d != "null":
                        disp_a.on()
                        disp_b.on()
                        disp_c.on()
                        disp_d.on()
                        disp_g.on()
                else:
                        miss("Fields A-D, G not configured.")
        elif char == 4:
                if disp_f != "null" and disp_g != "null" and disp_b != "null" and disp_c != "null":
                        disp_f.on()
                        disp_g.on()
                        disp_b.on()
                        disp_c.on()
                else:
                        miss("Fields B, C, F, G not configured.")
	elif char == 5:
                if disp_a != "null" and disp_f != "null" and disp_g != "null" and disp_c != "null" and disp_d != "null":
                        disp_a.on()
                        disp_f.on()
                        disp_g.on()
                        disp_c.on()
                        disp_d.on()
                else:
                        miss("Fields A, C, D, F, G not configured.")
        elif char == 6:
                if disp_a != "null" and disp_f != "null" and disp_g != "null" and disp_e != "null" and disp_d != "null" and disp_c != "null":
                        disp_a.on()
                        disp_f.on()
                        disp_g.on()
                        disp_e.on()
                        disp_d.on()
                        disp_c.on()
                else:
                        miss("Fields A, C-G not configured.")
        elif char == 7:
                if disp_a != "null" and disp_b != "null" and disp_c != "null":
                        disp_a.on()
                        disp_b.on()
                        disp_c.on()
                else:
                        miss("Fields A-C not configured.")
	elif char == 8:
                if disp_a != "null" and disp_b != "null" and disp_c != "null" and disp_d != "null" and disp_e != "null" and disp_f != "null" and disp_g != "null":
                        disp_a.on()
                        disp_b.on()
                        disp_c.on()
                        disp_d.on()
                        disp_e.on()
                        disp_f.on()
                        disp_g.on()
		else:
			miss("Fields A-G not configured.")
        elif char == 9:
                if disp_a != "null" and disp_b != "null" and disp_f != "null" and disp_g != "null" and disp_c != "null" and disp_d != "null":
                        disp_a.on()
                        disp_f.on()
                        disp_g.on()
                        disp_b.on()
                        disp_c.on()
                        disp_d.on()
                else:
                        miss("Fields A-D, F-G not configured.")
	elif char == 0:
		if disp_a != "null" and disp_b != "null" and disp_c != "null" and disp_d != "null" and disp_e != "null" and disp_f != "null":
			disp_a.on()
                        disp_b.on()
                        disp_c.on()
                        disp_d.on()
                        disp_e.on()
                        disp_f.on()
		else:
			miss("Fields A-F not configured.")
