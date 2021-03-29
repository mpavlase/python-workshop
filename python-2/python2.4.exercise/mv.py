from ptns import PattrnSim, PtternSep

def mv(s, a, b):
    if a == "simultaneous":
        c = PattrnSim(s, b)
        c.mv()
    elif a == "separately":
        c = PtternSep(s, b)
        c.mv()
