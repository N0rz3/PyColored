import os, sys, time
from os import system, name, get_terminal_size
from sys import stdout as st
from pyfiglet import Figlet



__name__ = "pycolors v1"
__credits__ = "Norze and Platipus"
__doc__ = ""



"""
List Function
    System:
        System.Title("#title window")
        System.Clear()
        System.Init()
        System.Exit()


    Color:
        Color.Black + "text"


    Pattern:
        Pattern.Ansi_Shadow(banner #Ascii Police Ansi_Shadow, Color.Pink #first color, Color.White #second color)
        Pattern.Big_Money(banner #Ascii Police Big_Money, Color.Pink #first color, Color.White #second color)
        Pattern.Electronic(banner #Ascii Police Electronic, Color.Pink #first color, Color.White #second color)



    Input:
        Input.Void() #input("")

    Print:
        Print.Void() #print("")
        Print.Write(banner, 0.001 #delay)


    Ascii:
        Ascii.Text(texte="name", font="graffiti #name font")
"""








class System:
    Windows = name == 'nt'

    #window title
    def Title(title: str) -> None:
        os.system(f"title {title}")


    #cls/clear cmd equivalent
    def Clear() -> None:
        if System.Windows:
            os.system("cls")
        else:
            os.system("clear")


    def Init() -> None:
        os.system("")


    def Exit() -> None:
        sys.exit()




class Color:
    """Reset Colors"""
    Reset = '\033[38;2;255;255;255m'


    """Simple Colors"""
    White = "\033[38;2;255;255;255m"
    Black = "\033[38;2;0;0;0m"
    Red = "\033[38;2;255;0;0m"
    Green = "\033[38;2;0;255;0m"
    Blue = "\033[38;2;0;0;255m"
    Purple = "\033[38;2;147;112;219m"
    Cyan = "\033[38;2;0;255;255m"
    Yellow = "\033[38;2;255;255;0m"
    Orange = "\033[38;2;255;130;0m"
    Pink = "\033[38;2;255;138;239m"
    Brown = "\033[38;2;139;115;85m"


    """Light Colors"""
    Light_Orange = "\033[38;2;255;170;0m"
    Light_Green = "\033[38;2;193;255;193m"
    Light_Yellow = "\033[38;2;251;255;133m"
    Light_Pink = "\033[38;2;255;199;248m"
    Light_Red = "\033[38;2;255;48;48m"
    Light_Blue = "\033[38;2;100;149;237m"
    Light_Cyan = "\033[38;2;151;255;255m"
    Light_Purple = "\033[38;2;191;62;255m"


    """Dark Colors"""
    Dark_Orange = "\033[38;2;255;90;0m"
    Dark_Green = "\033[38;2;18;82;0m"
    Dark_Yellow = "\033[38;2;212;219;0m"
    Dark_Pink = "\033[38;2;194;0;168m"
    Dark_Red = "\033[38;2;139;26;26m"
    Dark_Purple = "\033[38;2;93;71;139m"
    Dark_Blue = "\033[38;2;0;0;205m"
    Dark_Brown = "\033[38;2;139;101;8m"



class Pattern:
    def Ansi_Shadow(text: str, main_color: str, second_color: str, col_reset: bool = True) -> str:
        """
    Banner Format:

    ████████╗███████╗██╗  ██╗████████╗
    ╚══██╔══╝██╔════╝╚██╗██╔╝╚══██╔══╝
       ██║   █████╗   ╚███╔╝    ██║   
       ██║   ██╔══╝   ██╔██╗    ██║   
       ██║   ███████╗██╔╝ ██╗   ██║   
       ╚═╝   ╚══════╝╚═╝  ╚═╝   ╚═╝"""

        result = ""
        for caract in text:
            if caract in ["╚", "═", "╝", "╔", "║", "╗"]:
                result += second_color + caract
            else:
                result += main_color + caract
        if col_reset:
            return result + '\033[38;2;255;255;255m'
        else:
            return result


    system("")


    def Big_Money(text: str, main_color: str, second_color: str, col_reset: bool = True) -> str:
        """
    Banner Format:
    
   __                            __     
  |  \                          |  \    
 _| $$_     ______   __    __  _| $$_   
|   $$ \   /      \ |  \  /  \|   $$ \  
 \$$$$$$  |  $$$$$$\ \$$\/  $$ \$$$$$$  
  | $$ __ | $$    $$  >$$  $$   | $$ __ 
  | $$|  \| $$$$$$$$ /  $$$$\   | $$|  \
   \$$  $$ \$$     \|  $$ \$$\   \$$  $$
    \$$$$   \$$$$$$$ \$$   \$$    \$$$$ 
                                        
                                        
                                        
                                      
    """

        result = ""
        for caract in text:
            if caract in ["\\", "__", "/", "|", "__", "_"]:
                result += second_color + caract
            else:
                result += main_color + caract
        if col_reset:
            return result + '\033[38;2;255;255;255m'
        else:
            return result
        

    def Electronic(text: str, main_color: str, second_color: str, col_reset: bool = True) -> str:
        """
    Banner Format:

 ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄       ▄  ▄▄▄▄▄▄▄▄▄▄▄ 
▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌     ▐░▌▐░░░░░░░░░░░▌
 ▀▀▀▀█░█▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀  ▐░▌   ▐░▌  ▀▀▀▀█░█▀▀▀▀ 
     ▐░▌     ▐░▌            ▐░▌ ▐░▌       ▐░▌     
     ▐░▌     ▐░█▄▄▄▄▄▄▄▄▄    ▐░▐░▌        ▐░▌     
     ▐░▌     ▐░░░░░░░░░░░▌    ▐░▌         ▐░▌     
     ▐░▌     ▐░█▀▀▀▀▀▀▀▀▀    ▐░▌░▌        ▐░▌     
     ▐░▌     ▐░▌            ▐░▌ ▐░▌       ▐░▌     
     ▐░▌     ▐░█▄▄▄▄▄▄▄▄▄  ▐░▌   ▐░▌      ▐░▌     
     ▐░▌     ▐░░░░░░░░░░░▌▐░▌     ▐░▌     ▐░▌     
      ▀       ▀▀▀▀▀▀▀▀▀▀▀  ▀       ▀       ▀                                                                                                                                                                                                       
    """

        result = ""
        for caract in text:
            if caract in ["▄", "▐", "▀", "▌", "█"]:
                result += second_color + caract
            else:
                result += main_color + caract
        if col_reset:
            return result + '\033[38;2;255;255;255m'
        else:
            return result



class Input:
    
    def Void() -> None:
        input()


class Print:

    def Void() -> None:
        print("")


    def Write(text: str,delay_time: str = 0.01) -> str: 
        for character in text:      
            sys.stdout.write(character) 
            sys.stdout.flush()
            time.sleep(delay_time)



class Ascii:
    def Text(texte: str, font: str = 'graffiti') -> str:
        fliget = Figlet(font=font)
        return fliget.renderText(texte)


"""Font List"""    
# 1943____
# 3-d
# 3x5
# 4x4_offr
# 5lineoblique
# 5x7
# 5x8
# 64f1____
# 6x10
# 6x9
# a_zooloo
# acrobatic
# advenger
# alligator
# alligator2
# alphabet
# aquaplan
# arrows
# asc_____
# ascii___
# assalt_m
# asslt__m
# atc_____
# atc_gran
# avatar
# b_m__200
# banner
# banner3
# banner3-D
# banner4
# barbwire
# basic
# battle_s
# battlesh
# baz__bil
# beer_pub
# bell
# big
# bigchief
# binary
# block
# brite
# briteb
# britebi
# britei
# broadway
# bubble
# bubble__
# bubble_b
# bulbhead
# c1______
# c2______
# c_ascii_
# c_consen
# calgphy2
# caligraphy
# catwalk
# caus_in_
# char1___
# char2___
# char3___
# char4___
# charact1
# charact2
# charact3
# charact4
# charact5
# charact6
# characte
# charset_
# chartr
# chartri
# chunky
# clb6x10
# clb8x10
# clb8x8
# cli8x8
# clr4x6
# clr5x10
# clr5x6
# clr5x8
# clr6x10
# clr6x6
# clr6x8
# clr7x10
# clr7x8
# clr8x10
# clr8x8
# coil_cop
# coinstak
# colossal
# com_sen_
# computer
# contessa
# contrast
# convoy__
# cosmic
# cosmike
# cour
# courb
# courbi
# couri
# crawford
# cricket
# cursive
# cyberlarge
# cybermedium
# cybersmall
# d_dragon
# dcs_bfmo
# decimal
# deep_str
# defleppard
# demo_1__
# demo_2__
# demo_m__
# devilish
# diamond
# digital
# doh
# doom
# dotmatrix
# double
# drpepper
# druid___
# dwhistled
# e__fist_
# ebbs_1__
# ebbs_2__
# eca_____
# eftichess
# eftifont
# eftipiti
# eftirobot
# eftitalic
# eftiwall
# eftiwater
# epic
# etcrvs__
# f15_____
# faces_of
# fair_mea
# fairligh
# fantasy_
# fbr12___
# fbr1____
# fbr2____
# fbr_stri
# fbr_tilt
# fender
# finalass
# fireing_
# flyn_sh
# fourtops
# fp1_____
# fp2_____
# fraktur
# funky_dr
# future_1
# future_2
# future_3
# future_4
# future_5
# future_6
# future_7
# future_8
# fuzzy
# gauntlet
# ghost_bo
# goofy
# gothic
# gothic__
# graceful
# gradient
# graffiti
# grand_pr
# greek
# green_be
# hades___
# heavy_me
# helv
# helvb
# helvbi
# helvi
# heroboti
# hex
# high_noo
# hills___
# hollywood
# home_pak
# house_of
# hypa_bal
# hyper___
# inc_raw_
# invita
# isometric1
# isometric2
# isometric3
# isometric4
# italic
# italics_
# ivrit
# jazmine
# jerusalem
# joust___
# katakana
# kban
# kgames_i
# kik_star
# krak_out
# larry3d
# lazy_jon
# lcd
# lean
# letter_w
# letters
# letterw3
# lexible_
# linux
# lockergnome
# mad_nurs
# madrid
# magic_ma
# marquee
# master_o
# maxfour
# mayhem_d
# mcg_____
# mig_ally
# mike
# mini
# mirror
# mnemonic
# modern__
# morse
# moscow
# mshebrew210
# nancyj
# nancyj-fancy
# nancyj-underlined
# new_asci
# nfi1____
# nipples
# notie_ca
# npn_____
# ntgreek
# nvscript
# o8
# octal
# odel_lak
# ogre
# ok_beer_
# os2
# outrun__
# p_s_h_m_
# p_skateb
# pacos_pe
# panther_
# pawn_ins
# pawp
# peaks
# pebbles
# pepper
# phonix__
# platoon2
# platoon_
# pod_____
# poison
# puffy
# pyramid
# r2-d2___
# rad_____
# rad_phan
# radical_
# rainbow_
# rally_s2
# rally_sp
# rampage_
# rastan__
# raw_recu
# rci_____
# rectangles
# relief
# relief2
# rev
# ripper!_
# road_rai
# rockbox_
# rok_____
# roman
# roman___
# rot13
# rounded
# rowancap
# rozzo
# runic
# runyc
# sans
# sansb
# sansbi
# sansi
# sblood
# sbook
# sbookb
# sbookbi
# sbooki
# script
# script__
# serifcap
# shadow
# shimrod
# short
# skate_ro
# skateord
# skateroc
# sketch_s
# slant
# slide
# slscript
# sm______
# small
# smisome1
# smkeyboard
# smscript
# smshadow
# smslant
# smtengwar
# space_op
# spc_demo
# speed
# stacey
# stampatello
# standard
# star_war
# starwars
# stealth_
# stellar
# stencil1
# stencil2
# stop
# straight
# street_s
# subteran
# super_te
# t__of_ap
# tanja
# tav1____
# taxi____
# tec1____
# tec_7000
# tecrvs__
# tengwar
# term
# thick
# thin
# threepoint
# ti_pan__
# ticks
# ticksslant
# tiles
# times
# timesofl
# tinker-toy
# tomahawk
# tombstone
# top_duck
# trashman
# trek
# triad_st
# ts1_____
# tsalagi
# tsm_____
# tsn_base
# tty
# ttyb
# tubular
# twin_cob
# twopoint
# type_set
# ucf_fan_
# ugalympi
# unarmed_
# univers
# usa_____
# usa_pq__
# usaflag
# utopia
# utopiab
# utopiabi
# utopiai
# vortron_
# war_of_w
# wavy
# weird
# whimsy
# xbrite
# xbriteb
# xbritebi
# xbritei
# xchartr
# xchartri
# xcour
# xcourb
# xcourbi
# xcouri
# xhelv
# xhelvb
# xhelvbi
# xhelvi
# xsans
# xsansb
# xsansbi
# xsansi
# xsbook
# xsbookb
# xsbookbi
# xsbooki
# xtimes
# xtty
# xttyb
# yie-ar__
# yie_ar_k
# z-pilot_
# zig_zag_
# zone7___
