#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import sys
import os
import random

from optparse import OptionParser

Parser = OptionParser()
Parser.add_option("-l", "--lenght", dest="Lenght", help="Password lenght (default 8)", default=True)
Parser.add_option("-a", "--alphanumeric", dest="Alphanumeric", help="Generate alphanumeric only password", action="store_true")
Parser.add_option("-s", "--specialchars", dest="SpecialChars", help="Generate an alphanumeric w/ special chars password", action="store_true")
Parser.add_option("-n", "--number", dest="Number", help="Specify how many password you want to generate")

(Options,Args) = Parser.parse_args()
Lenght = Options.Lenght
Alphanumeric = Options.Alphanumeric
SpecialChars = Options.SpecialChars
Number = Options.Number

MinPasswdLenght = 8

def GenPassword(lenght=MinPasswdLenght,alphanum=True,specialchars=False, Num=1):

    AlphaNum = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    All = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890&#{}()|-_^@=$%<>!:;.,?"

    if Lenght is True:
        lenght = MinPasswdLenght
    if alphanum is True:
        choice = AlphaNum
    if specialchars is True:
        choice = All
    else:
        choice = AlphaNum

    print "\nMots de passes générés :\n"
    for x in range(0,int(Num)):
        GeneratedPW = ''.join(random.sample(choice, int(lenght)))
        print '',GeneratedPW

def CheckLenght(Lenght):
	if int(Lenght) < MinPasswdLenght and Lenght is not True:
		print '\n ! Longeur minimum du mot de passe\ peu être moins que  %d' % MinPasswdLenght
		Lenght = MinPasswdLenght
	else:
		Lenght = Lenght

	return Lenght

if len(sys.argv) < 2:
    print "\n=> Pas d'options peu être... Je vais générer des %d des caratères Alphanumeriques\n   Type %s -h pour plus d'informations" % (MinPasswdLenght,sys.argv[0])
    DefinedLenght = MinPasswdLenght
    DefinedNum = 1
    DefinedAlphanumeric = True
    DefinedSpecialChars = False
    GenPassword(DefinedLenght,DefinedAlphanumeric,DefinedSpecialChars,DefinedNum)
elif Options.Lenght is not None:
    if Number is None:
        Number = 1
    DefinedLenght = CheckLenght(Lenght)
    DefinedNum = Number
    DefinedAlphanumeric = Alphanumeric
    DefinedSpecialChars = SpecialChars
    GenPassword(DefinedLenght,DefinedAlphanumeric,DefinedSpecialChars,DefinedNum)
