from time import sleep
class PattrnSim:
  def __init__(s, ss, p):
    s.s = ss
    s.p = p
    s.cp = [0, 0]
  def mv(s):
    i = 0
    p = s.p.copy()
    p = [s.cp[0], s.cp[1]] + s.p
    while i <= (len(p)) / 2:
      a = p[i]
      b = p[i+1]
      c = p[i+2]
      d = p[i+3]
      j = 0
      print(f"Sim: moving from ({a}, {b}) to ({c}, {d})")
      while j < 100:
        e = (c - a) / 100
        f = (d - b) / 100

        s.cp[0] += e
        s.cp[1] += f

        s.s.move_to(s.cp[0], s.cp[1])
        sleep(0.01)

        j += 1

      print(f"Sim: on position ({s.cp[0]}, {s.cp[1]})")















      i += 2
class PtternSep:
  def __init__(s, ss, p):
    s.s = ss
    s.p = p
    s.cp = [0, 0]

  def mv(s):
    i = 0
    p = s.p.copy()
    p = [s.cp[0], s.cp[1]] + s.p
    while i <= (len(p)) / 2:
      a = p[i]
      b = p[i+1]
      c = p[i+2]
      d = p[i+3]

      j = 0

      print(f"Sep: moving from ({a}, {b}) to ({c}, {d})")
      while j < 50:
        e = (c - a) / 50

        s.cp[0] += e

        s.s.move_to(s.cp[0], s.cp[1])
        sleep(0.01)

        j += 1

      j = 0
      while j < 50:
        f = (d - b) / 50

        s.cp[1] += f

        s.s.move_to(s.cp[0], s.cp[1])
        sleep(0.01)

        j += 1
      print(f"Sep: on position ({s.cp[0]}, {s.cp[1]})")
      i += 2
