import streamlit as st


import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import math
import numpy as np
from matplotlib.patches import Patch, Circle, Polygon, Wedge
import pandas as pd


# def angle_in_sector(angle, center, width):
#     angle = round(angle % (2 * np.pi),6)   # modulo 2 pi
#     center = center % (2 * np.pi) # modulo 2 pi
#     half_width = width / 2
#     lower = round((center - half_width) % (2 * np.pi),6)
#     upper = round((center + half_width) % (2 * np.pi),6)
#     # print('lower < upper ' + str(lower < upper))
#     # if abs(lower-angle)<0.001:
#     #     print('caution with phase lower')
#     #     print(lower*180/np.pi)
#     #     print(angle*180/np.pi)
#     #     print('lower < angle and angle <= upper ' + str(lower < angle and angle <= upper))
#     # if abs(upper-angle)<0.001:
#     #     print('caution with phase upper')
#     #     print(upper*180/np.pi)
#     #     print(angle*180/np.pi)

#     if lower < upper:
#         return lower < angle and angle <= upper
#     else:
#         return angle > lower or angle <= upper


# def star_of_slots(m, nb_poles, nb_slots, nb_layers, fig, ax, title, electrical=False,legend=False):
#     poles_pair = nb_poles / 2
#     base_angles = np.linspace(0, 2 * np.pi, nb_slots, endpoint=False)
#     # phase_labels = ['U', 'V', 'W', 'X', 'Y', 'Z']
#     phase_labels = ['A', 'B', 'C', 'D', 'E', 'F']
#     phase_colors = ['green', 'orange', 'purple', 'cyan', 'magenta', 'brown']
#     sector_width = np.pi / m

#     if electrical:
#         angles = base_angles * poles_pair
#     else:
#         angles = base_angles



#     if electrical:     # Draw phase sectors if in electrical domain - Only for visualization
#         ax.set_theta_zero_location('N')
#         for k in range(m):
#             center_pos = (2 * np.pi * k / m          + 6* np.pi / m /4 ) # décallage de 1/2
#             center_neg = (2 * np.pi * k / m + np.pi + 6* np.pi / m /4  )  # décallage de 1/2
#             for center, alpha in [(center_pos, 0.4), (center_neg, 0.2)]:  # alpha: transparency
#                 start_angle = (center - sector_width / 2) * 180 / np.pi  # degrees
#                 end_angle = (center + sector_width / 2) * 180 / np.pi
#                 wedge = Patch(
#                     facecolor=phase_colors[k % len(phase_colors)],
#                     edgecolor=None,
#                     alpha=alpha,
#                     label=f"{phase_labels[k]} sector",
#                 )
#                 wedge = plt.matplotlib.patches.Wedge((0, 0), 0.9, start_angle, end_angle,
#                                                     width=0.15, color=phase_colors[k % len(phase_colors)],
#                                                     alpha=alpha, zorder=0
#                                                     ,transform=ax.transData._b
#                                                     )
#                 ax.add_patch(wedge)


#     for idx, angle in enumerate(angles): # On itère sur les dents (slots)
#         test_angle = base_angles[idx] * poles_pair  # Always use electrical angle to determine phase
#         phase_label = ''
#         phase_idx = None
#         polarity = None



#         for k in range(m): # on itère sur les phases
#             center_pos = (2 * np.pi * k / m         ) # - np.pi / m /4 )   # décallage de 1/2
#             center_neg = (2 * np.pi * k / m + np.pi ) # - np.pi / m /4  )  # décallage de 1/2

#             if angle_in_sector(test_angle, center_pos, sector_width):
#                 phase_label = phase_labels[k]
#                 phase_idx = k
#                 polarity = '+'
#                 # print("angle "+str(angle*180/np.pi)+" appartient a la phase  "+str(k)+" polarity +")
#                 break
#             elif angle_in_sector(test_angle, center_neg, sector_width):
#                 phase_label = phase_labels[k]
#                 phase_idx = k
#                 polarity = '–'
#                 # print("angle "+str(angle*180/np.pi)+" appartient a la phase  "+str(k)+" polarity -")
#                 break
#             # Sinon il n'appartient pas à cette phase n°k, et on passe a la phase suivante

#         # Use phase color
#         color = phase_colors[phase_idx % len(phase_colors)] if phase_idx is not None else 'gray'


#         # Plot each layer
#         if nb_layers == 2 or  (nb_layers == 1 and idx % 2 == 0 ) : # Si il y a qu'une layer, il faut bobiner une dent sur deux, à améliorer pour prendre en compte n layers # TO DO
#             radius = 1 #+ nb_layers * 0.1
#             if electrical:
#                 ax.plot([0, angle], [0, radius], marker='o', color=color) # plot phasors only for electrical
#                 # Electrical domain: simpler single label
#                 label_radius = 1.3 + (idx * 0.03)
#                 ax.text(angle, label_radius, f"{idx + 1}\n{phase_label}{polarity}", fontsize=8, ha='center', va='center',color=color,rotation=np.degrees(angle), rotation_mode='anchor')
#             else:
#                 # Label only once per slot — for mechanical domain, do dual-side labeling
#                 label_radius = 1 + 0.15
#                 angle_deg = np.degrees(angle)
#                 # Rotate left/right label slightly off-axis
#                 delta = 0.025 + 0.13*10/nb_slots

#                 if polarity == '+':
#                     label_right = f"{phase_label}+"
#                     label_left = f"{phase_label}–"
#                 elif polarity == '–':
#                     label_right = f"{phase_label}-"
#                     label_left = f"{phase_label}+"
#                 else:
#                     label_right = label_left = ""
#                     print('error : no polarity')

#                 # Right side (positive direction)
#                 ax.text(angle + delta, label_radius, label_right,
#                         fontsize=8, color=color, ha='center', va='center',
#                         rotation=angle_deg, rotation_mode='anchor')

#                 # Left side (opposite direction)
#                 ax.text(angle - delta, label_radius, label_left,
#                         fontsize=8, color=color, ha='center', va='center',
#                         rotation=angle_deg, rotation_mode='anchor')



#     ax.set_title(title)


#     if legend == True:
#         # Legend for phases
#         legend_elements = [
#         Patch(facecolor=phase_colors[i], edgecolor='black', label=f'Phase {phase_labels[i]}') for i in range(m)]
#         ax.legend(handles=legend_elements, loc='upper left')


# def draw_magnets(nb_poles, fig, ax):
#     angles = np.linspace(0, 2 * np.pi, nb_poles, endpoint=False)
#     full_width = 2 * np.pi / nb_poles
#     width = 0.8 * full_width

#     for i, angle in enumerate(angles):
#         color = 'blue' if i % 2 == 1 else 'red'
#         ax.bar(angle, 0.15, width=width, bottom=1.5, color=color,
#         #edgecolor='black'
#         )

# def draw_stator(ax, nb_slots, radius_core=1.0, radius_magnet_base=1.3, tooth_width=0.1):
#     """
#     Draw a rotor with:
#     - A gray core circle
#     - Rectangular teeth (bridges) centered on radial phasors
#     - Pole shoes as wedges
#     """
#     # 1. Core rotor circle
#     core = Circle((0, 0), radius_core, transform=ax.transData._b,
#                   color='lightgray', zorder=0)
#     ax.add_patch(core)

#     # 2. Tooth centers
#     angles = np.linspace(0, 2 * np.pi, nb_slots, endpoint=False)  + np.pi / 2  # Pour mettre 0° au nord #+ (np.pi / nb_slots)
#     # ax.set_theta_zero_location('E')
#     # print(angles*180/np.pi)
#     full_angle = 2 * np.pi / nb_slots
#     half_width = 0.02 + 0.1*10/nb_slots / 2
#     #fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
#     # ax.set_theta_zero_location("N")       # Met le 0° en haut
#     for angle in angles:
#         # Base et extrémité du phasor
#         x_start, y_start = radius_core * np.cos(angle), radius_core * np.sin(angle)
#         x_end, y_end = radius_magnet_base * np.cos(angle), radius_magnet_base * np.sin(angle)

#         # Déplacement perpendiculaire pour créer la largeur de la dent
#         dx = half_width * np.cos(angle + np.pi / 2)
#         dy = half_width * np.sin(angle + np.pi / 2)

#         # Rectangle parfaitement droit centré sur le phasor
#         corners = [
#             [x_start - dx, y_start - dy],
#             [x_start + dx, y_start + dy],
#             [x_end + dx, y_end + dy],
#             [x_end - dx, y_end - dy],
#         ]

#         bridge = Polygon(corners, closed=True, color='lightgray', zorder=2,transform=ax.transData._b)
#         ax.add_patch(bridge)

#         # 3. Pole shoe (wedge)
#         shoe_radius = 0.1
#         shoe_outer_r = radius_magnet_base + shoe_radius
#         shoe_angle_deg = np.degrees(full_angle * 0.8)

#         start_angle = np.degrees(angle) - shoe_angle_deg / 2
#         wedge = Wedge(center=(0, 0),
#                       r=shoe_outer_r,
#                       theta1=start_angle,
#                       theta2=start_angle + shoe_angle_deg,
#                       width=shoe_radius,
#                       facecolor='lightgray',
#                       #edgecolor='black',
#                       zorder=3,transform=ax.transData._b)
#         ax.add_patch(wedge)
#     # ax.set_theta_zero_location('N')



# def show_winding(m=3, see_electrical_domain=1, nb_poles = 14, nb_slots = 12, nb_layers = 2):

#     # Mechanical domain
#     fig1, ax1 = plt.subplots(subplot_kw={'projection': 'polar'})
#     ax1.set_theta_zero_location('N')
#     ax1.set_yticklabels([])
#     ax1.set_xticklabels([])
#     ax1.grid(False)
#     # ax1.legend(handles=[
#     #     Patch(facecolor='blue', edgecolor='black', label='Polarity 1'),
#     #     Patch(facecolor='red', edgecolor='black', label='Polarity 2')],
#     #     loc='upper right')
#     star_of_slots(m, nb_poles, nb_slots, nb_layers, fig1, ax1, f"Mechanical domain for a machine with {nb_slots} slots and {nb_poles} poles")
#     draw_magnets(nb_poles, fig1, ax1)
#     draw_stator(ax1, nb_slots)

#     if see_electrical_domain ==1:
#         # Electrical domain
#         fig2, ax2 = plt.subplots(subplot_kw={'projection': 'polar'})
#         ax2.set_theta_zero_location('N')
#         ax2.set_yticklabels([])
#         ax2.set_xticklabels([])
#         ax2.grid(False)
#         star_of_slots(m, nb_poles, nb_slots, nb_layers, fig2, ax2, f"Electrical domain for a machine with {nb_slots} slots and {nb_poles} poles", electrical=True)
#         #draw_rotor(ax, nb_poles, radius_core=1.0, radius_magnet_base=1.5, tooth_width=0.1)

#     plt.show()


# def calculate_winding_characteristics(m,Ns,p,nb_layers):
#     q = Ns / p / m # Nombre d'encoches par pôle et par phase (q) il est préférable d'avoir q ∈ [ 0.25 ; 0.5 ], car en dehors de cet intervalle il y a plusieurs pôles qui interragissement avec une seule dent, ou plusieurs dents qui interragissent avec le même pôle, ce qui n'est pas optimal. Il ne faudrait pas avoir q = 1/3, car cela ne permet pas pas d'avoir un système équilibré
#     pole_pairs = p/2
#     z = Ns*1/(3-(nb_layers))/(math.gcd(Ns,p*m))
#     harmonic_nb = 1
#     sigma = 2*np.pi/2/m
#     kmn = math.sin(0.5 * harmonic_nb * sigma) / ( z * math.sin( harmonic_nb * sigma / (2*z) ) )
#     gamma_s = np.pi/(q * m)
#     epsilon = np.pi - gamma_s # chroding or coil-span angle
#     ken = np.cos(0.5*harmonic_nb*epsilon)
#     kw = ken * kmn # winding_factor
#     f_torque = ppcm(p,Ns) # Frequence des ondulations de couple (lorsque le moteur n'est pas alimenté)
#     nb_of_identic_sections = math.gcd(Ns,p)
#     S = (Ns/(m*math.gcd(Ns,int(p/2)))) # Indicator of unbalanced winding
#     S = S - int(S)
#     warning_flag = False
#     if kw<0.85:
#         print("Warning, the winding factor is low")
#         warning_flag = True
#     if q < 0.25:
#         print("Warning, there are multiple north and south magnet poles interacting with each stator tooth, which is not optimal")
#         warning_flag = True
#     if q > 0.5:
#         print("Warning, a single rotor pole will span over multiple teeth, which is not optimal")
#         warning_flag = True
#     if nb_of_identic_sections < 2:
#         print("Warning, there is no symmetry, which can result in high level of vibrations")
#         warning_flag = True
#     if S > 0:
#         print("Warning, the winding is unbalanced")
#         warning_flag = True
#     return kw, f_torque, nb_of_identic_sections,warning_flag

# def ask_user():
#     nb_poles = 3
#     while nb_poles % 2 != 0:     # Verification

#         nb_poles = int(input("Enter the number of poles: "))
#         poles_pair = nb_poles /2
#         if nb_poles % 2 != 0:
#             print("Error : The number of poles is not even")

#     nb_slots = 1
#     while nb_slots % 3 != 0:     # Verification

#         nb_slots = int(input("Enter the number of slots: "))
#         if nb_slots % 3 != 0:
#             print("Error : the phase number should be 3 and the number of slots should be a multiple of the number of slots !")

#     nb_layers = 0 # TO BE FIXED in star_of_slots function
#     while ((nb_layers != 1) and  (nb_layers != 2))  :     # Verification

#         nb_layers = int(input("Enter the number of layers: "))
#         if ((nb_layers != 1) and  (nb_layers != 2)) :
#             print("Error : the number of layers should be 1 or 2")
#     return nb_poles, nb_slots, nb_layers


# def ppcm(a,b): # plus petit multiple commun
#     return a*b/math.gcd(a,b)




# st.title("Visualisation du bobinage d'une machine électrique")

# m = 3
# nb_poles = st.slider("Nombre de pôles", min_value=2, max_value=40, step=2, value=10)
# nb_slots = st.slider("Nombre d'encoches", min_value=3, max_value=60, step=3, value=12)
# nb_layers = st.selectbox("Nombre de couches", options=[1, 2], index=1)

# kw, f_torque, sections, warning_flag = calculate_winding_characteristics(m, nb_slots, nb_poles, nb_layers)

# st.write(f"Winding Factor : {kw:.3f}")
# st.write(f"Nombre de sections identiques : {sections}")
# st.write(f"Fréquence d'ondulation du couple : {f_torque}")

# fig1, ax1 = plt.subplots(subplot_kw={'projection': 'polar'})
# ax1.set_theta_zero_location('N')
# ax1.set_yticklabels([])
# ax1.set_xticklabels([])
# ax1.grid(False)

# star_of_slots(m, nb_poles, nb_slots, nb_layers, fig1, ax1, "Domaine mécanique")
# draw_magnets(nb_poles, fig1, ax1)
# draw_stator(ax1, nb_slots)

# st.pyplot(fig1)


plt.close('all')

def number_to_letter(n):
    """Convertit 1 → 'a', 2 → 'b', ..., 26 → 'z'"""
    return chr(ord('a') + int(n) - 1)


def angle_in_sector(angle, center, width):
    angle = round(angle % (2 * np.pi),6)   # modulo 2 pi , 6 chiffres après la virgule
    center = center % (2 * np.pi) # modulo 2 pi
    half_width = width / 2
    lower = round((center - half_width) % (2 * np.pi),6)
    upper = round((center + half_width) % (2 * np.pi),6)

    if lower < upper:
        return lower < angle and angle <= upper
    else:
        return angle > lower or angle <= upper
    

def star_of_slots(winding_type, m, nb_poles, nb_slots, nb_layers, fig, ax, electrical=False,legend=False,raccourcissement=0,plot_fig = True,plot_end_turns=False,silent = True,export_motorcad_tables=False):
    poles_pair = nb_poles / 2
    base_angles = np.linspace(0, 2 * np.pi, nb_slots, endpoint=False)
    # phase_labels = ['U', 'V', 'W', 'X', 'Y', 'Z']
    # phase_colors = ['green', 'orange', 'purple', 'cyan', 'magenta', 'brown']
    phase_labels = ['A', 'B', 'C', 'D', 'E', 'F']
    phase_colors = ['red','blue','green', 'orange', 'purple', 'cyan'] 
    sector_width = np.pi / m
    radius_phasor = 1 
    tooth_height = 0.43
    phasors = {label: [] for label in phase_labels[:m]}
    Conductors_distribution = np.zeros((nb_slots,m))
    warning_flag = False
    
    if nb_layers > 1 :
        radius_increment = tooth_height / (2*(nb_layers - 1 ) )
    else : 
        radius_increment = 0

    fontsize = 7 + radius_increment / (0.45/2)  

    # Dictionnaire pour compter les conducteurs
    conductor_count = {label: {'+': 0, '-': 0} for label in phase_labels[:m]}

    if electrical:
        # angles = base_angles * poles_pair
        draw_phase_sector(ax,m,phase_colors,phase_labels,sector_width)  # Draw phase sectors if in electrical domain - Only for visualization
    # else:
        # angles = base_angles

    if export_motorcad_tables == True:
        output_file = 'winding.xlsx'
        writer = pd.ExcelWriter(output_file, engine='xlsxwriter')
        data = {label: [] for label in phase_labels[:m]}
        coil_index = [1 for i in range(m)]
        turns_per_coil = 10 # To be changed
        conductor_pos='None'

    if winding_type == 'Bobinage distribué à pas raccourcit' or winding_type == 'Bobinage distribué à nombre d’encoches par pôle et par phase entier' or winding_type == 'Bobinage à pas dentaire': 

        slot_pitch = 2 * np.pi / nb_slots
        # pole_pitch_nb = nb_slots / nb_poles
        # pole_pitch = pole_pitch_nb * slot_pitch
        # raccourcissement_factor = raccourcissement / pole_pitch

        if  winding_type == 'Bobinage distribué à pas raccourcit' or winding_type == 'Bobinage distribué à nombre d’encoches par pôle et par phase entier':
            coil_span_nb = raccourcissement
        elif winding_type == 'Bobinage à pas dentaire':
            coil_span_nb = 1

        coil_span = coil_span_nb * slot_pitch
        label_radius = 1.15
        previous_slot = -1 # intitialisation à -1 pour commencer à 0

        for idx in range(int(nb_layers * nb_slots / 2)): # on itère sur le nombre de bobines a placer, on divise par deux car on affecte l'aller et le retour en une fois d'une spire
            
            slot_number = (previous_slot+1)% nb_slots
            slot_number_return = (slot_number+coil_span_nb)%nb_slots
            counter = 0
            while (sum(abs(Conductors_distribution[slot_number,:])) == 1 or sum(abs(Conductors_distribution[slot_number_return,:])) == 1 ) and counter <= slot_number: # si l'aller ou le retour sont plein
                slot_number = (slot_number+1)% nb_slots
                slot_number_return = (slot_number+coil_span_nb)%nb_slots
                counter += 1 # pour éviter de rester coincer

            if counter > slot_number:
                if silent ==False:
                    print('error, winding is not possible')
                warning_flag = True


            layer_number = sum(abs(Conductors_distribution[slot_number,:]))*nb_layers +1
            layer_number_return = sum(abs(Conductors_distribution[slot_number_return,:]))*nb_layers +1

            
            # if nb_layers == 1 and winding_type == 'Bobinage à pas dentaire' :
            #     slot_number = 2 * (idx) % nb_slots 
            # else:
            #     slot_number = (idx) % nb_slots # bobinages distribué
            # layer_number = ((idx) // nb_slots) *2


            angle = slot_number * slot_pitch
            angle_elec = angle * poles_pair + np.pi / 6


            # print('\n idx cond number : ' + str(idx) + ' | slot nb : ' + str(slot_number) + ' | nb layer : ' + str(layer_number))

            for j in range(m):
                center_pos = (-2 * np.pi * j / m)
                center_neg = (-2 * np.pi * j / m + np.pi)
                # print('idx : ' + str(idx))
                # print('phase : ' + str(j))
                if angle_in_sector(angle_elec, center_pos, sector_width):
                    phase_label = phase_labels[j]
                    phase_idx = j
                    polarity = '+'
                    Conductors_distribution[slot_number,j]    +=    1/nb_layers
                    Conductors_distribution[slot_number_return,j] +=  - 1/nb_layers
                    break
                elif angle_in_sector(angle_elec, center_neg, sector_width):
                    phase_label = phase_labels[j]
                    phase_idx = j
                    polarity = '-'
                    # print('ok?')
                    Conductors_distribution[slot_number,j]              += - 1/nb_layers
                    Conductors_distribution[slot_number_return,j] +=   1/nb_layers
                    break            

            color = phase_colors[phase_idx % len(phase_colors)] if phase_idx is not None else 'gray'
            # print("angle " + str(angle * 180 / np.pi) + " appartient à la phase " + str(phase_label) + " polarity " + polarity)

            if polarity == '+':
                label_right = f"{phase_label}+"
                label_left = f"{phase_label}-"
            elif polarity == '-':
                label_right = f"{phase_label}-"
                label_left = f"{phase_label}+"

            if export_motorcad_tables == True:
                throw = (slot_number_return - slot_number) % nb_slots
                return_layer_letter = number_to_letter(layer_number_return)
                go_layer_letter = number_to_letter(layer_number)

                if polarity == '+':
                    data[phase_label].append({
                        "Coil": coil_index[j],
                        "Path": 1,
                        "Go": slot_number + 1,
                        # "PosGo": go_layer_letter,
                        "Return": slot_number_return + 1,
                        # "PosReturn": return_layer_letter,
                        "Throw": throw,
                        "Turns": turns_per_coil
                    })
                
                elif polarity == '-':
                    data[phase_label].append({
                        "Coil": coil_index[j],
                        "Path": 1,
                        "Go": slot_number_return + 1,
                        # "PosGo": return_layer_letter,
                        "Return": slot_number + 1,
                        # "PosReturn": go_layer_letter,
                        "Throw": throw,
                        "Turns": turns_per_coil
                    })
                    
                coil_index[j] += 1

        

            if electrical: # ici les phasors représentent les bobinages des encoches
                angle_elec_retour = angle_elec+coil_span*poles_pair
                if plot_fig == True:
                    ax.plot([0, angle_elec+0.01*np.random.random()], [0, radius_phasor], marker='o', color=color) # plot phasors only for electrical , on ajoute un peu d'aléatoire pour pouvoir deviner les phasors quand ils se supperposent
                    ax.plot([0, angle_elec_retour+0.01*np.random.random()], [0, radius_phasor], marker='o', color=color) # plot phasors only for electrical
                    # Electrical domain: simpler single label
                    # label_radius1 = label_radius + 0.05 * idx#+ np.random.randint(0, 0.,) 
                    ax.text(angle_elec, label_radius, f"{idx + 1}\n{label_right}", fontsize=8, ha='center', va='center',color=color,rotation=angle_elec*180/np.pi, rotation_mode='anchor')
                    ax.text(angle_elec_retour, label_radius+radius_increment, f"{idx + 1}\n{label_left}", fontsize=8, ha='center', va='center',color=color,rotation=(angle_elec_retour)*180/np.pi, rotation_mode='anchor')

                if electrical and phase_label in phasors and polarity in ('+', '-'):
                    signe = 1 if polarity == '+' else -1
                    phasor_depart = signe * np.exp(1j * angle_elec)
                    phasor_retour = signe * np.exp(1j * angle_elec_retour)
                    phasors[phase_label].append(phasor_depart)
                    phasors[phase_label].append(phasor_retour)


            else : # mechanical domain
                if winding_type == 'Bobinage à pas dentaire' and nb_layers == 2 and plot_fig == True: # Affichage différent pour les bobinages concentrés autour des dents à deux couches (conducteurs séparer à la moitié d'un slot)
                    delta = 0.025 + 0.13*10/nb_slots
                    # Right side (positive direction)
                    angle_right = angle  + delta + slot_pitch/2.5
                    angle_deg_right = 180/(np.pi)*(angle_right)
                    label_radius_right = label_radius #+ radius_increment * (layer_number+0.5)
                    ax.text(angle_right, label_radius_right, label_right,
                            fontsize=fontsize, color=color, ha='center', va='center',
                            rotation=angle_deg_right, rotation_mode='anchor')

                    # Left side (opposite direction) (seconde partie de la bobine)
                    angle_left =  angle_right - delta + coil_span
                    angle_deg_left = 180/(np.pi)* angle_left
                    label_radius_left = label_radius #- radius_increment * (layer_number+0.5)
                    ax.text(angle_left , label_radius_left, label_left,
                            fontsize=fontsize, color=color, ha='center', va='center',
                            rotation=angle_deg_left, rotation_mode='anchor')

                elif plot_fig == True: # bobinages distribué ou concentré a une couche (conducteurs au centre des slots)
                    # Right side (positive direction)
                    angle_right = angle + slot_pitch/2
                    angle_deg_right = 180/(np.pi)*(angle_right)
                    label_radius_right = label_radius + radius_increment * (layer_number-1.5)
                    ax.text(angle_right, label_radius_right, label_right,
                            fontsize=fontsize, color=color, ha='center', va='center',
                            rotation=angle_deg_right, rotation_mode='anchor')

                    # Left side (opposite direction) (seconde partie de la bobine)
                    angle_left =  angle_right + coil_span
                    angle_deg_left = 180/(np.pi)* angle_left
                    # label_radius_left = label_radius_right - radius_increment #label_radius_left = label_radius + radius_increment * (layer_number+0.5) # = label_radius - radius_increment * (layer_number+0.5)
                    label_radius_left = label_radius + radius_increment * (layer_number_return-1.5)

                    ax.text(angle_left , label_radius_left, label_left,
                            fontsize=fontsize, color=color, ha='center', va='center',
                            rotation=angle_deg_left, rotation_mode='anchor')

                

                if plot_end_turns == True:
                    # ➔ Ajouter un trait entre les deux côtés de la bobine
                    # Coordonnées initiales
                    x_start = label_radius_right * np.cos(angle_right + np.pi/2)
                    y_start = label_radius_right * np.sin(angle_right + np.pi/2)
                    x_end = label_radius_left * np.cos(angle_left + np.pi/2)
                    y_end = label_radius_left * np.sin(angle_left + np.pi/2)

                    # Calcul du vecteur directionnel unitaire
                    dx = x_end - x_start
                    dy = y_end - y_start
                    length = np.sqrt(dx**2 + dy**2)
                    ux, uy = dx / length, dy / length  # vecteur unitaire

                    # Application du décalage de 0.05 dans la direction de la ligne
                    x_start_new = x_start + 0.05 * ux
                    y_start_new = y_start + 0.05 * uy
                    x_end_new = x_end - 0.05 * ux
                    y_end_new = y_end - 0.05 * uy

                    # Tracé de la ligne raccourcie
                    ax.plot([x_start_new, x_end_new], [y_start_new, y_end_new],
                            color=color, linewidth=1.0, zorder=9, transform=ax.transData._b)
            previous_slot = slot_number
        if legend == True and plot_fig == True:
            # Legend for phases
            legend_elements = [
            Patch(facecolor=phase_colors[i], edgecolor='black', label=f'Phase {phase_labels[i]}') for i in range(m)]
            ax.legend(handles=legend_elements, loc='upper left')
            
    if export_motorcad_tables == True:
        
        for label in phase_labels[:m]:
            df = pd.DataFrame(data[label], columns=["Coil", "Path", "Go", "PosGo", "Return", "PosReturn", "Throw", "Turns"])
            df.to_excel(writer, sheet_name=label, index=False)
        
        # for phase_label in range(m):
        #     df = pd.DataFrame(data[phase_label], columns=["Coil", "Path", "Go", "Pos", "Return", "Pos", "Throw", "Turns"])
        #     df.to_excel(writer, sheet_name=phase_label, index=False)
        
        
        try:
            writer.close()
            print("✅ Excel file generated.")
        except Exception as e:
            print("❌ Error exporting Excel:", e)
                            
        # writer.close()
        # print(f"✅ Fichier Excel généré : {output_file}")
        
    return phasors,Conductors_distribution,warning_flag
     
        
def draw_phase_sector(ax,m,phase_colors,phase_labels,sector_width):
    ax.set_theta_zero_location('N')
    for k in range(m):
        center_pos = (-2 * np.pi * k / m         - 6* np.pi / m /4 ) # décallage de 1/2
        center_neg = (-2 * np.pi * k / m + np.pi - 6* np.pi / m /4  )  # décallage de 1/2
        for center, alpha in [(center_pos, 0.4), (center_neg, 0.2)]:  # alpha: transparency
            start_angle = (center - sector_width / 2) * 180 / np.pi  # degrees
            end_angle = (center + sector_width / 2) * 180 / np.pi
            wedge = Patch(
                facecolor=phase_colors[k % len(phase_colors)],
                edgecolor=None,
                alpha=alpha,
                label=f"{phase_labels[k]} sector",
            )
            wedge = plt.matplotlib.patches.Wedge((0, 0), 0.9, start_angle, end_angle,
                                                width=0.15, color=phase_colors[k % len(phase_colors)],
                                                alpha=alpha, zorder=0
                                                ,transform=ax.transData._b
                                                )
            ax.add_patch(wedge)

def draw_magnets(nb_poles, fig, ax):
    angles = np.linspace(0, 2 * np.pi, nb_poles, endpoint=False)
    full_width = 2 * np.pi / nb_poles
    width = 0.8 * full_width

    for i, angle in enumerate(angles):
        color = 'blue' if i % 2 == 1 else 'red'
        ax.bar(angle, 0.15, width=width, bottom=1.5, color=color, 
        #edgecolor='black'
        )

def draw_stator(ax, nb_slots, radius_core=1.0, radius_magnet_base=1.3, tooth_width=0.1):
    """
    Draw a rotor with:
    - A gray core circle
    - Rectangular teeth (bridges) centered on radial phasors
    - Pole shoes as wedges
    """
    # 1. Core rotor circle
    core = Circle((0, 0), radius_core, transform=ax.transData._b,
                  color='lightgray', zorder=0)
    ax.add_patch(core)

    # 2. Tooth centers
    angles = np.linspace(0, 2 * np.pi, nb_slots, endpoint=False)  + np.pi / 2  # Pour mettre 0° au nord #+ (np.pi / nb_slots)
    # ax.set_theta_zero_location('E')
    # print(angles*180/np.pi)
    full_angle = 2 * np.pi / nb_slots
    half_width = 0.02 + 0.1*10/nb_slots / 2
    #fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    # ax.set_theta_zero_location("N")       # Met le 0° en haut
    for angle in angles:
        # Base et extrémité du phasor
        x_start, y_start = radius_core * np.cos(angle), radius_core * np.sin(angle)
        x_end, y_end = radius_magnet_base * np.cos(angle), radius_magnet_base * np.sin(angle)

        # Déplacement perpendiculaire pour créer la largeur de la dent
        dx = half_width * np.cos(angle + np.pi / 2)
        dy = half_width * np.sin(angle + np.pi / 2)

        # Rectangle parfaitement droit centré sur le phasor
        corners = [
            [x_start - dx, y_start - dy],
            [x_start + dx, y_start + dy],
            [x_end + dx, y_end + dy],
            [x_end - dx, y_end - dy],
        ]
        
        bridge = Polygon(corners, closed=True, color='lightgray', zorder=2,transform=ax.transData._b)
        ax.add_patch(bridge)
            
        # 3. Pole shoe (wedge)
        shoe_radius = 0.1
        shoe_outer_r = radius_magnet_base + shoe_radius
        shoe_angle_deg = np.degrees(full_angle * 0.8)

        start_angle = np.degrees(angle) - shoe_angle_deg / 2
        wedge = Wedge(center=(0, 0),
                      r=shoe_outer_r,
                      theta1=start_angle,
                      theta2=start_angle + shoe_angle_deg,
                      width=shoe_radius,
                      facecolor='lightgray',
                      #edgecolor='black',
                      zorder=3,transform=ax.transData._b)
        ax.add_patch(wedge)
    # ax.set_theta_zero_location('N')



def export_motorcad_tables(Conductors_distribution, turns_per_coil, output_file="winding_tables.xlsx",nb_layers=2):
    """
    Génère les tableaux de bobines pour Motor-CAD à partir d'une distribution de conducteurs.
    
    Args:
        Conductors_distribution: numpy array (nb_slots x nb_phases) avec valeurs +1, -1, 0
        turns_per_coil: nombre de spires par bobine
        output_file: nom du fichier Excel de sortie
    """
    conductor_weight = 1/nb_layers
    # print(Conductors_distribution)
    nb_slots, nb_phases = Conductors_distribution.shape
    writer = pd.ExcelWriter(output_file, engine='xlsxwriter')

    for phase in range(nb_phases):
        phase_label = f"Phase {phase+1}"
        data = []
        coil_index = 1

        # Trouve les positions des +1 et -1 pour cette phase
        plus_slots = np.where(Conductors_distribution[:, phase] == conductor_weight)[0]
        minus_slots = np.where(Conductors_distribution[:, phase] == -conductor_weight)[0]

        if len(plus_slots) != len(minus_slots):
            print(f"⚠️ Phase {phase+1} : Nombre de départs (+1) différent du nombre de retours (-1)")

        for go, ret in zip(plus_slots, minus_slots):
            throw = (ret - go) % nb_slots
            data.append({
                "Coil": coil_index,
                "Path": 1,
                "Go": go + 1,
                "Pos": "a",
                "Return": ret + 1,
                "Pos": "a",
                "Throw": throw,
                "Turns": turns_per_coil
            })
            coil_index += 1

        df = pd.DataFrame(data, columns=["Coil", "Path", "Go", "Pos", "Return", "Pos", "Throw", "Turns"])
        df.to_excel(writer, sheet_name=phase_label, index=False)

    writer.close()
    print(f"✅ Fichier Excel généré : {output_file}")



def show_winding(m=3, see_electrical_domain=1, nb_poles = 14, nb_slots = 12, nb_layers = 2, raccourcissement =0, vrillage_encoche = 0, plot_end_turns = False, silent = True):
    
    # Mechanical domain
    fig1, ax1 = plt.subplots(subplot_kw={'projection': 'polar'})
    ax1.set_theta_zero_location('N')
    ax1.set_yticklabels([])
    ax1.set_xticklabels([])
    ax1.grid(False)
    # ax1.legend(handles=[
    #     Patch(facecolor='blue', edgecolor='black', label='Polarity 1'),
    #     Patch(facecolor='red', edgecolor='black', label='Polarity 2')],
    #     loc='upper right')

    f_torque, sections,winding_type, warning = calculate_winding_characteristics(3, nb_slots, nb_poles, nb_layers,raccourcissement)
    phasors,Conductors_distribution,warning_flag = star_of_slots(winding_type, m, nb_poles, nb_slots, nb_layers, fig1, ax1,raccourcissement=raccourcissement,plot_end_turns=plot_end_turns, silent = True)
    # ax1.set_title(f"Mechanical domain for a machine with {nb_slots} slots and {nb_poles} poles")
    kw = calculer_facteur_de_bobinage(phasors,Conductors_distribution,nb_slots,nb_poles,m,silent=False)
    print(f"Vous avez choisit de visualiser un bobinage avec {nb_slots} encoches, {nb_poles} poles et {nb_layers} couches.")
    # print(f"Facteur de bobinage: {kw:.3f} (vrillage de {vrillage_encoche} encoches)    |    Fréquence des ondulations de couple: {f_torque} par tour    |    Sections identiques: {sections}    |    Type de bobinage: {winding_type}")
    print(f"Facteur de bobinage: {kw:.3f}    |    Fréquence des ondulations de couple: {f_torque} par tour    |    Sections identiques: {sections}    |    Type de bobinage: {winding_type}")
    
    export_winding = False
    if export_winding:
        export_motorcad_tables(Conductors_distribution, turns_per_coil=5, output_file="motorcad_windings.xlsx",nb_layers=nb_layers)

    # Titre principal
    title_string = f"Bobinage d'une machine de {nb_slots} encoches, {nb_poles} pôles, \n Avec {nb_layers} couches et un pas de bobine de {raccourcissement} slots"
    fig1.suptitle(title_string, y=0.85, fontsize=11)

    
    # Texte informatif en bas
    fig1.text(
        0.5, 0.06,  
        f"Facteur de bobinage: {kw:.3f}  \nFréquence des ondulations de couple: {f_torque} par tour    \nSections identiques: {sections}    \nType de bobinage: {winding_type}", 
        ha='center', 
        va='bottom', 
        fontsize=10,
        bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.8'),
        zorder=10
    )

    #   fig1.text(
    #     0.5, 0.06,  
    #     f"Facteur de bobinage: {kw:.3f} (vrillage de {vrillage_encoche} encoches)  \nFréquence des ondulations de couple: {f_torque} par tour    \nSections identiques: {sections}    \nType de bobinage: {winding_type}", 
    #     ha='center', 
    #     va='bottom', 
    #     fontsize=10,
    #     bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.8'),
    #     zorder=10
    # )

#     fig1.text(0.5, 0.06, 
#             f"Facteur de bobinage: {kw:.3f}    \nFréquence des ondulations de couple: {f_torque} par tour    \nSections identiques: {sections}    \nType de bobinage: {winding_type}", 
#             ha='left', va='bottom', fontsize=10)
# #             f"Facteur de bobinage: {kw:.3f}    \n|    Fréquence des ondulations de couple: {f_torque} par tour    \n|    Sections identiques: {sections}    \n|    Type de bobinage: {winding_type}", 
    # Optionnel : ajuster les marges pour que tout soit visible
    fig1.tight_layout(rect=[0, 0.03, 1, 0.95])

    if warning_flag:
        print("Warning: Some winding characteristics are suboptimal")
    # if kw < 0.85:
    #     print("Attention, le facteur de bobinage n'est pas très élevé")
    #     warning_flag = True
    # star_of_slots(winding_type, m, nb_poles, nb_slots, nb_layers, fig1, ax1, f"Mechanical domain for a machine with {nb_slots} slots and {nb_poles} poles",raccourcissement=raccourcissement,plot_end_turns=plot_end_turns, silent = False)
    draw_magnets(nb_poles, fig1, ax1)
    draw_stator(ax1, nb_slots)

    if see_electrical_domain == 1:    
        # Electrical domain
        fig2, ax2 = plt.subplots(subplot_kw={'projection': 'polar'})
        ax2.set_theta_zero_location('N')
        ax2.set_yticklabels([])
        ax2.set_xticklabels([])
        star_of_slots(winding_type, m, nb_poles, nb_slots, nb_layers, fig2, ax2, electrical=True,raccourcissement=raccourcissement)
        title_string = f"Domaine électrique pour une machine avec {nb_slots} encoches et {nb_poles} pôles"
        fig2.suptitle(title_string, y=0.95, fontsize=12)
        # ax2.set_title(f"Winding Factor: {kw:.3f}\nTorque Ripple Freq: {f_torque}\nIdentic Sections: {sections}\nWinding type: {winding_type}")

        ax2.grid(False)
        if silent == False:
            print('phasors : ')
            print(phasors)
        # print(' facteur de bobinage géometrique  : ')
        #draw_rotor(ax, nb_poles, radius_core=1.0, radius_magnet_base=1.5, tooth_width=0.1)
        
        # Diagnostic de symétrie (basé sur le PGCD des encoches et demi-pôles)
    pgcd = math.gcd(nb_slots, nb_poles // 2)
    has_no_symmetry = (pgcd == 1)

    # Vérification d'équilibre du bobinage
    total_conductors = nb_slots * nb_layers
    is_unbalanced = (total_conductors % 6 != 0)

    # Avertissement si facteur de bobinage faible
    # warning_flag = kw < 0.85

    results = {
        "kw": kw,
        "torque_ripple_freq": f_torque,
        "identical_sections": sections,
        "winding_type": winding_type,
        "has_no_symmetry": has_no_symmetry,
        "is_unbalanced": is_unbalanced,
        "warning_flag": warning_flag
    }

    plt.show(block=False)
    return results



def calculate_winding_characteristics(m,Ns,p,nb_layers,coil_span,silent = False):
    q = Ns / p / m # Nombre d'encoches par pôle et par phase (q) il est préférable d'avoir q ∈ [ 0.25 ; 0.5 ], car en dehors de cet intervalle il y a plusieurs pôles qui interragissement avec une seule dent, ou plusieurs dents qui interragissent avec le même pôle, ce qui n'est pas optimal. Il ne faudrait pas avoir q = 1/3, car cela ne permet pas pas d'avoir un système équilibré
    pole_pairs = p/2

    winding_types = ['Bobinage distribué à nombre d’encoches par pôle et par phase entier','Bobinage distribué à pas raccourcit','Bobinage à pas dentaire']
    harmonic_nb = 1


    if coil_span == 1 : #or q < 1 :
        winding_type = winding_types[2]
    
    elif q-int(q) == 0 : # Si q est entier 
        winding_type = winding_types[0]
        kw = 1
    elif q > 1 : # Si q est fractionnaire et supérieur à 1
        # coil_span = raccourcissement # TO BE MODIFIED
        winding_type = winding_types[1]
    else :
        winding_type = "bobinage inconnu"

    f_torque = ppcm(p,Ns) # Frequence des ondulations de couple (lorsque le moteur n'est pas alimenté)
    nb_of_identic_sections = math.gcd(Ns,p)
    S = (Ns/(m*math.gcd(Ns,int(p/2)))) # Indicator of unbalanced winding
    S = S - int(S)
    warning_flag = False
    # if kw<0.85:
    #     print("Warning, the winding factor is low")
    #     warning_flag = True
    if q < 0.25:
        if silent == False:
            print("Warning, there are multiple north and south magnet poles interacting with each stator tooth, which is not optimal")
        warning_flag = True
    # if q > 0.5:
    #     print("Warning, a single rotor pole will span over multiple teeth, which is not optimal")
    #     warning_flag = True
    if nb_of_identic_sections < 2:
        if silent == False:
            print("Warning, there is no symmetry, which can result in high level of vibrations")
        warning_flag = True
    if S > 0:
        if silent == False:
            print("Warning, the winding is unbalanced")
        warning_flag = True
    return f_torque, nb_of_identic_sections,winding_type,warning_flag

def ask_user():
    nb_poles = 3
    while nb_poles % 2 != 0:     # Verification

        nb_poles = int(input("Enter the number of poles: "))
        poles_pair = nb_poles /2 
        if nb_poles % 2 != 0:
            print("Error : The number of poles is not even")

    nb_slots = 1
    while nb_slots % 3 != 0:     # Verification

        nb_slots = int(input("Enter the number of slots: "))
        if nb_slots % 3 != 0:
            print("Error : the phase number should be 3 and the number of slots should be a multiple of the number of slots !")

    nb_layers = 0 # TO BE FIXED in star_of_slots function
    while nb_layers > 30 or nb_layers == 0: # ((nb_layers != 1) and  (nb_layers != 2))  :     # Verification

        nb_layers = int(input("Enter the number of layers: "))
        # if ((nb_layers != 1) and  (nb_layers != 2)) :
        #     print("Error : the number of layers should be 1 or 2")
    if (int(nb_layers * nb_slots / 2) != (nb_layers * nb_slots / 2)):
        print("Bobinage non possible (nombre d'emplacements de bras de bobines non pair)")
    print(f"Vous avez choisit de visualiser un bobinage avec {nb_slots} encoches, {nb_poles} pôles et {nb_layers} couches.")

    return nb_poles, nb_slots, nb_layers


def ppcm(a,b): # plus petit multiple commun
    return a*b/math.gcd(a,b)


def calculer_facteur_de_bobinage(phasors,Conductors_distribution,nb_slots,nb_poles,m,silent = True):
    # angle_vrillage_rad = vrillage_encoche * 2*np.pi/nb_slots
    # if vrillage_encoche == 0:
    #     facteur_de_vrillage_fondamental =  1
    # else : 
    #     facteur_de_vrillage_fondamental = np.sin( ( nb_poles*angle_vrillage_rad )/2) / (nb_poles*angle_vrillage_rad/2)
    # kw = []
    longueurs = [len(slots) for slots in phasors.values()]

    # Vérification de l'équilibre des conducteurs entre phases
    if len(set(longueurs)) > 1:
        if silent == False:
            print("⚠️ Déséquilibre : les phases n'ont pas le même nombre de conducteurs.")
        for phase, slots in phasors.items():
            if silent == False:
                print(f"  Phase {phase} : {len(slots)} conducteurs")
    else:
        if silent == False:
            print("✅ Les trois phases ont un nombre équilibré de conducteurs.")

    
    # '''d'après : General, compact and easy-to-compute winding factor formulation - Franck Scuiller '''
    Q = nb_slots  # Number of slots
    N = m   # number of phases
    p = nb_poles/2   # Number of pole pairs

    # Space harmonic winding factor vector
    Kw_v_space = (N / Q) * np.fft.fft(Conductors_distribution[:,0])

    # Electric harmonic order remapping: indices = mod(p * [0:Q-1], Q)
    indices = (p * np.arange(Q)) % Q
    Kw_h_electrical = Kw_v_space[indices.astype(int)]

    # Optional: print fundamental (1st) harmonic component
    kw_fundamental = Kw_h_electrical[1]
    # print(f"Fundamental winding factor (complex): {kw_fundamental}")
    # print(f"Amplitude (|kw|): {abs(kw_fundamental):.3f}")
    return abs(kw_fundamental)

def coil_span_possibilities_list(nb_layer, nb_slot, nb_pole):
    try:
        nb_layer = int(nb_layer)
        nb_slot = int(nb_slot)
        nb_pole = int(nb_pole)
        m = 3 # nb de phases
        if nb_slot/(nb_pole*m) < 1 :
           poss_list = [1]
        else:
           poss_list =  list(range(nb_slot//2,0,-1))
    except ValueError:
        return []
    return poss_list

def layers_possibilities_list(nb_slot, nb_pole):
    try:
        nb_slot = int(nb_slot)
        nb_pole = int(nb_pole)
        m = 3 # nb de phases
        
        if int(nb_slot/2)!=nb_slot/2:
            poss_list =  [2,4,6,8]    
        else :
            poss_list =  [1,2,4,6,8]
    except ValueError:
        return []
    return poss_list

class WindingApp:
    def __init__(self, master):
        self.master = master
        master.title("Outil de visualisation des bobinages")
        master.configure(bg='white')

        default_font = ("Segoe UI", 10)
        label_opts = {'bg': 'white', 'fg': 'black', 'font': default_font}
        button_opts = {'bg': '#0078D7', 'fg': 'white', 'font': ("Segoe UI", 10, "bold"), 'relief': 'flat'}

        # === Variables initialisées ===
        self.poles_var = tk.StringVar(value="2")
        self.slots_var = tk.StringVar(value="9")
        self.layers_var = tk.StringVar(value="2")  # Valeur par défaut fixée
        self.vrillage_encoche_var = tk.StringVar(value="0")  # Valeur par défaut fixée
        self.coil_span_var = tk.StringVar()

        # === Widgets ===

        # Pôles
        tk.Label(master, text="Nombre de pôles (pair)", **label_opts).grid(row=0, column=0, sticky="w", padx=10, pady=5)
        poles_values = [str(i) for i in range(2, 31, 2)]
        self.poles_combo = ttk.Combobox(master, textvariable=self.poles_var, values=poles_values)
        self.poles_combo.grid(row=0, column=1, padx=10, pady=5)

        # Encoches
        tk.Label(master, text="Nombre d'encoches (multiple de 3)", **label_opts).grid(row=1, column=0, sticky="w", padx=10, pady=5)
        slots_values = [str(i) for i in range(3, 31, 3)]
        self.slots_combo = ttk.Combobox(master, textvariable=self.slots_var, values=slots_values)
        self.slots_combo.grid(row=1, column=1, padx=10, pady=5)

        # Couches (valeurs dynamiques)
        tk.Label(master, text="Nombre de couches", **label_opts).grid(row=2, column=0, sticky="w", padx=10, pady=5)
        self.layers_combo = ttk.Combobox(master, textvariable=self.layers_var)
        self.layers_combo.grid(row=2, column=1, padx=10, pady=5)

        # Pas de bobine
        tk.Label(master, text="Pas de bobine (en nombre d'encoches)", **label_opts, justify='left').grid(row=3, column=0, sticky="w", padx=10, pady=5)
        self.coil_span_combo = ttk.Combobox(master, textvariable=self.coil_span_var)
        self.coil_span_combo.grid(row=3, column=1, padx=10, pady=5)

        # # Vrillage_encoche
        # tk.Label(master, text="Vrillage (en nombre d'encoches)", **label_opts, justify='left').grid(row=4, column=0, sticky="w", padx=10, pady=5)
        # self.vrillage_encoche_combo = ttk.Combobox(master, textvariable=self.vrillage_encoche_var)
        # self.vrillage_encoche_combo.grid(row=4, column=1, padx=10, pady=5)


        # Options supplémentaires
        # Domaine elec
        tk.Label(master, text="Voir le domaine électrique ?", **label_opts).grid(row=5, column=0, sticky="w", padx=10, pady=5)
        self.electrical_var = ttk.Combobox(master, values=["Oui", "Non"])
        self.electrical_var.grid(row=5, column=1, padx=10, pady=5)
        self.electrical_var.current(1)

        # Têtes de bobines
        tk.Label(master, text="Afficher les têtes de bobines ?", **label_opts).grid(row=6, column=0, sticky="w", padx=10, pady=5)
        self.plot_end_turns_var = ttk.Combobox(master, values=["Oui", "Non"])

        self.plot_end_turns_var.grid(row=6, column=1, padx=10, pady=5)
        self.plot_end_turns_var.current(0)

        # Bouton principal
        self.plot_button = tk.Button(master, text="Calculer le bobinage", command=self.plot_winding, **button_opts)
        self.plot_button.grid(row=7, columnspan=2, pady=15, ipadx=10, ipady=5)

        # Zone de messages
        self.error_label = tk.Label(master, text="", fg="red", bg="white", font=("Segoe UI", 9, "italic"))
        self.error_label.grid(row=8, columnspan=2, pady=(0, 2))

        self.warning_label = tk.Label(master, text="", fg="orange", bg="white", font=("Segoe UI", 9, "italic"))
        self.warning_label.grid(row=9, columnspan=2, pady=(0, 2))

        self.result_label = tk.Label(master, text="", fg="black", bg="white", font=("Segoe UI", 9, "italic"))
        self.result_label.grid(row=10, columnspan=2, pady=(0, 10))

        # === Traces de mise à jour automatique ===
        self.poles_var.trace_add("write", self.update_dynamic_options)
        self.slots_var.trace_add("write", self.update_dynamic_options)
        self.layers_var.trace_add("write", self.update_dynamic_options)

        # === Appel initial de mise à jour ===
        self.update_dynamic_options()

    def update_dynamic_options(self, *args):
        if not hasattr(self, "error_label"):
            return  # On quitte si le widget n'est pas encore créé

        self.error_label.config(text="")
        self.warning_label.config(text="")
        self.result_label.config(text="")

        try:
            nb_poles = int(self.poles_var.get())
            nb_slot = int(self.slots_var.get())
            m = 3
        except ValueError:
            return

        # Met à jour la liste de pas de bobine


        # Met à jour la liste de couches
       
        try:
            if nb_slot == '':
                nb_slot = 9
                nb_poles = 2
            layers_list = layers_possibilities_list(nb_slot, nb_poles)
            self.layers_combo['values'] = [str(l) for l in layers_list]

            current_val = self.layers_var.get()

            if current_val == "" : # not in [str(l) for l in layers_list]:
                m = 3  # nombre de phases
                if nb_slot / (m * nb_poles) < 1:  # bobinage concentré
                    self.layers_var.set("2")
                elif nb_slot / (m * nb_poles) == int(nb_slot / (m * nb_poles)):  # pas entier
                    self.layers_var.set(str(layers_list[0]))
                else:  # pas fractionnaire
                    self.layers_var.set("2")
        except Exception as e:
            print("Erreur layers:", e)

        try:
            m = 3
            coil_span_list = coil_span_possibilities_list(int(self.layers_var.get() or 1), nb_slot, nb_poles)
            coil_span_list.reverse()
            self.coil_span_combo['values'] = [str(p) for p in coil_span_list]
            # self.coil_span_var.set(str(nb_slot//nb_poles) if (nb_slot//nb_poles) > 0 else ( if (nb_slot/(nb_poles*m)) < 1 else 2) )
            # if coil_span_list:
            # self.coil_span_var.set(str(coil_span_list[-1]))
            if nb_slot/(m*nb_poles) < 1 :# si bobinage concentré a pas fractionnaire
                self.coil_span_var.set(str(1))
            elif nb_slot/(m*nb_poles) >= 1 :# si bobinage distribué a pas fractionnaire 
                self.coil_span_var.set(str(nb_slot//nb_poles) if (nb_slot//nb_poles) > 0 else 1 )
            else :
                self.coil_span_var.set(str(coil_span_list[-1]))
        except Exception:
            pass


    def plot_winding(self):
        try:
            # Réinitialiser les messages
            self.error_label.config(text="")
            self.warning_label.config(text="")
            self.result_label.config(text="")

            poles = int(self.poles_var.get())
            slots = int(self.slots_var.get())
            layers = int(self.layers_var.get())
            raccourcissement = int(self.coil_span_var.get())
            # vrillage = float(self.vrillage_encoche_var.get())
            vrillage = 0
            # print( "vrillage_encoche : " + str(vrillage_encoche))

            electrical = 1 if self.electrical_var.get() == "Oui" else 0
            m = 3
            plot_end_turns = True if self.plot_end_turns_var.get() == "Oui" else False

            # Vérifications avec messages explicites

            if poles % 2 != 0:
                raise ValueError("❌ Le nombre de pôles doit être pair.")
            if slots % 3 != 0:
                raise ValueError("❌ Le nombre d'encoches doit être un multiple de 3.")
            if layers < 1 or layers > 30:
                raise ValueError("❌ Le nombre de couches doit être compris entre 1 et 30.")
            if layers == 1 and ( slots % 2 == 1 or raccourcissement % 2 == 0): # Condition vennant de la doc de motorcad, à vérifier
                raise ValueError("❌ Bobinage à une couche non faisable.")
            if (layers * slots / 2) != int(layers * slots / 2):
                raise ValueError("❌ Les trois phases ont un nombre déséquilibré de conducteurs.")
            if (slots / (m * math.gcd(slots, int(poles / 2)))) != int(slots / (m * math.gcd(slots, int(poles / 2)))):
                raise ValueError("❌ Bobinage non équilibré (slots / (m * pgcd) n'est pas entier).")



            # --- Appel au modèle de bobinage
            result = show_winding(
                m=3,
                see_electrical_domain=electrical,
                nb_poles=poles,
                nb_slots=slots,
                nb_layers=layers,
                raccourcissement=raccourcissement,
                vrillage_encoche = vrillage,
                plot_end_turns=plot_end_turns,
                )
            if result.get("warning_flag"):
                raise ValueError("❌ Il n'est pas possible de bobiner la machine entièrement de manière équilibré.")

            # --- Traitement des résultats retournés
            if result.get("has_no_symmetry", False):
                self.warning_label.config(
                    text="⚠️ Attention : Absence de symétrie, ce qui peut engendrer de fortes vibrations.")

            if result.get("is_unbalanced", False):
                self.error_label.config(
                    text="❌ Les trois phases ont un nombre déséquilibré de conducteurs.")
                return  # bloquer affichage des résultats

            # Résumé des résultats en noir
            info_text = (
                f"Facteur de bobinage : {result['kw']:.3f}\n"
                f"Fréquence des ondulations de couple : {result['torque_ripple_freq']:.1f} par tour\n"
                f"Sections identiques : {result['identical_sections']}\n"
                f"Type de bobinage : {result['winding_type']}"
            )
            self.result_label.config(text=info_text)

        except Exception as e:
            self.error_label.config(text=str(e))



# if __name__ == "__main__":
#     root = tk.Tk()
#     app = WindingApp(root)
#     root.mainloop()


# export_table = False 

# if export_table == True:

#     results = []
#     raccourcissement_max = 7
#     nb_slots_max = 109
#     nb_poles_max = 75
#     fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})

#     for nb_layers in [1, 2]:  # Nombre de couches
#         for nb_slots in range(3, nb_slots_max, 3):  # Slots (multiples de 3)
#             raccourcissement_max = max(int(nb_slots// 2+1) ,2)
#             for raccourcissement in range(1, raccourcissement_max):  # Pas de bobine
#                 for nb_poles in range(2, nb_poles_max, 2):  # Pôles pairs
#                     try:
#                         # Calcul du type de bobinage
#                         f_torque, sections, winding_type, warning = calculate_winding_characteristics(
#                             3, nb_slots, nb_poles, nb_layers, raccourcissement,silent=True
#                         )

#                         # Distribution des conducteurs
#                         #         star_of_slots(winding_type, m, nb_poles, nb_slots, nb_layers, fig2, ax2, electrical=True,raccourcissement=raccourcissement)

#                         phasors, Conductors_distribution, warning_flag = star_of_slots(
#                             winding_type, 3, nb_poles, nb_slots, nb_layers,
#                             fig=None, ax=None, plot_fig = False,
#                             raccourcissement=raccourcissement,
#                             plot_end_turns=False, silent=True
#                         )

#                         # Calcul du kw 
#                         kw = calculer_facteur_de_bobinage(phasors, Conductors_distribution, nb_slots, nb_poles, 3, silent=True)
#                         # print("KW : " + str(kw))
#                         # print(phasors)
#                         if kw >1 :
#                             kw = 0
#                         # print('kw : ')
#                         # print(kw)
#                         results.append({
#                             'Slots': nb_slots,
#                             'Poles': nb_poles,
#                             'Pas_de_bobine': raccourcissement,
#                             'Nb_couches': nb_layers,
#                             'kw': kw
#                         })

#                     except Exception as e:
#                         print('ERROR !! ' + str(e))
#                         results.append({
#                             'Slots': nb_slots,
#                             'Poles': nb_poles,
#                             'Pas_de_bobine': raccourcissement,
#                             'Nb_couches': nb_layers,
#                             'kw': np.nan
#                         })

#     # Création du DataFrame
#     df = pd.DataFrame(results)

#     # Export Excel
#     df.to_excel("facteurs_de_bobinage_complet.xlsx", index=False)
#     print("✅ Fichier généré : facteurs_de_bobinage_complet.xlsx")







st.title("Visualisation du bobinage d'une machine électrique")

# m = 3
# nb_poles = st.slider("Nombre de pôles", min_value=2, max_value=40, step=2, value=10)
# nb_slots = st.slider("Nombre d'encoches", min_value=3, max_value=60, step=3, value=12)
# nb_layers = st.selectbox("Nombre de couches", options=[1, 2], index=1)
# coil_span = st.selectbox("Pas de bobinage", options=[1, 2,3,4,5,6], index=1)
# plot_end_turns = st.selectbox("Tetes de bobines ?", options=[0, 1], index=1)


m = 3  # nombre de phases

# --- Choix du nombre de pôles et d'encoches ---
nb_poles = st.selectbox(
    "Nombre de pôles (pair)", 
    options=list(range(2, 41, 2)), 
    index=4
)
nb_slots = st.selectbox(
    "Nombre d'encoches (multiple de 3)", 
    options=list(range(3, 61, 3)), 
    index=3
)

# --- Calcul des options dynamiques ---
# Couches possibles
layers_list = layers_possibilities_list(nb_slots, nb_poles)
if layers_list:
    default_layers = 2 if nb_slots / (m * nb_poles) < 1 else layers_list[0]
else:
    default_layers = 2

nb_layers = st.selectbox(
    "Nombre de couches", 
    options=layers_list if layers_list else [1, 2],
    index=layers_list.index(default_layers) if default_layers in layers_list else 1
)

# Pas de bobine possible
coil_span_list = coil_span_possibilities_list(nb_layers, nb_slots, nb_poles)
coil_span_list = sorted(coil_span_list, reverse=True)

if nb_slots / (m * nb_poles) < 1:
    default_span = 1
else:
    default_span = max(1, nb_slots // nb_poles)

coil_span = st.selectbox(
    "Pas de bobinage", 
    options=coil_span_list if coil_span_list else list(range(1, 7)),
    index=coil_span_list.index(default_span) if default_span in coil_span_list else 0
)

# Têtes de bobines
plot_end_turns = st.selectbox(
    "Têtes de bobines ?", 
    options=[0, 1],
    index=1
)


f_torque, nb_of_identic_sections,winding_type,warning_flag = calculate_winding_characteristics(m, nb_slots, nb_poles, nb_layers, coil_span, silent = False)
     




# fig1, ax1 = plt.subplots(subplot_kw={'projection': 'polar'})
# ax1.set_theta_zero_location('N')
# ax1.set_yticklabels([])
# ax1.set_xticklabels([])
# ax1.grid(False)

dark_bg = "#1e1e1e"  # gris très foncé

fig1, ax1 = plt.subplots(subplot_kw={'projection': 'polar'}, facecolor=dark_bg)
ax1.set_facecolor(dark_bg)
ax1.set_theta_zero_location('N')
ax1.set_yticklabels([])
ax1.set_xticklabels([])
ax1.grid(False)

# Couleur des ticks et du contour pour qu'on voie bien
ax1.tick_params(colors='white')
ax1.spines['polar'].set_color('white')


#star_of_slots(m, nb_poles, nb_slots, nb_layers, fig1, ax1, "Domaine mécanique")
phasors,Conductors_distribution,warning_flag = star_of_slots( winding_type, m, nb_poles, nb_slots, nb_layers, fig1, ax1, electrical=False,legend=True,raccourcissement=coil_span,plot_fig = True,plot_end_turns=plot_end_turns,silent = False,export_motorcad_tables=False)

kw = calculer_facteur_de_bobinage(phasors,Conductors_distribution,nb_slots,nb_poles,m,silent = True)

st.write(f"Winding Factor : {kw:.3f}")
st.write(f"Nombre de sections identiques : {nb_of_identic_sections}")
st.write(f"Fréquence d'ondulation du couple : {f_torque}")

draw_magnets(nb_poles, fig1, ax1)
draw_stator(ax1, nb_slots)

st.pyplot(fig1)
