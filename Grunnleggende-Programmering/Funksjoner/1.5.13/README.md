I VG2-faget «Matematikk X» lærer elevene om begrepet kongruens. To heltall sies å være kongruente (“like”) hvis de får samme rest når vi deler på samme tall.

Eksempelvis sier vi at 27 er kongruent med 12 modulus 5 siden siden begge får samme rest når vi deler på 5.

Matematisk skriver vi at  27 ≡ 12 (mod 5)  siden  27 = 5⋅5 + 2  og  12 = 5⋅2 + 2.

Skriv en funksjon congruent som tar tre heltall, henholdsvis  a, b  og  modulus  som parametre. Funksjonen skal returnere True hvis a og b får samme rest når de deles på modulus. False returneres hvis ikke.


Funksjonen du skrev over skal brukes i et analyseprogram, der brukeren skriver inn to hele tall og får listet opp alle tallene (modulusene) som gir samme rest når en deler de to brukervalgte tallene på dem. Vi finner disse tallene ved å bruke funksjonen over med modulus opp til og med det minste av disse to tallene.
Med tallene 1337 og 42 skal vi få skrevet ut tallene {1, 5, 7, 35, 27}.