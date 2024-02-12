## 1. Explain how an electron beam can be made to bend either towards or away from the normal to an equipotential surface.
### Ans: **Bending Towards the Normal:**

**Non-Uniform Electric Field:**

-   Imagine an electron beam moving through a space where the electric field **strength varies**. This creates a **non-uniform** field, like the one depicted in the image below:

-   As the electron encounters this region, it experiences a force not entirely perpendicular to the equipotential surface (shown as dashed lines).
-   This **force component parallel to the surface** causes the electron to deviate from its initial path and **bend towards the region of higher potential** (represented by the denser equipotential lines).

**Electrostatic Lenses:**
-   Specially designed structures, like the one shown below, use electric fields to manipulate electron beams:

-   By shaping these lenses (electrodes), we can create non-uniform fields that **focus or defocus** the beam, altering its direction and convergence.

**Bending Away from the Normal:**
**Retarding Potential:**
-   If the electron beam enters a region with a **higher potential** than its initial energy, it experiences a **retarding force**.
-   This force, again not perfectly perpendicular to the equipotential surface, pushes the electron **away** from the region of higher potential (positive charges), bending its path accordingly.
-   Imagine an electron beam approaching a positively charged plate, as illustrated here:

**Apertures with Fringing Fields:**
-   When an electron beam passes through an opening, the electric field at the edges "fringes" outwards.
-   This fringing field can have a component that pushes the electron away from the aperture, causing it to deviate from its straight path.
-   Picture an electron beam passing through a small hole, with the edges influencing its trajectory:

**Remember:**
-   Electrons are negatively charged, attracted to positive charges (higher potential), and repelled by negative charges (lower potential).
-   By strategically manipulating the electric field around the beam, we can control its direction and bending behavior.

**Key Concepts:**
-   Equipotential surfaces: Surfaces of constant electric potential.
-   Electric field: Force experienced by a charged particle due to the presence of other charges.
-   Gradient of potential: Direction and magnitude of change in potential.
-   Electrostatic lenses: Systems using electric fields to manipulate charged particle beams.

## 2. Show that velocity acquired by an electron in a uniform electrostatic field varies as square root of potential difference through which it is accelerated.
### Ans: **1. Work-Energy Principle:**

-   The electron gains kinetic energy as it moves through the potential difference (voltage).
-   Work done by the electric field on the electron equals the change in its kinetic energy.
-   Work = Potential difference (V) * Charge of the electron (e)

**2. Kinetic Energy and Velocity:**

-   The kinetic energy of the electron is related to its mass (m) and velocity (v) by:
-   Kinetic Energy = 1/2 * mass * velocity^2

**3. Combining Equations:**

-   Substitute the work expression and kinetic energy expression into the work-energy principle:
-   V * e = 1/2 * m * v^2

**4. Solving for Velocity:**

-   Rearrange the equation to isolate velocity:
-   v^2 = 2 * (V * e) / m
-   Take the square root of both sides:
-   v = √(2 * (V * e) / m)

**5. Simplifying:**

-   The electron charge (e) and mass (m) are fundamental constants.
-   Therefore, the velocity (v) depends only on the square root of the potential difference (V):
-   v ∝ √V

**Conclusion:**

The velocity acquired by an electron in a uniform electrostatic field **varies directly with the square root of the potential difference** through which it's accelerated. This relationship is derived from the work-energy principle and the relationship between kinetic energy and velocity.

**Additional Notes:**

-   This assumes the electron starts from rest.
-   The direction of the velocity depends on the polarity of the voltage.
-   This relationship holds true for any charged particle in a uniform electric field, not just electrons.

## 3. List any four applications of CRO. Illustrate any one of them.
###  Ans: **1. Signal Visualization and Analysis:**

-   CROs excel at displaying and analyzing waveforms of various electrical signals, such as sine waves, square waves, and pulses. This is crucial in various fields like electronics, telecommunications, and physics for:
    
    -   Troubleshooting circuit malfunctions by observing signal distortions or unexpected behavior.
    -   Measuring signal characteristics like amplitude, frequency, and phase.
    -   Analyzing signal integrity and noise levels.
    -   Verifying the functionality of designed circuits.

**2. Biomedical Applications:**

-   CROs play a vital role in medical equipment for:
    
    -   Displaying electrocardiograms (ECGs) to monitor heart activity.
    -   Visualizing electroencephalograms (EEGs) to study brain activity.
    -   Analyzing electromyograms (EMGs) to assess muscle function.
    
**3. Audio Signal Analysis:**

-   In audio systems, CROs help:
    
    -   Visualize audio waveforms to identify distortions or clipping.
    -   Measure audio signal characteristics like frequency response and harmonic content.
    -   Analyze sound quality and troubleshoot audio equipment issues.
    
**4. Educational and Research Applications:**

-   CROs are valuable tools for:
    -   Demonstrating electrical concepts and principles in science and engineering education.
    -   Conducting research in various fields like physics, materials science, and electrical engineering.
    -   Visualizing and analyzing experimental data obtained from various sensors and instruments.

## 4. Define Deflection sensitivity. Derive an expression for deflection sensitivity.
### Ans: **Deflection Sensitivity**

Deflection sensitivity is a measure of how much a spot on the screen of a cathode ray oscilloscope (CRO) deflects for a given change in voltage applied to the deflection plates. It is usually expressed in units of millimeters per volt (mm/V).

**Deriving an expression for deflection sensitivity**

The deflection of the electron beam in a CRO is caused by the force exerted by the electric field between the deflection plates. The magnitude of this force is given by:
```
F = E * q

```
where:
-   F is the force (N)
-   E is the electric field strength (V/m)
-   q is the charge of the electron (C)

The electric field strength between the deflection plates is proportional to the voltage applied to the plates:
```
E = V / d

```
where:

-   V is the voltage applied to the plates (V)
-   d is the distance between the plates (m)

Substituting this expression for E into the first equation, we get:
```
F = (V / d) * q

```
The acceleration of the electron beam is then:
```
a = F / m

```
where:
-   m is the mass of the electron (kg)

The deflection of the electron beam on the screen is proportional to the acceleration and the square of the time the electron spends between the plates:

```
y = 1/2 * a * t^2

```
where:
-   y is the deflection of the electron beam on the screen (m)
-   t is the time the electron spends between the plates (s)

The time the electron spends between the plates is related to the length of the deflection plates (L) and the velocity of the electron (v):
```
t = L / v
```
Substituting this expression for t into the previous equation, we get:
```
y = 1/2 * a * (L / v)^2

```
The velocity of the electron beam is related to the accelerating voltage (Va) applied to the electron gun:

```
v = sqrt(2 * Va * e / m)

```
where:

-   e is the charge of the electron (C)

Substituting this expression for v into the previous equation, we get:
```
y = 1/2 * a * (L^2 / (2 * Va * e / m))^2

```
Simplifying this expression, we get:

```
y = (L^2 * m) / (4 * Va * e * d)

```
Since the deflection sensitivity is defined as the deflection per unit voltage, we can divide both sides by V to get:

```
Deflection sensitivity = y / V = (L^2 * m) / (4 * Va * e * d^2)

```
This is the expression for the deflection sensitivity of a CRO.

In conclusion, the deflection sensitivity of a CRO is determined by the length of the deflection plates, the mass of the electron, the accelerating voltage, the charge of the electron, and the distance between the deflection plates.

**Additional notes:**

-   This derivation assumes that the initial velocity of the electron beam is negligible.
-   The deflection sensitivity of a CRO is not perfectly linear, especially at high deflection voltages.
-   The actual deflection sensitivity of a CRO can be slightly different from the theoretical value due to factors such as manufacturing tolerances and the presence of stray electric and magnetic fields.

## 5. What is an electron lens? Compare between electron lens and optical lens. 
### Ans:  An electron lens is a device that focuses or manipulates an electron beam, similar to how an optical lens focuses light. While light lenses rely on refracting or reflecting light waves, electron lenses use electric and/or magnetic fields to control the behavior of charged electrons.

There are two main types of electron lenses:

**1. Electrostatic Lenses:**

-   These use electric fields created by charged conductors or apertures to focus or defocus the beam.
-   By shaping the electrodes, we can create non-uniform electric fields that attract or repel electrons, bending their trajectories and achieving desired focusing or defocusing effects.
-   Electrostatic lenses offer low-cost and relatively lightweight implementations but struggle with strong focusing power compared to magnetic lenses.

**2. Magnetic Lenses:**

-   These utilize magnetic fields generated by electromagnets to manipulate the electron beam.
-   The magnetic field exerts a force on the moving electrons, causing them to bend their path and converge or diverge according to the field configuration.
-   Magnetic lenses offer significantly stronger focusing power and are the preferred choice for high-resolution applications, but they are generally more complex and expensive.

**Applications of Electron Lenses:**

-   **Electron Microscopes:** Both electric and magnetic lenses are crucial components in electron microscopes, focusing the beam onto the sample and achieving ultra-high magnifications that enable detailed observation of structures down to the atomic level.
-   **Electron Beam Lithography:** In this technique, electron lenses precisely sculpt patterns on surfaces by directing a focused beam, enabling intricate microfabrication processes for chipmaking and other applications.
-   **Particle Accelerators:** Some sections of particle accelerators use magnetic lenses to guide and steer beams of charged particles along their trajectory.

**Understanding Electron Lenses:**

The ability to focus and manipulate electron beams using lenses opens up a vast range of scientific and technological possibilities. By understanding the principles behind electric and magnetic fields, we can design and control electron lenses for various applications, advancing areas like microscopy, nanotechnology, and particle physics.

### Electron vs. Optical Lens: 10 Key Differences 
1.  **Rays:** Electrons vs. Photons (light)
2.  **Material:** Electromagnetic fields vs. Glass/plastic
3.  **Focusing:** Electromagnetic manipulation vs. Refraction/diffraction
4.  **Wavelength:** Ultra-short (atomic) vs. Visible light spectrum
5.  **Magnification:** Millions of times vs. Up to 2000 times
6.  **Resolution:** Atomic level vs. Limited to 0.2 µm
7.  **Complexity:** Highly complex, expensive vs. Simple, affordable
8.  **Environment:** Vacuum required vs. Works in air
9.  **Applications:** Microstructures, atoms, viruses vs. Cells, tissues, organisms
10.  **Live Imaging:** Limited vs. Possible for certain cells

## 6. State Bethe’s law. Compare between Bethe’s law & Snell’s law.
### Ans:- ##   
Bethe's Law vs. Snell's Law

Both Bethe's law and Snell's law deal with the bending of waves or particles when they encounter an interface between two media, but they apply to different types of phenomena and use different underlying principles.

**Bethe's Law:**

-   **Applies to:** Charged particles (electrons, positrons, etc.)
-   **Principle:** Bending due to interaction with the electrostatic potential of the medium.
-   **Formula:**  `sin θ₁ / sin θ₂ = √(p₁/p₂) * √((V₂ - V₁)/T)` where:
    
    -   θ₁ and θ₂ are the angles of incidence and refraction, respectively.
    -   p₁ and p₂ are the momenta of the particle before and after refraction.
    -   V₁ and V₂ are the electrostatic potentials of the two media.
    -   T is the kinetic energy of the particle.
    
-   **Bending direction:** Towards the region of higher potential for positively charged particles, away for negatively charged.

**Snell's Law:**

-   **Applies to:** Waves (light, sound, etc.)
-   **Principle:** Bending due to change in wave speed depending on the refractive index of the medium.
-   **Formula:**  `n₁ * sin θ₁ = n₂ * sin θ₂` where:
    
    -   n₁ and n₂ are the refractive indices of the two media.
    -   θ₁ and θ₂ are the angles of incidence and refraction, respectively.
    
-   **Bending direction:** Towards the denser medium for light.

**Key Differences:**

-   Bethe's law deals with charged particles interacting with electrostatic fields, while Snell's law deals with waves encountering changes in refractive index.
-   Bethe's law's formula is more complex and involves several parameters, while Snell's law has a simpler form.
-   The direction of bending in Bethe's law depends on the particle's charge and potential, while in Snell's law, it's always towards the denser medium for light.
## 7.  Draw block diagram of Cathode Ray Oscilloscope. Mention different parts of CRO.
### Ans:- 
![Image of](https://www.geeksforgeeks.org/cathode-ray-oscilloscope/Block-Diagram-of-Cathode-Ray-Oscilloscope-(CRO) 
)
## 8. Prove that electron follows a parabolic path when it enters in a transverse uniform electric field.
### Ans:- ## Proof of electron's parabolic path in a transverse electric field

When an electron enters a transverse uniform electric field, it experiences a constant force perpendicular to its initial velocity. This force causes the electron to accelerate in the direction of the force, leading to a **parabolic trajectory**. Here's the proof:

**1. Setting the scene:**

-   Assume the electron enters the field with initial velocity **v0** in the x-direction (parallel to the plane of the field).
-   The electric field **E** acts perpendicular to the electron's motion (y-direction).
-   The electron's mass is **m** and its charge is **-e**.

**2. Calculating the acceleration:**

-   The force **F** experienced by the electron is given by:  **F = -e * E** (negative sign due to negative charge)
-   This force causes an acceleration **a** in the y-direction:  **a = F / m = -e * E / m**

**3. Describing the motion:**

-   The electron's motion can be separated into two independent components:
    
    -   **x-direction:** Constant velocity **v0** due to no force in this direction.
    -   **y-direction:** Accelerated motion under the influence of the electric field.
    

**4. Analyzing the y-direction motion:**

-   We can use the kinematic equation for constant acceleration:
    
    -   **y = v0y * t + 1/2 * a * t^2**
    -   Since the initial y-velocity (v0y) is 0 (transverse field), it simplifies to:
    -   **y = 1/2 * a * t^2**
    

**5. Substituting acceleration:**

-   Substitute the expression for acceleration (a) from step 2:
    
    -   **y = 1/2 * (-e * E / m) * t^2**
    

**6. Simplifying and recognizing the parabola:**

-   Rearrange the equation:
    
    -   **y = (-e * E) / (2 * m) * t^2**
    -   Notice the square term (t^2) in the equation, which is the defining characteristic of a parabola.
    

Therefore,  **y is proportional to t^2**, confirming that the electron follows a parabolic path in the y-direction under the influence of the transverse electric field.

**Additional notes:**

-   This proof assumes the initial velocity in the x-direction remains constant and the electric field is perfectly uniform.
-   In reality, the electric field strength might vary, slightly modifying the parabolic shape.
-   This phenomenon has practical applications in electron microscopes and particle accelerators, where manipulating electron beams with electric fields is crucial for imaging and accelerating particles.

## 9. An electron moves in circular path perpendicular to uniform magnetic field with magnitude of 5 mT. Find the radius of circular path and time interval for one revolution if speed of electron is 2*107 m/s.
### Ans:- **Given:**

-   Magnetic field strength (B) = 5 mT = 5 * 10^-3 T
-   Electron velocity (v) = 2 * 10^7 m/s
-   Electron charge (e) = 1.6 * 10^-19 C
-   Electron mass (m) = 9.11 * 10^-31 kg

**1. Finding the radius (r):**

In a circular path with a constant magnetic field, the centripetal force acting on the electron is balanced by the magnetic force. We can use the following equation:

```
mv^2/r = e * v * B

```

where:

-   m is the mass of the electron
-   v is the velocity of the electron
-   r is the radius of the circular path
-   e is the charge of the electron
-   B is the magnetic field strength

Simplifying and solving for r:

```
r = mv / (e * B)
r = (9.11 * 10^-31 kg * 2 * 10^7 m/s) / (1.6 * 10^-19 C * 5 * 10^-3 T)
r ≈ 0.0384 m

```

Therefore, the radius of the circular path is approximately 0.0384 meters.

**2. Finding the time interval for one revolution (T):**

The time it takes for the electron to complete one revolution is equal to the circumference of the circle divided by its velocity:

```
T = 2 * pi * r / v
T = 2 * pi * 0.0384 m / (2 * 10^7 m/s)
T ≈ 3.82 * 10^-8 s

```

Therefore, the time interval for one revolution is approximately 3.82 x 10^-8 seconds.

**In conclusion:**

-   The radius of the circular path is approximately 0.0384 meters.
-   The time interval for one revolution is approximately 3.82 x 10^-8 seconds.

## 10. Compare between electron microscope and optical microscope.
### Ans:- 1.  **Illumination Source:**
    
    -   **Electron Microscope:**  Uses an electron beam instead of visible light.
    -   **Optical Microscope:**  Uses visible light or ultraviolet light.
2.  **Resolution:**
    
    -   **Electron Microscope:**  Significantly higher resolution, able to image individual atoms (nano to pico scale).
    -   **Optical Microscope:**  Limited resolution due to wavelength of light, can only observe objects down to about 0.2 micrometers.
3.  **Magnification:**
    
    -   **Electron Microscope:**  Much higher magnification, reaching millions of times.
    -   **Optical Microscope:**  Typically limited to around 2000x magnification.
4.  **Sample Preparation:**
    
    -   **Electron Microscope:**  Often requires complex sample preparation, including fixing, dehydrating, and coating with conductive material.
    -   **Optical Microscope:**  Simpler sample preparation, often requiring minimal processing.
5.  **Cost:**
    
    -   **Electron Microscope:**  Significantly more expensive due to complex technology.
    -   **Optical Microscope:**  Relatively inexpensive and readily available.
6.  **Applications:**
    
    -   **Electron Microscope:**  Used in research involving nanoscale structures, cell biology, material science, etc.
    -   **Optical Microscope:**  Used in education, biology, medicine, and various other fields.
7.  **Depth of Field:**
    
    -   **Electron Microscope:**  Larger depth of field, allowing observation of 3D features.
    -   **Optical Microscope:**  Limited depth of field, requiring frequent refocusing for different depths.
8.  **Live Samples:**
    
    -   **Electron Microscope:**  Cannot observe live samples due to high vacuum environment.
    -   **Optical Microscope:**  Can observe live samples with appropriate techniques.
9.  **Imaging Mode:**
    
    -   **Electron Microscope:**  Offers various imaging modes like transmission and scanning electron microscopy.
    -   **Optical Microscope:**  Primarily operates in brightfield and darkfield modes.
10.  **Ease of Use:**
     -   **Electron Microscope:**  Requires specialized training and expertise to operate and interpret images.
     -    **Optical Microscope:**  Relatively easier to use, good for basic observations and educational purposes.

## 11. Electron accelerated by a potential of 250 V enter the electric field at an angle of incidence 45o and get reflected through an angle of 30o . Find the potential difference between two regions.
### Ans:- 
1.  **Energy conversion:** Initial kinetic energy (K1) is converted to electrical potential energy (U2) upon reflection.
 2.  **Initial conditions:**
   -   mv1^2/2 = K1 = initial kinetic energy (given)
    -   qV = U1 = initial electrical potential energy
    -   v1 = sqrt(2) * v (assuming equal x and y components for initial velocity)
    
3.  **Distance traveled:**
    
    -   d = 2 * v1^2 * t^2 / 4a
    -   a = qE / m (acceleration due to electric field)
    -   v1^2 = 2v^2 (using v1/v relationship from step 2)
    -   Substitute and simplify to d = 4qEv^2 / mv^2
    
4.  **Final velocity:**
    
    -   v2 = sqrt(2) * v (similarly as for v1)
    
5.  **Final potential energy:**
    
    -   U2 = qV
    
6.  **Equating Energies:**
    
    -   K1 = U2
    -   mv1^2/2 = qV
    -   Substitute v1^2 and simplify to V = -4mv^2 / (2q)
    
7.  **Finding the potential difference:**
    
    -   Substitute all known values (m, q, and v)
    -   Calculate V ≈ -1.42 x 10^11 volts
    

**Answer:** The potential difference between the two regions is approximately **-1.42 x 10^11 volts**. The negative sign indicates the direction of the potential difference.

## 12. Explain the concept of thin film interference.
### Ans:- **Thin film interference** is a phenomenon where light interacting with a thin layer of material (like a soap bubble or oil film) produces colorful patterns or intensity changes due to the superposition of reflected and transmitted light waves.

**Key concepts:**

-   **Multiple reflections and transmissions:** When light reaches the thin film, part is reflected from the top surface and part is transmitted through. The transmitted light then bounces off the bottom surface, creating two reflected beams (one from each interface) and two transmitted beams.
-   **Path length difference:** The reflected beams travel different distances due to the film's thickness. This path length difference affects their phase relationship when they recombine.
-   **Constructive and destructive interference:** When the recombined waves are in phase (crest coinciding with crest), they constructively interfere,  **increasing reflected intensity** and appearing brighter. Conversely, when out of phase (crest coinciding with trough), they destructively interfere,  **decreasing reflected intensity** and appearing darker.
-   **Dependence on thickness and wavelength:** The path length difference depends on the film thickness and the wavelength of light. Changing either alters the interference pattern, leading to different colors being reflected or transmitted (as different colors have different wavelengths).

**Factors influencing interference:**

-   **Film thickness:** Thickness changes the path length difference, shifting the interference pattern's colors.
-   **Refractive index of the film:** This affects the light's speed within the film, further influencing the path length and interference pattern.
-   **Wavelength of light:** Different colors (wavelengths) interact differently with the film, leading to variations in the observed interference patterns.

**Applications:**

-   **Anti-reflective coatings:** Reduce unwanted reflections on lenses and eyeglasses, improving clarity and minimizing glare.
-   **Optical filters:** Selectively transmit or reflect specific wavelengths, used in cameras, microscopes, and other optical instruments.
-   **Decorative coatings:** Create iridescent colors on objects like soap bubbles, butterfly wings, and certain gemstones.

**Visualization:**

Imagine a soap bubble under sunlight. The rainbow-like colors arise from thin film interference. Depending on the viewing angle, different wavelengths experience constructive or destructive interference, highlighting specific colors.

**Additional points:**

-   Interference effects are most pronounced when the film thickness is comparable to the light's wavelength, as small path length changes can significantly impact the phase relationship.
-   Thin film interference can also occur with transmitted light, but usually reflected interference is more visible.
-   Mathematical equations can be used to calculate the specific conditions for constructive and destructive interference.

## 13. A thin film of uniform thickness is illuminated by a monochromatic light. Obtain an expression for path difference for reflected systems. Hence derive the conditions for constructive and destructive interference.
### Ans:-##   Path Difference in Thin Film Interference for Reflected Systems
In a thin film illuminated by monochromatic light, interference occurs between light reflected from the top and bottom surfaces of the film. Here's how to find the path difference and derive the conditions for constructive and destructive interference:

**1. Path Difference Calculation:**

Consider a ray of light incident on a thin film with thickness `d` and refractive index `n` (relative to the surrounding medium). Let the angle of incidence be `θ₁`.

**Reflected ray 1 (R₁):**

-   Reflects from the top surface without entering the film.
-   Path length = 2 * AB (direct path).

**Reflected ray 2 (R₂):**

-   Enters the film, travels AC + CD + DE, and reflects from the bottom surface.
-   Path length = AC + (2 * CD) + DE.

**Path difference (δ):**

δ = Path length of R₂ - Path length of R₁ δ = AC + (2 * CD) + DE - 2 * AB

Using trigonometry and Snell's Law:

-   AC = AB * sin(θ₁)
-   CD = AB * cos(θ₁) / n
-   DE = AB * sin(θ₁)

Substituting:

δ = AB * sin(θ₁) + 2 * AB * cos(θ₁) / n - 2 * AB * sin(θ₁) δ = 2 * AB * cos(θ₁) / n - AB * sin(θ₁)

**2. Conditions for Constructive and Destructive Interference:**

Constructive interference occurs when the reflected waves are in phase, meaning their path difference is an integer multiple of the wavelength (λ):

δ = mλ, where m is an integer (0, 1, 2, ...)

Destructive interference occurs when the reflected waves are out of phase by half a wavelength, meaning their path difference is an odd multiple of half the wavelength:

δ = (2m + 1)λ/2, where m is an integer (0, 1, 2, ...)

Therefore, for constructive interference:

2 * AB * cos(θ₁) / n - AB * sin(θ₁) = mλ

For destructive interference:

2 * AB * cos(θ₁) / n - AB * sin(θ₁) = (2m + 1)λ/2

These equations can be further simplified and rearranged depending on the specific problem requirements.

**Additional Notes:**

-   These conditions are for normal incidence (θ₁ = 0). For oblique angles, the analysis becomes more complex due to refraction and additional ray paths.
-   The equations account for the phase shift that occurs upon reflection at the bottom surface due to the change in refractive index.
-   In real situations, factors like non-monochromatic light, absorption within the film, and film imperfections can affect the observed interference patterns.

## 14. A parallel beam of light λ = 5890 Å is incident on glass plate of refractive index μ= 1.5 such that angle of refraction in to plate is 600. Calculate the smallest thickness of the plate which will make it appear dark by reflection .
### Ans:- For the plate to appear dark by reflection, we need to achieve **destructive interference** between the light reflected from the top and bottom surfaces of the glass plate. This occurs when the path difference between the two reflected rays is an odd multiple of half the wavelength of the light.

**1. Calculate the path difference:**

Let the thickness of the plate be `d`. The path difference (δ) between the reflected rays can be calculated using the following steps:

-   **Path length of the reflected ray from the top surface:**  This is simply twice the distance the light travels through air (refractive index = 1), which is 2d.
-   **Path length of the reflected ray from the bottom surface:**  This involves the light traveling through the glass plate, undergoing refraction at both the top and bottom surfaces, and then reflecting back out. To calculate this, we need to consider the angle of refraction within the glass (θ₂).
```
 Using Snell's Law:
    -   sin(θ₁) / sin(θ₂) = μ₁ / μ₂
    -   sin(60°) / sin(θ₂) = 1 / 1.5
    -   θ₂ ≈ 36.87°
```
The effective path length within the glass can be calculated as: - 2d / cos(θ₂)

Therefore, the total path difference is:
```
δ = 2d + 2d / cos(θ₂)
```
**2. Apply the condition for destructive interference:**

For destructive interference, the path difference must be an odd multiple of half the wavelength:
```
δ = (2n + 1)λ / 2, where n is an integer (0, 1, 2, ...)
```
Substituting the values and solving for the smallest thickness `d`:
```
2d + 2d / cos(θ₂) = (2n + 1)λ / 2 d = [(2n + 1)λ / 4] / [1 + 1 / cos(θ₂)]
```
For the smallest thickness, we want n = 0:
```
d = λ / 4 * [1 + 1 / cos(θ₂)]

d = 5890 Å / 4 * [1 + 1 / cos(36.87°)]

d ≈ 196.33 nm
```
**Therefore, the smallest thickness of the plate that will make it appear dark by reflection is approximately 196.33 nanometers.**

**Key points:**

-   The solution uses the concept of destructive interference to determine the path difference required for darkness.
-   The path difference calculation considers refraction within the glass and the angle of incidence.
-   The smallest thickness is obtained by setting the integer  `n`  to 0 in the condition for destructive interference.

## 15. A soap film of refractive index μ= 4/3 and thickness 1.5*10-4 cm is illuminated by white light incident at angle 450, The light reflected by it is examined by spectroscope in which it is found a dark band corresponding to wavelength of 5000 Å. Calculate order of interference band.
### Ans:- **1. Calculate the path difference:**

Consider the light reflecting from the top and bottom surfaces of the soap film. Due to the difference in path lengths, they interfere with each other. The path difference (δ) can be calculated as:
```
δ = 2 * thickness * cos(θ)

where:

-   thickness = 1.5 * 10^-4 cm
-   θ = angle of incidence = 45° (converted to radians for calculation: 45° * π/180° = π/4)
```
Substituting the values:
```
δ = 2 * 1.5 * 10^-4 cm * cos(π/4) ≈ 1.06 * 10^-4 cm
```
**2. Convert path difference to wavelength units:**

To compare the path difference with the wavelength of light, we need to convert it to Ångströms (Å).
```
1 cm = 10^4 Å

Therefore, the path difference in Å is:

δ ≈ 1.06 * 10^-4 cm * 10^4 Å/cm ≈ 106 Å
```
**3. Apply the condition for dark band:**

For a dark band to appear, the path difference must be an odd multiple of half the wavelength of the light.
```
δ = (2m + 1)λ / 2

where:

-   m = order of interference band (integer)
-   λ = wavelength of the dark band = 5000 Å
```
**4. Solve for the order of interference:**
```
Substitute the values of δ and λ into the equation and solve for m:

106 Å = (2m + 1) * 5000 Å / 2

Divide both sides by 5000 Å/2:

21.2 * 10^-4 = m + 1/2

Subtract 1/2 from both sides:

21.15 * 10^-4 = m
```
Therefore, the order of the interference band (m) is approximately **7**.

**Conclusion:**

The dark band observed in the spectroscope corresponds to the 7th order of interference. This means that the path difference between the reflected light rays is an odd multiple of half the wavelength of light (5000 Å) seven times.

    
