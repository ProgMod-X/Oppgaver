# Automatisert Løsningsgenerering med GPT-3

Dette prosjektet automatiserer prosessen med å generere løsningsforslag for programmeringsoppgaver ved hjelp av GPT-3, et avansert AI språkmodell utviklet av OpenAI. Målet er å hjelpe lærere, studenter og utviklere med å generere detaljerte og forklarende løsningsforslag for ulike programmeringsoppgaver.

## Innhold

- [Arbeidsflyt](#arbeidsflyt)
- [Hvordan Komme I Gang](#hvordan-komme-i-gang)
- [Konfigurasjon](#konfigurasjon)
- [Gjør Ditt Bidrag](#gjør-ditt-bidrag)
- [Lisens](#lisens)

## Arbeidsflyt

Dette prosjektet har en automatisert arbeidsflyt som består av flere skript som arbeider sammen:

1. **setup.sh**: Dette skriptet setter opp nødvendige omgivelser og avhengigheter, samt planlegger en cron-jobb for å kjøre arbeidsflytsskriptet jevnlig.

2. **AutomateWorkflow.sh**: Dette skriptet koordinerer hele prosessen. Det trekker nyeste endringer fra Git-repositoriet, oppdaterer oppgaveindeksen ved å kjøre `setup.py`, genererer løsningsforslag med `process_tasks.py`, og utfører automatisk git commit og push.

3. **process_files.py**: Dette skriptet leser en oppgavebeskrivelse og tilhørende kodeløsning, bruker GPT-3 til å generere en markdown-celle med løsningsforslag, og bygger en Jupyter Notebook-fil.

4. **process_tasks.py**: Dette skriptet oppdaterer oppgaveindeksen, sjekker hvilke oppgaver som mangler løsningsforslag, og genererer løsningsforslag for manglende oppgaver.

5. **git_commit_push.py**: Dette skriptet utfører git commit og push for å lagre løsningsforslagene i Git-repositoriet, med oppgavenavnet som commit-melding.

## Hvordan Komme I Gang

1. **Klon Repositoriene**: Klon dette prosjektets repo og script-repo til ønskede plasseringer på systemet ditt.

2. **Konfigurér API-nøkkel**: Sett din OpenAI API-nøkkel i `AutomateWorkflow.sh`, `process_files.py` og `process_tasks.py`.

3. **Kjør `setup.sh`**: Dette vil sette opp nødvendige omgivelser, installere avhengigheter og planlegge cron-jobben for automatisert løsningsgenerering.

4. **Overvåk Resultatene**: Prosjektet vil nå kjøre automatisk hver time, hente og behandle oppgaver, samt generere og lagre løsningsforslagene.

## Konfigurasjon

Du må konfigurere noen variabler før du kjører prosjektet:

- I `AutomateWorkflow.sh`, sett `OPENAI_API_KEY` til din OpenAI API-nøkkel.
- I `process_files.py` og `process_tasks.py`, sett `openai.api_key` til din OpenAI API-nøkkel.

## Gjør Ditt Bidrag

Dette prosjektet er åpent for bidrag. Hvis du vil bidra med forbedringer, rettelser eller nye funksjoner, er du velkommen til å lage en pull request.

## Lisens

Dette prosjektet er lisensiert under MIT-lisensen. Se `LICENSE`-filen for detaljer.
