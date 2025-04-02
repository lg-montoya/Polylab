MOTIVATION = """
#### Motivation
___
When I first began studying polynomials and wanted to 
experiment with them[$^*$]
(# "Rather than "wanted to experiment with them" it was really more 
"needed to complete the homework""), 
that process required many manual[$^*$](# "Typing numbers into a calculation is still manual.") 
calculations. The steps involved resembled:

1. Creating a table with two rows: one for $x$ and another for $f(x)$.
2. For each value of $x$ using a calculator to obtain its corresponding 
 $f(x)$ value.
3. Populating the table with the calculated values.
4. Obtaining ruled paper and plotting the coordinates $(x,f(x))$.
5. Connecting all these dots as smoothly as possible.  
6. Changing one of the coefficients in the polynomial, and[$^*$](# "Very deep breath ...") 
repeating steps 1-5 . 

Drawing a quadratic using 7 points would require 42 mathematical operations in my 
head[$^*$](# "21 additions, 14 multiplications, 7 squarings." ), and I'd spend 
90% of my time on step 2[$^*$](# "Great for my mental arithmentic."), 5% 
on step 5, but only 3% 
conceptualising the relationship between coefficients and polynomial shapes[$^*$](# "Which was the exercise's raison d'etre.").
Additionally (and unfortunately), it was not uncommmon for careless mistakes[$^*$](# "Negatives (magically) becoming positives. We've all been there.") to creep into one of the
42 mathematical operations. The sketch of my graph would then look suspect, and I'd spend time[$^*$](# "That's the other 2% went in case the statisticians were wondering.")
 hunting down the error.

And all that work was just for looking at the impact on $f(x)$. If I also wanted to see 
the impact on $f'(x)$, I had to do all that work over 
again[$^*$](# "OK, there's one less term in the calculation, but still ... another deep sigh.").  

Fortunately, the manual calculations can be avoided with the use of this dashboard. We
can now focus on bending/twisting/shifting our polynomial by changing the coefficients.

Enjoy 

( Dedicated to A & H ) 
"""


# MOTIVATION = """
# #### MOTIVATION
# ___
# When I first began studying polynomials and wanted to experiment[$^1$](# "Rather than "wanted to experiment with" it was really more 
# "needed to complete the homework on"") with them,
# that process required[dsadas]("SomeHover") many manual[$^2$](#tabla-topologia) calculations. The steps involved 
# looked something like:

# 1. Create a table with two rows: one for $x$ and another for $f(x)$.
# 2. For each value of $x$ use a calculator to obtain its corresponding 
#  $f(x)$ value.
# 3. Populate the $x$, $f(x)$ table with the calculated values.
# 4. Obtain ruled paper and plot the coordinates $(x,f(x))$.
# 5. Connect all these dots as smoothly as possible.  
# 6. Change one of the coefficients in the polynomial, and[$^5$](#tabla-topologia) repeat steps
# 1-5 .

# Drawing a quadratic using 7 points would require 42 mathematical operations in my head[$^5$](#tabla-topologia).
# I would spend 90% of my time on step 2[$^5$](#tabla-topologia), 5% 
# on step 5, but only 3% 
# conceptualising the relationship between coefficients and polynomial shapes which was the exercise's raison d'etre.
# Additionally (and unfortunately), it was not uncommmon for careless mistakes[$^5$](#tabla-topologia) to creep into one of the
# 42 mathematical operations. The sketch of my graph would then look suspect, and I'd spend time[$^5$](#tabla-topologia) hunting down the error.

# And all that work was just for looking at the impact on $f(x)$. If I also wanted to see 
# the impact on its derivate $f'(x)$, I had to do all that work over again[$^4$](#tabla-topologia).  

# [$^1$]Rather than "wanted to experiment with" it was really more 
# "needed to complete the homework on".  
#  [$^2$] Typing numbers into a calculation is still manual.  
#  [$^3$] 21 additions, 14 multiplications, 7 squarings.  
#  [$^4$] Or calculator. Depending on the numbers I was working with. Scientific calculators came much later for me.    
#  [$^3$] Negatives (magically) becoming positives. We've all been there.  
#  [$^4$] OK, there's one less term in the calculation, but still.  
#  [$^5$] Very deep breath.  
#  [$^2$] That's where the other 2% went in case the statisticians were wondering.  
#  [$^2$] Great for my mental arithmetic.
 

# ##### Dog ate my homework

# """

POLYNOMIAL_INSTRUCTIONS = '''
**Dropdown**  
Begin by choosing from the dropdown the desired polynomial whose form and derivatives 
you wish to explore. The highest order polynomial available is a cubic.

**Sliders**  
They are disabled until a polynomial is selected from the dropdown.
Each polynomial has a different set of coefficients whose values are
adjusted by the sliders. The graphs (and their titles) will reflect the 
coeffiecients' changes.

**Legend**  
Activate and deactivate the traces by single clicking on the legend.
Double-click a trace to isolate it.

**Theme-toggle**  
Choose the dashboard's skin at the top right: Fluffy marshmallow
 unicorn or Witch-king of Angmar.
'''

POLYNOMIAL_ABOUT = '''
**COEFFICIENT ORDERING**  
El formulario le ayuda localisar los (casa)lotes dentro del municipio de
 Medellín. *Buscar* sera habilitado solo cuando todos los campos esten llenos.

Vias como *El Palo*, *Carabobo*, *Avenida Las Palmas* etc., se encuentran solo
 con su correspondiente Carrera, Diagonal, etc..

**A LINE! REALLY?**  
Sure why not. Not the most exciting of polynomials, but it is a polynomial
of degree 1.


**CONTINUITY AND SMOOTHNESS FOR DERIVATIVENESS 

La exactitud de los valores en la tabla mejora cuando el lote esta
 completamente dentro la(s) frontera(s). Por ejemplo un lote puede abarcar
 dos *Poligonos de Tratamientos*  en cuyo caso, la tabla exponera información
 solo de uno de esos poligonos. Una inspeción visual del mapa es recomendable
 en esos casos. Valores como *N/A*, *None* corresponde a información
 incompleta.

**A constant**  
Active y desactive capas con el widget de capas al lado superior-derecho del
 mapa. Flote sobre cualquier frontera para ver su valor.
'''

SINUSOIDAL_INSTRUCTIONS = '''
**Add Graphs**  
Click the "+" button to add a new graph with controls. A maximum of
3 graphs is allowed.

**Dropdown**  
From the dropdown choose the desired polynomial whose form and derivatives 
you wish to explore. The highest order polynomial available is a cubic.

**Sliders**  
They are disabled until a polynomial is selected from the dropdown.
Each polynomial has a different set of coefficients whose values are
adjusted by the sliders. The graphs (and their titles) will reflect the 
coeffiecients' changes.

**Legend**  
Activate and deactivate the traces by single clicking on the legend.
Double-click a trace to isolate it.

**Theme-toggle**  
Choose the dashboard's skin at the top right: Fluffy marshmallow
 unicorn or Witch-king of Angmar.
'''


