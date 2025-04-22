import streamlit as st
import matplotlib.pyplot as plt


def angle_in_sector(angle, center, width):
    angle = round(angle % (2 * np.pi),6)   # modulo 2 pi
    center = center % (2 * np.pi) # modulo 2 pi
    half_width = width / 2
    lower = round((center - half_width) % (2 * np.pi),6)
    upper = round((center + half_width) % (2 * np.pi),6)
    # print('lower < upper ' + str(lower < upper))
    # if abs(lower-angle)<0.001:
    #     print('caution with phase lower')
    #     print(lower*180/np.pi)
    #     print(angle*180/np.pi)
    #     print('lower < angle and angle <= upper ' + str(lower < angle and angle <= upper))
    # if abs(upper-angle)<0.001:
    #     print('caution with phase upper')
    #     print(upper*180/np.pi)
    #     print(angle*180/np.pi)

    if lower < upper:
        return lower < angle and angle <= upper
    else:
        return angle > lower or angle <= upper


def star_of_slots(m, nb_poles, nb_slots, nb_layers, fig, ax, title, electrical=False,legend=False):
    poles_pair = nb_poles / 2
    base_angles = np.linspace(0, 2 * np.pi, nb_slots, endpoint=False)
    # phase_labels = ['U', 'V', 'W', 'X', 'Y', 'Z']
    phase_labels = ['A', 'B', 'C', 'D', 'E', 'F']
    phase_colors = ['green', 'orange', 'purple', 'cyan', 'magenta', 'brown']
    sector_width = np.pi / m

    if electrical:
        angles = base_angles * poles_pair
    else:
        angles = base_angles



    if electrical:     # Draw phase sectors if in electrical domain - Only for visualization
        ax.set_theta_zero_location('N')
        for k in range(m):
            center_pos = (2 * np.pi * k / m          + 6* np.pi / m /4 ) # décallage de 1/2
            center_neg = (2 * np.pi * k / m + np.pi + 6* np.pi / m /4  )  # décallage de 1/2
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


    for idx, angle in enumerate(angles): # On itère sur les dents (slots)
        test_angle = base_angles[idx] * poles_pair  # Always use electrical angle to determine phase
        phase_label = ''
        phase_idx = None
        polarity = None



        for k in range(m): # on itère sur les phases
            center_pos = (2 * np.pi * k / m         ) # - np.pi / m /4 )   # décallage de 1/2
            center_neg = (2 * np.pi * k / m + np.pi ) # - np.pi / m /4  )  # décallage de 1/2

            if angle_in_sector(test_angle, center_pos, sector_width):
                phase_label = phase_labels[k]
                phase_idx = k
                polarity = '+'
                # print("angle "+str(angle*180/np.pi)+" appartient a la phase  "+str(k)+" polarity +")
                break
            elif angle_in_sector(test_angle, center_neg, sector_width):
                phase_label = phase_labels[k]
                phase_idx = k
                polarity = '–'
                # print("angle "+str(angle*180/np.pi)+" appartient a la phase  "+str(k)+" polarity -")
                break
            # Sinon il n'appartient pas à cette phase n°k, et on passe a la phase suivante

        # Use phase color
        color = phase_colors[phase_idx % len(phase_colors)] if phase_idx is not None else 'gray'


        # Plot each layer
        if nb_layers == 2 or  (nb_layers == 1 and idx % 2 == 0 ) : # Si il y a qu'une layer, il faut bobiner une dent sur deux, à améliorer pour prendre en compte n layers # TO DO
            radius = 1 #+ nb_layers * 0.1
            if electrical:
                ax.plot([0, angle], [0, radius], marker='o', color=color) # plot phasors only for electrical
                # Electrical domain: simpler single label
                label_radius = 1.3 + (idx * 0.03)
                ax.text(angle, label_radius, f"{idx + 1}\n{phase_label}{polarity}", fontsize=8, ha='center', va='center',color=color,rotation=np.degrees(angle), rotation_mode='anchor')
            else:
                # Label only once per slot — for mechanical domain, do dual-side labeling
                label_radius = 1 + 0.15
                angle_deg = np.degrees(angle)
                # Rotate left/right label slightly off-axis
                delta = 0.025 + 0.13*10/nb_slots

                if polarity == '+':
                    label_right = f"{phase_label}+"
                    label_left = f"{phase_label}–"
                elif polarity == '–':
                    label_right = f"{phase_label}-"
                    label_left = f"{phase_label}+"
                else:
                    label_right = label_left = ""
                    print('error : no polarity')

                # Right side (positive direction)
                ax.text(angle + delta, label_radius, label_right,
                        fontsize=8, color=color, ha='center', va='center',
                        rotation=angle_deg, rotation_mode='anchor')

                # Left side (opposite direction)
                ax.text(angle - delta, label_radius, label_left,
                        fontsize=8, color=color, ha='center', va='center',
                        rotation=angle_deg, rotation_mode='anchor')



    ax.set_title(title)


    if legend == True:
        # Legend for phases
        legend_elements = [
        Patch(facecolor=phase_colors[i], edgecolor='black', label=f'Phase {phase_labels[i]}') for i in range(m)]
        ax.legend(handles=legend_elements, loc='upper left')


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



def show_winding(m=3, see_electrical_domain=1, nb_poles = 14, nb_slots = 12, nb_layers = 2):

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
    star_of_slots(m, nb_poles, nb_slots, nb_layers, fig1, ax1, f"Mechanical domain for a machine with {nb_slots} slots and {nb_poles} poles")
    draw_magnets(nb_poles, fig1, ax1)
    draw_stator(ax1, nb_slots)

    if see_electrical_domain ==1:
        # Electrical domain
        fig2, ax2 = plt.subplots(subplot_kw={'projection': 'polar'})
        ax2.set_theta_zero_location('N')
        ax2.set_yticklabels([])
        ax2.set_xticklabels([])
        ax2.grid(False)
        star_of_slots(m, nb_poles, nb_slots, nb_layers, fig2, ax2, f"Electrical domain for a machine with {nb_slots} slots and {nb_poles} poles", electrical=True)
        #draw_rotor(ax, nb_poles, radius_core=1.0, radius_magnet_base=1.5, tooth_width=0.1)

    plt.show()


def calculate_winding_characteristics(m,Ns,p,nb_layers):
    q = Ns / p / m # Nombre d'encoches par pôle et par phase (q) il est préférable d'avoir q ∈ [ 0.25 ; 0.5 ], car en dehors de cet intervalle il y a plusieurs pôles qui interragissement avec une seule dent, ou plusieurs dents qui interragissent avec le même pôle, ce qui n'est pas optimal. Il ne faudrait pas avoir q = 1/3, car cela ne permet pas pas d'avoir un système équilibré
    pole_pairs = p/2
    z = Ns*1/(3-(nb_layers))/(math.gcd(Ns,p*m))
    harmonic_nb = 1
    sigma = 2*np.pi/2/m
    kmn = math.sin(0.5 * harmonic_nb * sigma) / ( z * math.sin( harmonic_nb * sigma / (2*z) ) )
    gamma_s = np.pi/(q * m)
    epsilon = np.pi - gamma_s # chroding or coil-span angle
    ken = np.cos(0.5*harmonic_nb*epsilon)
    kw = ken * kmn # winding_factor
    f_torque = ppcm(p,Ns) # Frequence des ondulations de couple (lorsque le moteur n'est pas alimenté)
    nb_of_identic_sections = math.gcd(Ns,p)
    S = (Ns/(m*math.gcd(Ns,int(p/2)))) # Indicator of unbalanced winding
    S = S - int(S)
    warning_flag = False
    if kw<0.85:
        print("Warning, the winding factor is low")
        warning_flag = True
    if q < 0.25:
        print("Warning, there are multiple north and south magnet poles interacting with each stator tooth, which is not optimal")
        warning_flag = True
    if q > 0.5:
        print("Warning, a single rotor pole will span over multiple teeth, which is not optimal")
        warning_flag = True
    if nb_of_identic_sections < 2:
        print("Warning, there is no symmetry, which can result in high level of vibrations")
        warning_flag = True
    if S > 0:
        print("Warning, the winding is unbalanced")
        warning_flag = True
    return kw, f_torque, nb_of_identic_sections,warning_flag

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
    while ((nb_layers != 1) and  (nb_layers != 2))  :     # Verification

        nb_layers = int(input("Enter the number of layers: "))
        if ((nb_layers != 1) and  (nb_layers != 2)) :
            print("Error : the number of layers should be 1 or 2")
    return nb_poles, nb_slots, nb_layers


def ppcm(a,b): # plus petit multiple commun
    return a*b/math.gcd(a,b)




st.title("Visualisation du bobinage d'une machine électrique")

m = 3
nb_poles = st.slider("Nombre de pôles", min_value=2, max_value=40, step=2, value=10)
nb_slots = st.slider("Nombre d'encoches", min_value=3, max_value=60, step=3, value=12)
nb_layers = st.selectbox("Nombre de couches", options=[1, 2], index=1)

kw, f_torque, sections, warning_flag = calculate_winding_characteristics(m, nb_slots, nb_poles, nb_layers)

st.write(f"Winding Factor : {kw:.3f}")
st.write(f"Nombre de sections identiques : {sections}")
st.write(f"Fréquence d'ondulation du couple : {f_torque}")

fig1, ax1 = plt.subplots(subplot_kw={'projection': 'polar'})
ax1.set_theta_zero_location('N')
ax1.set_yticklabels([])
ax1.set_xticklabels([])
ax1.grid(False)

star_of_slots(m, nb_poles, nb_slots, nb_layers, fig1, ax1, "Domaine mécanique")
draw_magnets(nb_poles, fig1, ax1)
draw_stator(ax1, nb_slots)

st.pyplot(fig1)
